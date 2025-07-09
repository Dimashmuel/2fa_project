from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm , LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import pyotp
import qrcode
import base64
from io import BytesIO

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            totp = pyotp.TOTP(user.totp_secret)
            otp_url = totp.provisioning_uri(name=user.username, issuer_name="My 2FA App")

            # generate QR image as PNG and encode in base64
            img = qrcode.make(otp_url)
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            img_str = base64.b64encode(buffer.getvalue()).decode()
            qr_data = f"data:image/png;base64,{img_str}"

            return render(request, 'accounts/qr.html', {'qr_data': qr_data})
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            token = form.cleaned_data['token']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                totp = pyotp.TOTP(user.totp_secret)
                if totp.verify(token):
                    login(request, user)
                    return render(request, 'accounts/welcome.html', {'user': user})
                else:
                    messages.error(request, "Invalid authenticator code.")
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')  # מניח שקיים view בשם login
