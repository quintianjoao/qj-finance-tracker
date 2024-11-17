# Use Case: Expense Management

## **Change Log**
| Date       | Change Description               | Version | Author              |
|------------|----------------------------------|---------|---------------------|
| 16/11/2024 | Created initial use case document| 1.0     | João Vitor Quintian |

## **Description**
This use case describes the CRUD operations for managing expenses in the application. Users can add, view, and remove expense records. The system validates user inputs, ensures data integrity, and provides a seamless experience for managing financial records.

---

## **Primary Actor(s)**
- **User:** An individual managing their financial expenses using the system.

## **Stakeholders and Interests**
- **User:** Wants to record and delete expense entries efficiently.

---

## **Preconditions**
- The user is logged into the system.
- The system is connected to the database and operational.

---

## **Main Flow**
### **Viewing Expenses**
1. The user navigates to the "Expenses" section.
2. The system queries the database for the user's expense records.
3. The system displays a list of expense entries, including:
   - **Type:** Always "Expense".
   - **Name:** Descriptive label for the expense.
   - **Tag:** Categorization label for the expense.
   - **Value:** Monetary amount.
   - **Date:** Date of the expense.
   - **Notes:** Additional details.
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
4. The system validates the inputs:
   - If valid, the system saves the new expense to the database and displays a success message.
   - If invalid, the system shows an appropriate error message (see Alternative Flow 01).

### **Removing Expense**
1. The user selects the "Remove Expense" option.
2. The system displays a list of the user's recorded expense entries.
3. The user selects an expense entry to remove.
4. The system confirms the deletion and removes the record from the database.

---

## **Alternative Flows**
### **01. Invalid Input for Adding Expense**
1. The system checks the input fields (BR01, BR02, BR03):
   - **Name**, **Tag**, or **Date** is missing.
2. The system displays an error message: 
   - "Must Provide Name", "Must Provide Tag", or "Must Provide Date."
3. The user corrects the inputs and resubmits the form.

---

## **Non-Functional Requirements**
- CRUD operations must execute in less than **5 seconds**.
- All financial data must be securely stored in the database.

---

## **Postconditions**
- Expense records are accurately stored, displayed, or removed in/from the database.

---

## **Business Rules**
BR01 - Each expense record must be associated with a valid **user_id**.  
BR02 - **Value** must be a positive number.  
BR03 - The **Name** and **Date** fields cannot be empty.  

---

## **Technical Notes**
- **Framework:** Uses **Flask** as the web framework and **Flask-WTF** for form handling.
- **Database:** Expense records are stored in the **SQLite** database (`finances` table).
- **Currency Format:** All monetary values are formatted using the custom `usd` filter.
- **Authentication:** All CRUD operations require the user to be logged in.
