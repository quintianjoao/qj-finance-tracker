# Use Case: Income Management 

## **Change Log**
| Date       | Change Description               | Version | Author              |
|------------|----------------------------------|---------|---------------------|
| 16/11/2024 | Created initial use case document| 1.0     | João Vitor Quintian |

## **Description**
This use case describes the CRUD operations for managing income in the application. Users can add, view, and remove income records. The system validates user inputs, ensures data integrity, and provides a seamless experience for managing financial records.

---

## **Primary Actor(s)**
- **User:** An individual managing their financial income using the system.

## **Stakeholders and Interests**
- **User:** Wants to record and delete income entries efficiently.

---

## **Preconditions**
- The user is logged into the system.
- The system is connected to the database and operational.

---

## **Main Flow**
### **Viewing Income**
1. The user navigates to the "Income" section.
2. The system queries the database for the user's income records.
3. The system displays a list of income entries, including:
   - **Type:** Always "Income".
   - **Name:** Descriptive label for the income.
   - **Tag:** Categorization label for the income.
   - **Value:** Monetary amount.
   - **Date:** Date of the income.
   - **Notes:** Additional details.
4. The system calculates and displays the total income in dollars.

### **Adding Income**
1. The user selects the "Add Income" option.
2. The system presents a form with the following fields:
   - **Income Name** (Required)
   - **Tag** (Required)
   - **Value** (Required)
   - **Date** (Required)
   - **Notes** (Optional)
3. The user fills out the form and submits it.
4. The system validates the inputs:
   - If valid, the system saves the new income to the database and displays a success message.
   - If invalid, the system shows an appropriate error message (see Alternative Flow 01).

### **Removing Income**
1. The user selects the "Remove Income" option.
2. The system displays a list of the user's recorded income entries.
3. The user selects an income entry to remove.
4. The system confirms the deletion and removes the record from the database.

---

## **Alternative Flows**
### **01. Invalid Input for Adding Income**
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
- Income records are accurately stored, displayed, or removed in/from the database.

---

## **Business Rules**
BR01 - Each income record must be associated with a valid **user_id**.  
BR02 - **Value** must be a positive number.  
BR03 - The **Name** and **Date** fields cannot be empty.  

---

## **Technical Notes**
- **Framework:** Uses **Flask** as the web framework and **Flask-WTF** for form handling.
- **Database:** Income records are stored in the **SQLite** database (`finances` table).
- **Currency Format:** All monetary values are formatted using the custom `usd` filter.
- **Authentication:** All CRUD operations require the user to be logged in.
