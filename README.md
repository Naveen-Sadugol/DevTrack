**DevTrack API**

A minimal backend API for tracking engineering issues, inspired by GitHub Issues.



**Features**

* Create and fetch Reporters
* Create and fetch Issues
* Filter issues by status
* OOP-based design using inheritance and validation
* JSON file storage (no database)

---

**Tech Stack**

* Python
* Django
* JSON (file-based storage)

---

**Project Setup**

1. Clone the repo

bash
git clone <your-repo-link>
cd devtrack

2. Create virtual environment

bash
python -m venv .venv
.venv\Scripts\activate   # Windows


3. Install dependencies

```bash
pip install django
```

4. Run server

```bash
python manage.py runserver
```

---

**API Endpoints**

Reporter APIs

Create Reporter

POST `/api/reporters/`

Get All Reporters

GET `/api/reporters/`

**Get Reporter by ID**

GET `/api/reporters/?id=1`

---

 Issue APIs

**Create Issue**

POST `/api/issues/`

**Get All Issues**

GET `/api/issues/`

**Get Issue by ID**

GET `/api/issues/?id=1`

**Filter by Status**

GET `/api/issues/?status=open`

---

**Sample Success Response**

```json
{
"id": 1,
"title": "Login issue",
"description": "Button not working",
"status": "open",
"priority": "critical",
"reporter_id": 1,
"message": "[URGENT] Login issue — needs immediate attention"
}
```

---

**Sample Error Response**

```json
{
"error": "Title cannot be empty"
}
```

---

**Design Decision**

I used an abstract base class `BaseEntity` to enforce a `validate()` method across all models. This ensures that both Reporter and Issue implement validation logic consistently.

Additionally, I used inheritance in Issue (`CriticalIssue`, `LowPriorityIssue`) to demonstrate polymorphism through method overriding (`describe()`), making the system extensible for future priority types.

---

**Postman Testing**

Included screenshots of:

**Successful POST request**

<img width="1182" height="620" alt="image" src="https://github.com/user-attachments/assets/8858c7d4-4c0a-42a2-8027-94c11f4ac21b" />

**Failed validation request**

<img width="1485" height="611" alt="image" src="https://github.com/user-attachments/assets/e89df1c0-15b5-49ea-9dc8-99a5867b9d95" />


**Data Storage**

`reporters.json`
`issues.json`



**Author**

Naveen P Sadugol
