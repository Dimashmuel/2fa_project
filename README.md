# Two-Factor Authentication (2FA) System with Django

This project is a secure Django web application that implements Two-Factor Authentication (2FA) using TOTP (Time-based One-Time Passwords), compatible with apps like Google Authenticator.

---

## 🔐 Features

- User registration with password and TOTP setup  
- QR code generation for Authenticator apps  
- Login using password + TOTP  
- Admin panel to view and manage users  
- Basic Bootstrap UI  

---

## 🛠️ Technology Stack

- **Python 3.13**
- **Django 5.2**
- **SQLite** (default DB)
- **PyOTP** – TOTP generation
- **qrcode** – QR code creation
- **Bootstrap 5** – UI styling

---

## 🚀 How to Run the Project

```bash
# 1. Clone or download the project
git clone https://github.com/yourusername/2fa_project.git
cd 2fa_project

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install django pyotp qrcode

# 4. Run migrations
python manage.py migrate

# 5. Create superuser (optional)
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver
```

Visit: http://127.0.0.1:8000/

---

## 📱 TOTP Setup

When registering, a QR code is displayed.  
Scan it using **Google Authenticator**   
At login, enter both your **password** and the **current TOTP code** from the app.

---

## 📂 Project Structure

```
2fa_project/
│
├── core/                  # Django project settings
├── accounts/              # App with models, views, forms
│   └── templates/accounts/
├── db.sqlite3             # SQLite database
├── manage.py              # Django CLI
├── venv/                  # Python virtual environment
└── README.md              # Project instructions
```

---

## ✅ Future Enhancements

- Lock user account after multiple failed login attempts  
- Add password reset via email  
- Provide backup/recovery codes  
- REST API + React frontend  

---

## 📄 License

This project is for educational use.
