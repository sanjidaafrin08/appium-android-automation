#  Mobile App Automation – Appium + Python + Pytest

This repository contains **mobile application automation test scripts** for HR module workflows using **Appium**, **Python**, and **Pytest**.  
The automation covers two main scenarios:  
1. **Attendance Report Search**  
2. **Check-IN & Leave Application Creation**  

GitHub Repository: [appium-android-automation](https://github.com/sanjidaafrin08/appium-android-automation)

---

##  Features Automated

### 1️⃣ Attendance Report Search
- Launch mobile application
- Navigate to **HR → My Attendance**
- Select **From Date** and **To Date** (gap ≤ 1 month)
- Filter results by **Status: On Leave**
- Validate that results are displayed
- Capture a screenshot of the search results

### 2️⃣ Check-IN & Leave Application Creation
- Launch mobile application
- Navigate to **HR → Check-IN**
- Complete check-in process
- Navigate to **HR → Leave Application**
- Select leave type, from/to dates, and enter reason
- Submit leave application
- Capture a screenshot of the confirmation

---

## Technology Stack

- **Programming Language:** Python 3.x
- **Automation Tool:** Appium
- **Test Framework:** Pytest
- **Device/Platform:** Android (Real Device / Emulator)
- **IDE:** Visual Studio Code
- **Mobile Environment:** Android Studio (AVD) / USB Debugging
- **Locator Tool:** Appium Inspector

---
## 📂 Project Structure
appium-android-automation/
│
├── tests/
│ ├── test_attendance_report.py # Attendance Report Search test
│ ├── test_hr_checkin.py # Check-IN & Leave Application test
│
├── utils/
│ ├── setup.py # Appium driver setup (Pytest fixture)
│
├── screenshots/ # Screenshots from test runs
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## Setup Instructions

### 1️⃣ Clone Repository
```bash
git clone https://github.com/sanjidaafrin08/appium-android-automation.git
cd appium-android-automation
2️⃣ Install Python Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Install & Run Appium
Install Appium Server or Appium Desktop

Start the Appium server at:

cpp
Copy
Edit
http://127.0.0.1:4723
4️⃣ Android Setup
Install Android Studio

Configure Android SDK and Emulator (or connect a real device with USB debugging enabled)

Ensure device/emulator is visible:

bash
Copy
Edit
adb devices
5️⃣ Appium Inspector
Use Appium Inspector to identify element locators

▶️ Running Tests
Run all tests:

bash
Copy
Edit
pytest -v --html=report.html --self-contained-html
Run a specific test file:

bash
Copy
Edit
pytest tests/test_attendance_report.py -v
Screenshots
All screenshots will be saved automatically in the screenshots/ directory after test execution.
 Author
Sanjida Afrin
Software QA Engineer
GitHub: sanjidaafrin08



