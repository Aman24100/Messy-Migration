## Major Issues Identified

- **Monolithic Design**  
  All logic (routing, DB, authentication) was placed inside `app.py`, making the codebase difficult to maintain and scale.

- **Security Risks**  
  SQL queries used raw string formatting (vulnerable to injection), and passwords were stored without hashing.

- **Poor Error Handling**  
  There was no input validation, incorrect HTTP status codes were returned, and error messages lacked clarity.

- **Hardcoded Configuration**  
  Database paths and secret keys were hardcoded, preventing environment-specific setups and secure deployment.

- **Lack of Testing**  
  No automated test cases were available to validate functionality or catch regressions.

## Changes Implemented

- **Project Structure Refactor**  
  Created `routes/`, `services/`, `models/`, and `config.py`.  
  Used Blueprints to organize routes for `users` and `auth`.

- **Security Improvements**  
  All database operations now use parameterized queries to prevent SQL injection.  
  Passwords are hashed using `bcrypt` and securely verified during login.

- **Input Validation & Status Codes**  
  Added email and password format validation in the service layer.  
  API now responds with appropriate HTTP status codes like 400, 404, 201, and 204.

- **Environment Config Support**  
  Integrated `.env` support via `python-dotenv`.  
  `config.py` now loads environment-specific DB path and secrets securely.

- **Testing Suite**  
  Implemented `pytest` tests for core functionalities: user creation, login, and retrieval.  
  Used a temporary SQLite database to keep tests isolated and clean.

## Future Work(With more time) 

- **Use PostgreSQL + ORM:** Replace raw SQLite with SQLAlchemy/PostgreSQL.
- **Add JWT Auth:** Token-based authentication and role management.
- **Dockerize the App:** For consistent local and production builds.
- **Add CI/CD:** GitHub Actions for automatic linting, testing, and deployment.
- **API Docs:** Add Swagger/OpenAPI for clear, interactive documentation.


## AI Usage Note

AI tool was used to brainstorm structural ideas and best practices for modularizing the project. All code was manually written, reviewed, and tested to ensure alignment with the assignment goals and coding standards.


## All changes were reviewed, validated, and customized before integration.

