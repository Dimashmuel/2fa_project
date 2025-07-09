from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # ← הוספה חדשה

urlpatterns = [
    path('', lambda request: redirect('login')),  # ← נתיב ראשי שולח ל-login
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
]
