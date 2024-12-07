# QJPFT - QuintianJoao Personal Finance Tracker

This project is a **Personal Finance Tracker** application built with **Flask**, **SQLAlchemy**, and **Flask-Migrate**. It empowers users to manage their finances by tracking incomes and expenses while offering insightful financial summaries. The application includes features such as user authentication, secure session handling, and robust database management.

## Features

- **User Authentication**: Secure registration, login, and logout functionality.
- **Income and Expense Management**: Add, view, and delete financial entries categorized by type, tag, and date.
- **Financial Overview Dashboard**: Displays total income, total expenses, and remaining income in a user-friendly interface.
- **Database Management**: Utilizes SQLAlchemy with support for migrations through Flask-Migrate, ensuring scalability and ease of updates.
- **Error Handling**: Provides informative feedback for user actions and input validation errors.
- **Custom Jinja Filters**: Includes a custom `usd` filter to format monetary values.

## Prerequisites

- **Python 3.13.0** or higher
- **pip** (Python package manager)
- **SQLite** (Default database; can be swapped with other RDBMS, such as PostgreSQL or MySQL)
- Environment variables defined in a `.env` file (e.g., `DATABASE_URL` for database connection)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/quintianjoao/qj-finance-tracker.git
   cd qjpft
