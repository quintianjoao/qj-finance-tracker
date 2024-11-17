# Project Roadmap

## Vision

The **Personal Finance Tracker** aims to provide an intuitive and feature-rich solution for users to seamlessly manage their financial data. This web application will empower users to track incomes and expenses, monitor financial health, and gain insights through robust filtering and reporting tools. Our vision includes delivering a responsive, secure, and user-friendly platform that evolves based on user feedback.

---

## Roadmap Overview

This roadmap outlines the development plan across a series of one-month sprints. Each sprint focuses on a defined scope of features, aligning with Agile best practices. The roadmap emphasizes incremental delivery, enabling early user feedback and prioritizing value-driven development.  

### Key Milestones:
- **Beta Release:** Post-Sprint 6 (18/05)
- **General Public Release:** Post-Sprint 7 (18/06)

Each sprint is capped at **10 story points**, ensuring a sustainable pace for quality delivery. Regular sprint reviews and retrospectives will guide adjustments to align with project goals and user needs.

---

## Sprints

### Sprint 1 (18/11 - 17/12)

**Goal:** Add email functionality for user registration and login, ensuring a secure and verified user base.  

**Story Points:** Maximum of 10.

**Key Features:**
- User registration with email.
- Email validation process.
- Login restricted to verified emails.

**Tasks:**
1. Modify the `register` route to trigger a validation email upon user registration.
2. Update the `login` route to enforce email validation before access.
3. Integrate an email service API (e.g., SendGrid, Mailgun).
4. Set up environment variables for secure email service integration.

---

### Sprint 2 (18/12 - 17/01)

**Goal:** Enable users to edit financial records and enhance data interaction with filters.  

**Story Points:** Maximum of 10.

**Key Features:**
- Edit incomes and expenses.
- Add filters to incomes, expenses, and overview tables.

**Tasks:**
1. Create a form for editing income and expense records.
2. Implement routes for handling edits securely.
3. Add filters for searching and sorting in data tables (by date, tag, value, etc.).
4. Ensure edits and filters respect user data privacy.

---

### Sprint 3 (18/01 - 17/02)

**Goal:** Improve usability by implementing pagination for financial data tables.  

**Story Points:** Maximum of 10.

**Key Features:**
- Pagination for overview, income, and expense tables.

**Tasks:**
1. Implement pagination for all large data tables.
2. Add an option for configurable rows per page.
3. Test performance and responsiveness of paginated tables.

---

### Sprint 4 (18/02 - 17/03)

**Goal:** Introduce custom categories and tagging for better data organization.  

**Story Points:** Maximum of 10.

**Key Features:**
- Custom income/expense categories.
- Tagging system for transactions.

**Tasks:**
1. Add a "Manage Categories" feature in user settings.
2. Enable users to add, edit, or delete categories.
3. Implement a tagging system in transaction forms.
4. Update filters and reports to include categories and tags.

---

### Sprint 5 (18/03 - 17/04)

**Goal:** Automate recurring transactions to reduce manual entries for repetitive expenses and incomes.  

**Story Points:** Maximum of 10.

**Key Features:**
- Support for recurring transactions.

**Tasks:**
1. Add a "Recurring" toggle with frequency options (e.g., monthly, weekly).
2. Implement backend logic to handle recurring entries.
3. Create a dashboard widget to manage recurring transactions.
4. Notify users of upcoming recurring transactions via email or in-app alerts.

---

### Sprint 6 (18/04 - 17/05)

**Goal:** Implement configurable email notifications for user actions and bill due reminders.  

**Story Points:** Maximum of 10.

**Key Features:**
- Email alerts for incomes and expenses.
- Notifications for upcoming bill due dates.
- User-configurable notification settings.

**Tasks:**
1. Add notification preferences in user settings.
2. Implement backend logic for sending notifications upon transactions.
3. Schedule background tasks to send bill reminders.
4. Secure email templates and ensure compliance with user settings.
5. Test notification delivery and system reliability.

---

### Beta Release (18/05)

**Milestone:** Following the completion of Sprint 6, the **Beta Release** will be launched to gather user feedback on core features.  

**Key Features:**
- Secure user registration and login.
- Editing and filtering financial records.
- Pagination for large datasets.
- Custom categories and tagging.
- Recurring transactions.
- Configurable email notifications.

---

### Sprint 7 (18/05 - 17/06)

**Goal:** Introduce gamification elements to encourage user engagement and achievement tracking.  

**Story Points:** Maximum of 10.

**Key Features:**
- Gamification with badges and milestones.

**Tasks:**
1. Design a badge system with achievements (e.g., "First Budget Created").
2. Add a dashboard widget to display badges and milestones.
3. Implement backend logic to calculate and assign achievements.
4. Notify users when new achievements are unlocked.

---

### General Public Release (18/06)

**Milestone:** After Sprint 7, the **General Public Release** will deliver a polished and feature-complete application.  

**Key Features:**
- Core and advanced financial tracking tools.
- Engaging user experience with gamification.
- Comprehensive reporting and organizational features.
- Responsive, secure, and user-friendly design.

---

## Development Principles

1. **Agile Framework:** Each sprint begins with planning and concludes with a review and retrospective.
2. **User-Centered Design:** Features are developed based on user feedback and evolving needs.
3. **Incremental Delivery:** Functional increments are delivered regularly to ensure progress and adaptability.
4. **Quality Focus:** Testing and validation are prioritized at every sprint to maintain reliability and performance.

---

## Conclusion

This roadmap represents the planned trajectory for the **Personal Finance Tracker** project. By following an Agile approach, the project will deliver a robust, user-focused solution while remaining flexible to adapt based on user insights and challenges encountered during development.
