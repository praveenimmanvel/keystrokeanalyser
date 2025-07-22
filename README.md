# KeystrokeAnalyser 🔐

**Created by Praveen C Immanuel**

## 📌 Overview
KeystrokeAnalyser is a cross-platform Python application that monitors global keystrokes and captures screenshots whenever a wrong password is entered. It is designed for security learning and analysis.

## ✅ Features
- Logs all keystrokes globally
- Detects wrong password attempts
- Takes screenshots on each wrong attempt
- Stores logs and screenshots in timestamped format
- Unlimited wrong attempts support
- Works on both **Windows** and **Linux**
- Background execution supported

## 🛠 Technologies Used
- Python 3
- [pynput](https://pypi.org/project/pynput/)
- [pillow (PIL)](https://pypi.org/project/Pillow/)
- [pyinstaller](https://www.pyinstaller.org/)

## 📁 Folder Structure
```
C:/Users/Administrator/Downloads/
├── keystrokeanalyser_crossplatform.exe
└── logs/
    ├── keystroke_log.txt
    └── screenshots/
        ├── wrong_attempt_YYYY-MM-DD_HH-MM-SS.png
```

## 🚀 How to Run (Windows)
1. Double-click the compiled `keystrokeanalyser_crossplatform.exe`
2. It runs in the background.
3. Type passwords anywhere (terminal, browser, etc.).
4. If the password is wrong, screenshot and keystroke are saved in `logs/`.

## ⚠ Legal Disclaimer
This tool is made for **educational and ethical use only**. Unauthorized use on devices you do not own or have permission to monitor may violate laws.

---

## 📷 Screenshots
See sample logs and screenshot outputs inside `logs/` folder or refer to `Final_KeystrokeAnalyser_Report_Praveen.docx`.

---

## 🧠 Author
Praveen C Immanuel  
Python & Cybersecurity Enthusiast