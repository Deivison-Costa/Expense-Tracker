# Expense Tracker Application
- This is a simple Expense Tracker web application built using Flask, a Python web framework. It allows users to track their expenses and incomes, view the list of expenses and incomes, and visualize their financial data using bar charts.

![Figure 1](https://github.com/Deivison-Costa/Expense-Tracker/assets/112001225/6867cf2c-f5cc-449c-8501-109e4cb23b11)
![Figure 2](https://github.com/Deivison-Costa/Expense-Tracker/assets/112001225/4d0a7a0b-bad6-4c32-8324-50173e9081d1)

# Installation and Setup
- Clone the repository or download the source code.
- Make sure you have Python installed on your system (Python 3.6 or higher is recommended).

## Create a virtual environment (optional, but recommended):
### On Windows:
    pip install virtualenv
    virtualenv venv
    .\venv\Scripts\Activate.ps1

### On Linux:
    sudo apt-get install python3-venv
    python3 -m venv venv
    source meu_env/bin/activate

## Install the required dependencies:
    pip install Flask

# Usage
- Ensure you are in the project directory.
## Run the app.py file to start the Flask application:
    python app.py
- Open your web browser and go to http://localhost:5000/ to access the Expense Tracker application.

# Features
## Home Page
- The home page displays a list of expenses and incomes along with input fields to add new expenses and incomes.

## Adding Expenses and Incomes
- To add a new expense or income, simply enter the amount in the respective input field and click the "Add" button.

## Analytics Page
- Clicking on the "View Analytics" button on the home page will take you to the Analytics page. This page visualizes the expenses and incomes using a bar chart.

# Technology Stack
- Python.
- Flask.
- SQLite (for database storage).
- Bootstrap (for styling).
- Plotly (for data visualization).
