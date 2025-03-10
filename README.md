# 📧 Python Email Automation System

A Python-based email automation tool that securely sends emails using **Gmail SMTP & App Password**. It includes:
- 🔐 **Two-Factor Authentication (2FA) using OTP**
- 🛡️ **Phishing Detection using Regex**
- 🔒 **Secure TLS Encryption**
- 📜 **Logging for Email Activity Tracking**

## 🚀 Features
- **Secure Email Sending:** Uses Gmail SMTP with App Password authentication.
- **Two-Factor Authentication (2FA):** Ensures only authorized users can send emails.
- **Phishing Content Filter:** Blocks emails with suspicious keywords or links.
- **TLS Encryption:** Ensures email data is transmitted securely.
- **Activity Logging:** Records sent emails and potential security issues.

## 🛠️ Setup & Installation
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/Kkpthant/email-automation-system.git
cd email-automation-system

## 🔐 Setup Your Own Credentials
Before running the script, create a `.env` file with your own Gmail credentials.

### **1️⃣ Enable 2-Step Verification on Gmail**
- Go to [Google Security](https://myaccount.google.com/security).
- Enable **2-Step Verification**.

### **2️⃣ Generate a Gmail App Password**
- Visit [App Passwords](https://myaccount.google.com/apppasswords).
- Choose **Mail** and **Windows Computer**.
- Copy the **16-character App Password**.

### **3️⃣ Create a `.env` File**
Run this command in the terminal:
```sh
touch .env && nano .env

Then, paste the following:
EMAIL_SENDER=your-email@gmail.com
EMAIL_PASSWORD=your-app-password
EMAIL_RECEIVER=recipient@example.com

### **4️⃣ Run the Script
python email_bot.py

✅ Now, the script will send an email using your credentials.

