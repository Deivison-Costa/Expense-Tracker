# Expense Tracker Application
This is a simple Expense Tracker web application built using Flask, a Python web framework. It allows users to track their expenses and incomes, view the list of expenses and incomes, and visualize their financial data using bar charts.

# Installation and Setup
Clone the repository or download the source code.

Make sure you have Python installed on your system (Python 3.6 or higher is recommended).

## Create a virtual environment (optional, but recommended):
    pip install virtualenv
    python -m venv venv
    source venv/bin/activate  
    On Windows: venv\Scripts\activate

## Install the required dependencies:
    pip install Flask

# Usage
Ensure you are in the project directory.

Run the app.py file to start the Flask application:
        python app.py
Open your web browser and go to http://localhost:5000/ to access the Expense Tracker application.

# Features
## Home Page
The home page displays a list of expenses and incomes along with input fields to add new expenses and incomes.

## Adding Expenses and Incomes
To add a new expense or income, simply enter the amount in the respective input field and click the "Add" button.

## Analytics Page
Clicking on the "View Analytics" button on the home page will take you to the Analytics page. This page visualizes the expenses and incomes using a bar chart.

# Technology Stack
### Python
### Flask
### SQLite (for database storage)
### Bootstrap (for styling)
### Plotly (for data visualization)
