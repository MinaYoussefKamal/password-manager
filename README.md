# 🔐 Password Manager (Python + Tkinter)

A simple password manager built in **Python** with a clean **dark-themed Tkinter GUI**.
It can generate secure passwords, save them locally in a JSON file, and retrieve them later with a search function.
This project helped me practice GUIs, file handling, and improving user experience.

---

## ✨ Features

* **Password Generator** → creates strong random passwords with letters, numbers, and symbols.
* **Clipboard Integration** → new passwords are automatically copied.
* **Save Accounts** → store website, email/username, and password in a local JSON file.
* **Search** → quickly find saved logins by website name.
* **Overwrite Protection** → warns before replacing an existing account.
* **Error Handling** → prevents saving empty fields and handles missing/corrupt files.
* **Dark Theme UI** → consistent colors for a clean look.

---

## 📂 Project Structure

```
Password-Manager/
│-- main.py
│-- logo.png
│-- icon.ico
│-- data.json.example   # empty example file to show format
│-- README.md
```

---

## 🚀 How to Run

1. Clone the repo:

   ```bash
   git clone https://github.com/your-username/password-manager.git
   ```
2. Navigate to the folder:

   ```bash
   cd password-manager
   ```
3. Install dependencies:

   ```bash
   pip install pyperclip
   ```
4. Run the app:

   ```bash
   python main.py
   ```

---

## 📄 Example Data Format

```json
{
  "example.com": {
    "email": "user@example.com",
    "password": "aStrongPassword123!"
  }
}
```

---

## 🔮 Possible Future Features

* Data encryption for stronger security
* Sorting/organizing accounts
* A more modern UI using [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)

---

## 🧑‍💻 About

This project was built as part of my learning journey in Python and Tkinter.
It’s not meant to replace a professional password manager, but it was a great way to practice GUIs, JSON handling, and UX design ideas.
