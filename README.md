# SauceDemo Playwright Automation

## Project Overview

This project uses **Python, pytest, and Playwright** to automate web UI testing for **SauceDemo (Swag Labs)**.

The test suite covers key e-commerce workflows, including successful and invalid login attempts, adding and removing items from the shopping cart, and completing the checkout process.

## Test Coverage

- Verify successful login with valid credentials.
- Verify that an error message appears when an incorrect password is entered.
- Verify that adding an item to the cart updates the cart badge to `1`.
- Verify that removing the item makes the cart badge disappear.
- Verify that completing checkout displays the order confirmation message.

## How to Run

Open a terminal in the project root directory and follow these steps.

**1. Create a virtual environment (Windows)**

```powershell
python -m venv .venv
```

**2. Activate the virtual environment (PowerShell)**

```powershell
.\.venv\Scripts\Activate.ps1
```

**3. Install the required dependencies**

```powershell
python -m pip install -r requirements.txt
```

**4. Install the Chromium browser** 

```powershell
python -m playwright install chromium
```

**5. Run the automated tests**

Open a terminal in the project root directory and follow these steps.

**1. Create a virtual environment (Windows)**

```powershell
python -m venv .venv
```

**2. Activate the virtual environment (PowerShell)**

```powershell
.\.venv\Scripts\Activate.ps1
```

**3. Install the required dependencies**

```powershell
python -m pip install -r requirements.txt
```

**4. Install the Chromium browser**

```powershell
python -m playwright install chromium
```

**5. Run the automated tests**## How to Run

Open a terminal in the project root directory and follow these steps.

**1. Create a virtual environment (Windows)**

```powershell
python -m venv .venv
```

**2. Activate the virtual environment (PowerShell)**

```powershell
.\.venv\Scripts\Activate.ps1
```

**3. Install the required dependencies**

```powershell
python -m pip install -r requirements.txt
```

**4. Install the Chromium browser**

```powershell
python -m playwright install chromium
```

**5. Run the automated tests**

```powershell
pytest --headed
```

The browser will open automatically, execute the tests, and display the results in the terminal.

```powershell
pytest --headed
```

The browser will open automatically, execute the tests, and display the results in the terminal.ests**

```powershell
pytest --headed
```

The browser will open automatically, execute the tests, and display the results in the terminal.
