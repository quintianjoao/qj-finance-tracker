from flask_sqlalchemy import SQLAlchemy
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required, usd
from sqlalchemy import text

app = Flask(__name__)

# SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/João Vitor Quintian/qjpft/personal_finance_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# SQLAlchemy
db = SQLAlchemy(app)

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
@login_required
def index():
    """Overview"""
    
    # Call the incomes from db
    incomes = db.session.execute(
        text("SELECT type, name, tag, value, date, notes FROM finances WHERE user_id = :user_id AND type = 'income' ORDER BY date ASC"),
        {"user_id": session["user_id"]}
    ).mappings().all()

     # Calculate total income earned
    total_income_query = db.session.execute(text("SELECT SUM(value) FROM finances WHERE type='income'")).fetchone()
    total_income = total_income_query[0] if total_income_query[0] else 0
    
    
    #Call expenses from db
    expenses = db.session.execute(
        text("SELECT type, name, tag, value, date, notes FROM finances WHERE user_id = :user_id AND type = 'expense' ORDER BY date ASC"),
        {"user_id": session["user_id"]}
    ).mappings().all() 

    # Calculate total expenses
    total_expense_query = db.session.execute(text("SELECT SUM(value) FROM finances WHERE type='expense'")).fetchone()
    total_expenses = total_expense_query[0] if total_expense_query[0] else 0


    #Calculate income still available
    income_still_available = total_income - total_expenses

     #Turn income_still_available in dollars
    income_still_available = usd(round(income_still_available))


    return render_template("index.html", incomes=incomes, expenses=expenses, income_still_available=income_still_available )


@app.route("/incomes")
@login_required
def incomes():
    """Show Incomes"""

    # Call incomes from db
    incomes = db.session.execute(
        text("SELECT type, name, tag, value, date, notes FROM finances WHERE user_id = :user_id AND type = 'income' ORDER BY date ASC"),
        {"user_id": session["user_id"]}
    ).mappings().all()
    
    # Calculate total income earned
    total_income_query = db.session.execute(text("SELECT SUM(value) FROM finances WHERE type='income'")).fetchone()
    total_income = total_income_query[0] if total_income_query[0] else 0
    
    # Turn total_income into dollars
    total_income = usd(round(total_income))

    #Call expenses from db
    expenses = db.session.execute(
        text("SELECT type, name, tag, value, date, notes FROM finances WHERE user_id = :user_id AND type = 'expense' ORDER BY date ASC"),
        {"user_id": session["user_id"]}
    ).mappings().all() 

    # Calculate total expenses
    total_expense_query = db.session.execute(text("SELECT SUM(value) FROM finances WHERE type='expense'")).fetchone()
    total_expenses = total_expense_query[0] if total_expense_query[0] else 0

    # Turn total_expenses into dollars
    total_expenses = usd(round(total_expenses))

    # Render Page
    return render_template("incomes.html", incomes=incomes, total_income=total_income)


@app.route("/add_income", methods=["GET", "POST"])
def add_income():
    """Add Income"""

    # Form presented to user fill and add a income
    if request.method == "POST":
        income_name = request.form.get("income_name").upper()
        income_tag = request.form.get("income_tag").upper()
        income_value = request.form.get("income_value")
        income_date = request.form.get("income_date")
        income_notes = request.form.get("income_notes").upper()

        # Error messages
        if not income_name:
            return apology("Must Provide Name")
        elif not income_tag:
            return apology("Must Provide Tag")
        elif not income_date:
            return apology("Must Provide Date")
        
        # Insert data into db
        db.session.execute(
            text("INSERT INTO finances (user_id, type, name, tag, value, date, notes) VALUES (:user_id, :type, :income_name, :income_tag, :income_value, :income_date, :income_notes)"),
            {
                "user_id": session["user_id"],
                "type": 'income',
                "income_name": income_name,
                "income_tag": income_tag,
                "income_value": income_value,
                "income_date": income_date,
                "income_notes": income_notes
            }
        )
        db.session.commit()  
        
        # Prompt user with information added
        flash(f"Income {income_name} in the value of {income_value} added")
        return redirect("/")
    
    else:
        return render_template("add_income.html")
    

@app.route("/remove_income", methods=["GET", "POST"])
@login_required
def remove_income():
    """Remove Income"""

    # Query the db for existent incomes
    incomes = db.session.execute(
        text("SELECT name FROM finances WHERE type='income' AND user_id = :user_id"),
        {"user_id": session["user_id"]}
    ).mappings().all()  

    if request.method == "POST":
        income_name = request.form.get("income_name")

        # Deletion of selected income
        db.session.execute(
            text("DELETE FROM finances WHERE name = :income_name AND type='income' AND user_id = :user_id"),
            {"income_name": income_name, "user_id": session["user_id"]}
        )
        db.session.commit()  

        flash(f"Income '{income_name}' removed successfully!")
        return redirect("/incomes")

    return render_template("remove_income.html", incomes=incomes)





@app.route("/expenses")
@login_required
def expenses():
    """Show Expenses"""

   #Call expenses from db
    expenses = db.session.execute(
        text("SELECT type, name, tag, value, date, notes FROM finances WHERE user_id = :user_id AND type = 'expense' ORDER BY date ASC"),
        {"user_id": session["user_id"]}
    ).mappings().all() 

    # Calculate total expenses
    total_expense_query = db.session.execute(text("SELECT SUM(value) FROM finances WHERE type='expense'")).fetchone()
    total_expenses = total_expense_query[0] if total_expense_query[0] else 0

    # Turn total_expenses into dollars
    total_expenses = usd(round(total_expenses))

    # Render Page
    return render_template("expenses.html", expenses=expenses, total_expenses=total_expenses)


@app.route("/add_expense", methods=["GET", "POST"])
def add_expense():
    """Add Expense"""
     # Form presented to user fill and add a income
    if request.method == "POST":
        expense_name = request.form.get("expense_name").upper()
        expense_tag = request.form.get("expense_tag").upper()
        expense_value = request.form.get("expense_value")
        expense_date = request.form.get("expense_date")
        expense_notes = request.form.get("expense_notes").upper()

        # Error messages
        if not expense_name:
            return apology("Must Provide Name")
        elif not expense_tag:
            return apology("Must Provide Tag")
        elif not expense_date:
            return apology("Must Provide Date")
        
        # Insert data into db
        db.session.execute(
            text("INSERT INTO finances (user_id, type, name, tag, value, date, notes) VALUES (:user_id, :type, :expense_name, :expense_tag, :expense_value, :expense_date, :expense_notes)"),
            {
                "user_id": session["user_id"],
                "type": 'expense',
                "expense_name": expense_name,
                "expense_tag": expense_tag,
                "expense_value": expense_value,
                "expense_date": expense_date,
                "expense_notes": expense_notes
            }
        )
        db.session.commit()  
        
        # Prompt user with information added
        flash(f"Expense {expense_name} in the value of {expense_value} added")
        return redirect("/")
    
    else:
        return render_template("add_expense.html")



@app.route("/remove_expense", methods=["GET", "POST"])
@login_required
def remove_expense():
    """Remove Expense"""

    # Query the db for existent expenses
    expenses = db.session.execute(
        text("SELECT name FROM finances WHERE type='expense' AND user_id = :user_id"),
        {"user_id": session["user_id"]}
    ).mappings().all()  

    if request.method == "POST":
        expense_name = request.form.get("expense_name")

        # Deletion of selected expense
        db.session.execute(
            text("DELETE FROM finances WHERE name = :expense_name AND type='expense' AND user_id = :user_id"),
            {"expense_name": expense_name, "user_id": session["user_id"]}
        )
        db.session.commit()  

        flash(f"Expense '{expense_name}' removed successfully!")
        return redirect("/expenses")

    # Convert the query result into a dictionary
    expenses = [{'name': row['name']} for row in expenses]

    return render_template("remove_expense.html", expenses=expenses)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user ID
    session.clear()

    # User reached route via POST
    if request.method == "POST":
        # Check for username
        if not request.form.get("username"):
            return apology("must provide username", 403)
        
        # Check for password
        elif not request.form.get("password"):
            return apology("must provide password", 403)
        
        # Query to retrieve the user data
        rows = db.session.execute(
            text("SELECT id, hash FROM users WHERE username = :username"),
            {"username": request.form.get("username")}
        ).mappings().all()

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)
        
        # Save user_id in session
        session["user_id"] = rows[0]["id"]

        # Redirect to home page
        return redirect("/")
    
    # User reached route via GET
    else:
        return render_template("login.html")



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register User FIRST"""
    session.clear()

    if request.method == "POST":
        if not request.form.get("username"):
            return apology("must provide username", 400)

        elif not request.form.get("password"):
            return apology("must provide password", 400)

        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("Passwords do not match", 400)


        # Query to check if username exists
        rows = db.session.execute(
            text("SELECT * FROM users WHERE username = :username"), {"username": request.form.get("username")}).mappings().all()
        session["user_id"] = rows[0]["id"]

        if rows:
            return apology("username already exists", 400)

        # Insert new user
        db.session.execute(
            text("INSERT INTO users (username, hash) VALUES (:username, :hash)"),
            {
                "username": request.form.get("username"),
                "hash": generate_password_hash(request.form.get("password"))
            }
        )
        db.session.commit()

        # Get the user id
        rows = db.session.execute(
            text("SELECT * FROM users WHERE username = :username"),
            {"username": request.form.get("username")}
        ).fetchall()
        
        session["user_id"] = rows[0]["id"]

        return redirect("/")

    else:
        return render_template("register.html")

@app.route("/logout")
def logout():
    """Log user out"""

    session.clear()

    return redirect("/")