# SQL Comment Injection Demonstration with Flask

This project demonstrates a vulnerability in a Flask web application that allows users to bypass authentication using SQL injection via comments (--). The goal is to showcase how attackers can exploit improperly sanitized user inputs to gain unauthorized access.

## Features
- SQL Injection Vulnerability: A Flask app that allows users to authenticate using a vulnerable login form, making it susceptible to SQL injection attacks.

- Bypass Authentication: Demonstrates how an attacker can log in as an administrator without knowing the password by injecting SQL code.

- No Authentication Protection: There are no security mechanisms to prevent SQL injection attacks, making it an ideal demonstration of the risk.

## Prerequisites

- Docker: Install Docker on your machine.

- Python: Ensure you have Python 3.8 or higher if you plan to run the app outside of Docker.

## Installation

Clone the repository:
```bash
git clone https://github.com/yourusername/SQL_Comment_Injection.git
cd SQL_Comment_Injection
```
Build and run the Docker container:
```bash
docker build -t sql_comment_demo .
docker run -p 8080:8080 sql_comment_demo
```
The application will now be running and accessible at http://127.0.0.1:8080.

## Usage

1. Access the Application
Open your browser and navigate to the following URL:
```bash
http://127.0.0.1:8080
```
2. Test the Vulnerability
You can now attempt to log in using SQL injection. Below is an example of how you can bypass authentication using an SQL comment attack.

Example: SQL Injection Login Bypass
Use the following credentials in the login form:

Username: admin' --

Password: (Leave blank)

This input exploits the SQL query by injecting a comment (--), effectively bypassing the password check and logging in as the admin user.

3. Observe the Results

Once logged in, you should have access to the admin panel or other protected areas of the application, demonstrating the risk of SQL injection.

## Observing the Results

If the attack is successful: You will gain admin access without entering a correct password, demonstrating the vulnerability.

If the attack fails: The application may have some level of security, such as input sanitization or prepared statements.

## Risks and Mitigations

- This type of vulnerability is common in applications that fail to properly sanitize user inputs.

- Potential risks include:

  - Data Breach: Attackers can extract sensitive information from the database.

  - Privilege Escalation: Malicious users can gain unauthorized admin access.

  - Data Manipulation: Attackers may alter or delete records in the database.

  - Denial of Service: SQL injections can overload the database, causing application crashes.

## How to Fix the Vulnerability

- Use Prepared Statements: Always use parameterized queries to separate SQL code from user input.

- Validate User Input: Restrict input fields to expected formats.

- Implement ORM Solutions: Using an ORM like SQLAlchemy can help prevent raw SQL injections.

- Enable Logging and Monitoring: Detect and alert on unusual login attempts or SQL query patterns.
