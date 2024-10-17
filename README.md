
# 🔄 LastPass to Apple Passwords Converter 🔐

## 🚀 Overview
Have you tried importing your LastPass passwords into Apple's new *Passwords* app on macOS, only to find that it's not so straightforward? 😤 Worry no more! This Python script helps you convert your LastPass CSV export into the exact format needed by Apple’s Passwords app, making the switch super easy! 🎉

## ✨ Features
- Converts LastPass CSV export to Apple *Passwords* app format.
- Keeps it simple: just input the LastPass CSV, and it does the rest.
- Handles `Title`, `URL`, `Username`, `Password`, `Notes`, and `OTPAuth`.

## 🍏 Why Use Apple Passwords Instead of LastPass?
- **Built-in**: If you're in the Apple ecosystem, Passwords.app is baked into macOS, iOS, iPadOS, and even Apple Vision Pro. No extra apps needed!
- **Secure**: End-to-end encryption ensures that even Apple can't access your data.
- **Seamless Sync**: Passwords and passkeys sync across all Apple devices via iCloud.
- **Passkeys Support**: Apple's app already supports next-gen passkey authentication, which is more secure and phishing-resistant. 🔐

## 🔧 How It Works
This script reads the CSV file exported from LastPass, transforms the data into a compatible format, and saves it into a new CSV that can be imported directly into Apple Passwords. 🛠️

🔒 **Important Note**: The script only processes login credentials (URL, Username, Password, etc.). Secure notes, payment cards, and other non-login data from LastPass are **excluded** from this conversion.

- **From LastPass**: `url`, `username`, `password`, `extra`, `name`.
- **To Apple Passwords**: `Title`, `URL`, `Username`, `Password`, `Notes`, and `OTPAuth` (left blank for now).

## 🛠️ Installation

1. **Clone this repo**:
   ```bash
   git clone https://github.com/yourusername/lastpass-to-apple-passwords.git
   cd lastpass-to-apple-passwords
   ```

2. **Install Python**: If you don’t have Python 3 installed, get it [here](https://www.python.org/downloads/).

3. **Run the script**:
   ```bash
   python3 lastpass_to_apple_passwords.py
   ```

## 📝 Usage

1. Export your passwords from LastPass as a CSV file:
   - Log into LastPass.
   - Navigate to **Advanced Options** -> **Export**.
   - Save the CSV file on your system.

2. Run the Python script:
   - You will be prompted to provide the file paths for the LastPass export and the output file for Apple Passwords. You can leave them as default or specify your own.

3. Import the generated CSV into the *Passwords* app:
   - Open the *Passwords* app on macOS.
   - Go to **File** -> **Import Passwords**, select the CSV file, and you’re done! 🎉

## 🔐 Security Considerations

⚠️ **Important**: The CSV files created by this script contain your passwords in **plain text** (unencrypted). Make sure to securely delete both the LastPass export and the Apple Passwords CSV file after you complete the import:
   ```bash
   rm lastpass_export.csv apple_passwords_import.csv
   ```
   Failure to do so can expose your passwords to unauthorized access! 💀

---

### 🏆 Contributions
Feel free to fork, improve, or report issues! Let's make this smoother for everyone. 😊
