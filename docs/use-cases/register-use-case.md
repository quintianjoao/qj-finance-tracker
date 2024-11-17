# Use Case: User Registration

## **Change Log**
| Date       | Change Description               | Version | Author              |
|------------|----------------------------------|---------|---------------------|
| 16/11/2024 | Created initial use case document| 1.0     | João Vitor Quintian |

## **Description**
This use case describes the process for user registration within the application. It includes validating user input, creating a new user account, securely storing the password, and managing potential errors related to existing usernames or mismatched passwords.

---

## **Primary Actor(s)**
- **User:** An individual who wants to create an account to access the application and manage their finances.

## **Stakeholders and Interests**
- **User:** Wants to create an account in the system to manage their financial records.
- **System:** Ensures valid user registration and proper handling of errors like duplicate usernames or mismatched passwords.

---

## **Preconditions**
- The user is not already registered in the system.
- The system is connected to the database and operational.

---

## **Main Flow**
### **User Registration Process**
1. The user navigates to the registration page.
2. The user enters a **username**, **password**, and **password confirmation** in the registration form.
3. The system checks if both the **username** and **password** fields are provided.
   - If either field is missing, the system prompts the user with an error message: "Must provide username" or "Must provide password."
4. The system checks if the **password** and **confirmation** match.
   - If the passwords do not match, the system displays the error message: "Passwords do not match."
5. The system queries the database to check if the **username** already exists.
   - If the **username** exists, the system prompts the user with an error message: "Username already exists."
6. The system inserts the new user into the database with the **username** and the **hashed password**.
   - The password is hashed using **Werkzeug**’s `generate_password_hash` method for secure storage.
7. After successful registration, the system logs the user in by creating a session with the **user_id** and redirects them to the homepage (`/`).

---

## **Alternative Flows**
### **01. Missing Username or Password**
1. The system checks if the **username** or **password** is missing.
2. If missing, the system displays the appropriate error message:
   - "Must provide username."
   - "Must provide password."
3. The user corrects the input and resubmits the form.

### **02. Passwords Do Not Match**
1. The system verifies if the **password** and **confirmation** match.
2. If they do not match, the system displays the error message: "Passwords do not match."
3. The user corrects the input and resubmits the form.

### **03. Username Already Exists**
1. The system checks if the **username** already exists in the database.
2. If the **username** exists, the system displays the error message: "Username already exists."
3. The user selects a different **username** and resubmits the form.

---

## **Non-Functional Requirements**
- Registration process must complete in less than **5 seconds**.
- The system must securely store passwords using **password hashing** (e.g., **Werkzeug’s `generate_password_hash`**).
- The system should provide real-time error feedback for missing fields, mismatched passwords, or existing usernames.

---

## **Postconditions**
- If the registration is successful, a new user account is created, and the user is logged in automatically.
- If the registration fails, the user is prompted with appropriate error messages and remains on the registration page.

---

## **Business Rules**
BR01 - Each user must have a unique **username**.  
BR02 - Passwords must be securely hashed before being stored in the database.  
BR03 - The **password** and **confirmation** must match exactly.  
BR04 - The system should prevent the use of already registered usernames.

---

## **Technical Notes**
- **Framework:** Uses **Flask** as the web framework and **Flask-Session** for session management.
- **Database:** User credentials are stored in the **SQLite** database (`users` table).
- **Password Handling:** The password is hashed using **Werkzeug**'s `generate_password_hash` function.
- **Session Management:** A session is created using **Flask-Session** to store the authenticated user's **user_id** upon successful registration.
