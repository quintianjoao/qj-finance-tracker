# Use Case: Login Management

## **Change Log**
| Date       | Change Description               | Version | Author              |
|------------|----------------------------------|---------|---------------------|
| 16/11/2024 | Created initial use case document| 1.0     | João Vitor Quintian |

## **Description**
This use case describes the process for user login within the application. It includes validating user credentials, creating a session for the authenticated user, and handling errors related to incorrect login attempts. The system ensures that only valid users can access the main functionality of the app.

---

## **Primary Actor(s)**
- **User:** An individual who wants to access their personal financial data within the application.

## **Stakeholders and Interests**
- **User:** Wants to securely log in to the system to manage their financial records.
- **System:** Ensures proper authentication and access control for users.

---

## **Preconditions**
- The user must have an existing account in the system.
- The system is connected to the database and operational.

---

## **Main Flow**
### **Login Process**
1. The user navigates to the login page.
2. The user enters their **username** and **password** in the login form.
3. The system checks if both **username** and **password** are provided.
   - If either field is missing, the system prompts the user with an error message: "Must provide username" or "Must provide password."
4. The system queries the database to retrieve the user's stored password hash based on the provided **username**.
5. The system compares the entered password with the stored hash.
   - If the credentials are correct, the system logs the user in and creates a session with the user’s **user_id**.
   - If the credentials are incorrect, the system prompts the user with an error message: "Invalid username and/or password."
6. Upon successful login, the user is redirected to the homepage (`/`), where they can manage their finances.

### **Handling Errors**
1. If the user fails to provide a **username** or **password**, the system displays an error message:
   - "Must provide username."
   - "Must provide password."
2. If the provided credentials do not match any user records, the system displays an error message: "Invalid username and/or password."

---

## **Alternative Flows**
### **01. Missing Username or Password**
1. The system checks if the **username** or **password** is missing.
2. If missing, the system displays the appropriate error message:
   - "Must provide username."
   - "Must provide password."
3. The user corrects the input and resubmits the form.

### **02. Invalid Username or Password**
1. The system verifies the entered **username** and **password** against the database.
2. If the credentials are incorrect, the system displays an error message: "Invalid username and/or password."
3. The user can attempt to log in again with the correct credentials.

---

## **Non-Functional Requirements**
- Login process must complete in less than **5 seconds**.
- All user passwords must be stored securely using **password hashing**.
- The system must ensure that session data is protected from unauthorized access.

---

## **Postconditions**
- If the login is successful, the user is granted access to the application and redirected to the homepage.
- If the login fails, the user is prompted with an appropriate error message and remains on the login page.

---

## **Business Rules**
BR01 - Each user must have a unique **username**.  
BR02 - Passwords must be hashed before storing in the database.  
BR03 - The **username** and **password** must be validated before proceeding with authentication.

---

## **Technical Notes**
- **Framework:** Uses **Flask** as the web framework and **Flask-Session** for session management.
- **Database:** User credentials are stored in the **SQLite** database (`users` table).
- **Authentication:** The system uses **Werkzeug**’s `check_password_hash` function to verify the password during login.
- **Session Management:** A session is created using **Flask-Session** to store the authenticated user's **user_id**.
