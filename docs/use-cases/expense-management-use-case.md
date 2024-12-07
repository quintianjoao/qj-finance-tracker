# Use Case: Expense Management

## **Change Log**
| Date       | Change Description                | Version | Author              |
|------------|-----------------------------------|---------|---------------------|
| 16/11/2024 | Created initial use case document | 1.0     | João Vitor Quintian |
| 07/12/2024 | Revised with additional details   | 1.1     | João Vitor Quintian |

---

## **Description**
This use case outlines the CRUD operations for managing expenses in the application. Users can add, view, and remove expense records. The system ensures data integrity by validating inputs and securely storing financial records in the database. The goal is to provide users with an intuitive interface for managing their financial expenses efficiently while adhering to performance and security standards.

---

## **Primary Actor(s)**
- **User**: An individual managing their financial expenses using the system.

---

## **Stakeholders and Interests**
- **User**: Needs a reliable, efficient tool to record and delete expense entries while receiving immediate feedback on actions.
- **Business Owner**: Interested in ensuring high user satisfaction through seamless functionality and intuitive design.
- **Administrators**: Require expense data accuracy for analytics or support purposes.

---

## **Preconditions**
- The user is logged into the system.
- The system has an active connection to the database and is fully operational.
- All required user roles and permissions are appropriately configured.

---

## **Main Flow**
### **Viewing Expenses**
1. The user navigates to the "Expenses" section.
2. The system queries the database for the user's expense records, filtering by `user_id`.
3. The system displays a list of expense entries with the following details:
   - **Type:** Always "Expense".
   - **Name:** Descriptive label for the expense.
   - **Tag:** Categorization label for the expense.
   - **Value:** Monetary amount in dollars.
   - **Date:** Date of the expense.
   - **Notes:** Additional user-provided details.
4. The system calculates and displays the total expenses in dollars.

### **Adding Expense**
1. The user selects the "Add Expense" option.
2. The system presents a form with the following fields:
   - **Expense Name** (Required)
   - **Tag** (Required)
   - **Value** (Required)
   - **Date** (Required)
   - **Notes** (Optional)
3. The user fills out the form and submits it.
4. The system performs input validation (see Business Rules).
   - If valid:
     - The system saves the new expense to the database.
     - The user receives a success message: "Expense [Name] added successfully."
   - If invalid:
     - The system shows an error message (see Alternative Flow 01).
5. The user is redirected to the "Expenses" section, where the new entry is displayed.

### **Removing Expense**
1. The user selects the "Remove Expense" option.
2. The system displays a list of the user's recorded expense entries.
3. The user selects an expense entry to remove.
4. The system presents a confirmation modal with a message:
   - "Are you sure you want to delete [Expense Name]?"
5. If the user confirms, the system removes the record from the database and displays a success message: "Expense [Name] removed successfully."

---

## **Alternative Flows**
### **01. Invalid Input for Adding Expense**
1. The system validates the input fields:
   - **Expense Name**, **Tag**, and **Date** must not be empty (BR01, BR03).
   - **Value** must be a positive number (BR02).
2. If validation fails, the system displays an error message:
   - "Must Provide Name", "Must Provide Tag", "Must Provide Date", or "Value must be a positive number."
3. The user corrects the inputs and resubmits the form.

### **02. Database Connection Failure**
1. If the database connection fails during any CRUD operation, the system displays an error message:
   - "Unable to process your request. Please try again later."
2. The system logs the error for further investigation.

---

## **Non-Functional Requirements**
- CRUD operations must execute in less than **5 seconds**.
- User interfaces must remain responsive and intuitive.
- All financial data must be securely stored in the database and encrypted where applicable.
- The system must be accessible on major browsers (Chrome, Firefox, Edge, Safari).

---

## **Postconditions**
- Expense records are accurately stored, displayed, or removed in/from the database.
- Users are provided with clear feedback on their actions.

---

## **Business Rules**
- **BR01**: Each expense record must be associated with a valid **user_id**.
- **BR02**: **Value** must be a positive number.
- **BR03**: The **Name** and **Date** fields cannot be empty.
- **BR04**: Tags must belong to a predefined set of allowed categories (e.g., Food, Rent, Utilities).

---

## **Assumptions**
- The user has a stable internet connection.
- The user interacts with the system through a modern, JavaScript-enabled browser.

---

## **System Assumptions**
- Database is operational and accessible.
- Flask session management ensures secure and reliable user authentication.

---

## **Usability Considerations**
- Use of modals for confirmation actions ensures no accidental deletions.
- Forms include placeholder text and tooltips for clarity.
- Error messages are contextual, guiding users to correct inputs.

---

## **Technical Notes**
- **Framework**: Uses **Flask** as the web framework and **Flask-WTF** for form handling.
- **Database**: Expense records are stored in the **SQLite** database (`finances` table).
- **Currency Format**: All monetary values are formatted using the custom `usd` filter.
- **Authentication**: All CRUD operations require the user to be logged in.
