# Two-Factor Authentication (2FA) System with Django

A secure Django web application implementing Two-Factor Authentication (2FA) using Time-based One-Time Passwords (TOTP), fully compatible with mobile authenticator apps such as Google Authenticator.

---

## 🔐 Features

- Secure user registration with password and TOTP secret generation
- Automatic QR code creation for easy configuration in Authenticator apps
- Login process requires both password and time-based one-time code
- Admin panel via Django's built-in admin interface
- Clean and responsive UI using Bootstrap 5

---

## 🛠️ Technology Stack

- **Python 3.13**
- **Django 5.2** – Web framework
- **SQLite** – Lightweight built-in database
- [**PyOTP**](https://pypi.org/project/pyotp/) – TOTP generation (RFC 6238)
- [**qrcode**](https://pypi.org/project/qrcode/) – QR code creation for 2FA
- **Bootstrap 5** – Simple and responsive UI

---

## 🚀 How to Run the Project

## 🚀 How to Run the Project

```bash
# 1. Clone the repository
git clone https://github.com/Dimashmuel/2fa_project.git
cd 2fa_project

# 2. Create and activate a virtual environment (Windows)
python -m venv venv
venv\Scripts\activate

# 3. Install required packages
pip install -r requirements.txt
# Or manually:
# pip install django pyotp qrcode

# 4. Apply database migrations
python manage.py migrate

# 5. (Optional) Create an admin user to access Django admin
python manage.py createsuperuser

# 6. Start the development server
python manage.py runserver


Visit: http://127.0.0.1:8000/

---

## 📱 TOTP Setup

During registration, a unique QR code is displayed.  
Scan it using an app such as **Google Authenticator** .

Once scanned, the app will generate a new 6-digit TOTP code every 30 seconds.  
At login, you must enter both your **password** and the **current code** from the app.

This ensures secure two-factor authentication (2FA) using the [TOTP standard (RFC 6238)](https://datatracker.ietf.org/doc/html/rfc6238).


--
## 👤 Author

- Created by Shmuel Dima
- ID: 310782164

