## Major Issues Identified

1. Monolithic Design: All logic (routing, DB, auth) was in app.py, making the codebase hard to maintain and  scale.
2. Security Risks: SQL queries used raw string formatting and passwords were stored without hashing.
3. Poor Error Handling: No input validation, incorrect HTTP response codes, and unclear messages.
4. Hardcoded Config: Database paths and secret keys were hardcoded, making it inflexible across environments.
5. Lack of Tests: No test cases existed to validate functionality.

## Changes Implemented

1. Project Structure Refactor
Created routes/, services/, models/, and config.py.
Blueprints used to organize routes for users and auth.

2. Security Improvements
All database operations now use parameterized queries to prevent SQL injection.
Passwords are now hashed using bcrypt and securely verified at login.

3. Input Validation & Status Codes
Email and password validation is done in the service layer.
API now returns proper HTTP status codes (e.g., 400, 404, 201, 204).

4. Environment Config Support
Added .env support with python-dotenv.
Config.py pulls in environment-specific database path and secret keys.

5. Testing Suite
Added pytest-based tests for core features: user creation, login, and fetching.
Used a temporary SQLite database for isolated test runs.

## Future Work 

- **Use PostgreSQL + ORM:** Replace raw SQLite with SQLAlchemy/PostgreSQL.
- **Add JWT Auth:** Token-based authentication and role management.
- **Dockerize the App:** For consistent local and production builds.
- **Add CI/CD:** GitHub Actions for automatic linting, testing, and deployment.
- **API Docs:** Add Swagger/OpenAPI for clear, interactive documentation.


## AI Usage Note

Used ChatGPT to:

1. Structure the refactor plan
2. Suggest secure coding practices
3. Draft some route logic and tests

## All changes were reviewed, validated, and customized before integration.

