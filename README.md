# 🎮 Nintendo Website Automated Testing with Playwright (Python)

This project is a complete UI automation test suite for the official [Nintendo US website](https://www.nintendo.com/us/), built using **Playwright** in **Python**.  
It follows the **Page Object Model (POM)** design pattern for better scalability and maintainability.

---

## 🧪 Project Overview

- ✅ Automated functional tests for navigation, filters, and forms
- 🌐 Covers multiple site areas: **Explore**, **Shop**, **Characters**, and **Support**
- 🔐 Includes sign-up flow tests with validation
- 💥 Stress and regression tests
- 📸 Highlighting UI elements during interaction
- 🚀 Pytest + Allure for rich reporting

---

## 📁 Project Structure

```
NintendoProject/
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   ├── explore.py
│   ├── characters.py
│   ├── shop.py
│   ├── shop_games.py
│   ├── shop_store_exclusives.py
│   └── sign_up.py
│
├── tests/
│   ├── base_test.py
│   ├── test_all.py
│   ├── test_home_page.py
│   ├── test_explore.py
│   ├── test_shop.py
│   ├── test_characters.py
│   ├── test_sign_up.py
│   ├── test_bdika.py
│   └── conftest.py
│
├── .venv/                # Virtual environment
├── requirements.txt      # Dependencies
└── README.md
```

---

## 🛠️ Technologies Used

- **Playwright (Python)**
- **Pytest**
- **Allure** – test reporting
- **Page Object Model (POM)** structure
- **Python 3.10+**

---

## 🚀 How to Run

1. 📦 Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. ▶️ Run tests with pytest:
   ```bash
   pytest tests/
   ```

3. 📊 (Optional) Generate Allure Report:
   ```bash
   pytest --alluredir=allure-results
   allure serve allure-results
   ```

---

## 💡 Highlights

- Smart element interaction using custom `BasePage` with:
  - `highlight()` method for UI debugging
  - Safe `wait_for()` and error handling
- SlowMo & debugging options available
- Rich test coverage across:
  - Navigation
  - Category browsing
  - Form validation
  - Sign-up errors and flow logic

---

## 📸 Screenshots (optional)

_Add sample test screenshots here if needed._

---

## 🤝 Contributing

Pull requests and feedback are welcome!  
For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

MIT License © 2025 Nadav Sagie
