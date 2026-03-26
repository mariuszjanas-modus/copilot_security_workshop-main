# Secure Coding: GitHub Copilot Developer Training

_Pre-requisite: Before starting the training, please make sure you have the necessary environment setup as mentioned in [SETUP.md](../setup/SETUP.md)._

## Introduction

The following training is delivered live alongside a set of accompanying slides. However, this training can also be performed in a non-live setting, by following the instructions in this file, or by watching a recording of the live training session.

The Copilot Securirty Vulneration and Remediation training touches on some basic topics

1. [Secure Coding](#module-1---secure-coding)
2. [Autofix](#module-2---autofix-optional)

We recommend you read the SETUP.md file prior to starting the course to familiarize yourself with the packages and tools used in these workshops.

## Module 1 - Secure Coding

### Objective

This module emphasizes secure coding practices with Copilot's assistance. By the end of this module, participants will be able to:

1. Identify and fix vulnerabilities such as SQL injection, Cross-Site Scripting (XSS), Insecure Authentication (Hardcoded Credentials), Sensitive Data Exposure (Logging & Debug Mode), Insecure File Handling (Path Traversal), and improper CORS configurations.
2. Utilize Copilot to generate secure code and recommendations for improvement.

### Secure Coding

We are now going to wrap up with some examples of how Copilot can assist you in securing your code.

1. Copilot has to ability to detect vulnerable code. Copy and paste the following function into your `cSecureCoding/src/appSecureCoding.py` file:

```python
def get_db_connection():
    conn = sqlite3.connect('example.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/secure_coding/insecure_sql')
def insecure_sql():
    username = request.args.get('query')
    conn = get_db_connection()
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    result = cursor.execute(query).fetchall()
    conn.close()
    users = [dict(row) for row in results]
    return jsonify(users)

@app.route('/secure_coding/insecure_xss')
def insecure_xss():
    user_input = request.args.get("input", "")
    return f"<h1>Hello, {user_input}</h1>"

@app.route('/secure_coding/hardcoded_login')
def hardcoded_login():
    username = request.args.get("username")
    password = request.args.get("password")
    
    if username == "admin" and password == "password123":
        return "Login Successful"
    return "Invalid credentials", 401

@app.route('/secure_coding/log_password')
def log_password():
    password = request.args.get("password")
    print(f"User entered password: {password}")
    return "Check server logs!"

@app.route('/secure_coding/read_file')
def read_file():
    filename = request.args.get("filename")
    with open(f"/var/www/data/{filename}", "r") as file:
        return file.read()
```

The search route contain a SQL injection vulnerability, let's see if Copilot detects this.

2. In the Copilot chat window, ask the following question:

```console
What vulnerabilities exist in `appSecureCoding.py`
```

Copilot will respond with a list of issues it has detected, for example:

> The appSecureCoding.py file has a couple of potential vulnerabilities:
>
> SQL Injection: In the search function, the query parameter is directly used in the SQL query without any sanitization or parameterization. This opens up the possibility for SQL injection attacks.
>
> Cross-Origin Resource Sharing (CORS): The Access-Control-Allow-Origin header is set to \* in the dummy_data function. This means that any website can make a request to this endpoint, which could potentially lead to security issues.
>
> Database Connection Handling: The get_db_connection function opens a connection to the database but there's no explicit handling of connection closure in case of errors. This could potentially lead to resource leaks.
>
> Hardcoded Database Name: The database name 'example.db' is hardcoded in the get_db_connection function. This could be a problem if you want to change the database or use different databases for different environments.
>
> No Input Validation: There's no validation of the input query in the search function. This could lead to unexpected behavior or errors.
>
> No Error Handling: There's no explicit error handling in the code. If any error occurs (like database connection failure, SQL execution failure, etc.), the application might crash or behave unexpectedly.
>
> Cross-Site Scripting (XSS): The insecure_xss function renders user input directly in an HTML response, making it vulnerable to script injection attacks.
>
> Hardcoded Credentials: The hardcoded_login function has hardcoded admin credentials, making them easy for attackers to exploit.
>
> Sensitive Data Exposure: The log_password function prints user passwords to logs, which can be a security risk if logs are accessible.
>
> Path Traversal: The read_file function allows users to request arbitrary files, potentially exposing sensitive system files.

Notice how Copilot detected that we had set the `Access-Control-Allow-Origin` to `*` earlier! Copilot has also found the issue we added with the SQL injection vulnerability.

So how can we fix this? Let's ask Copilot chat. Add in the next prompt:

```console
How do I fix the SQL injection vulnerability?
```

Copilot will respond now with a recommendation to refactor the code:

> To fix the SQL injection vulnerability, you should use parameterized queries instead of string formatting. Here's how you can do it:

```python
sql_query = "SELECT * FROM users WHERE name LIKE ?"
params = ('%' + query + '%',)
```

> In this way, the query variable is not directly included in the SQL query string. Instead, it's passed as a parameter to the SQL execution function, which properly escapes it and prevents SQL injection attacks.

3. Select the lines with the SQL injection issue:

```python
sql_query = f"SELECT * FROM users WHERE name LIKE '%{query}%'"
cursor.execute(sql_query)
```

Right click and open the Copilot inline chat window. Next enter the following prompt:

```console
Fix this SQL injection vulnerability
```

Copilot will now apply a fix similar to what was described in the Copilot chat window. For example:

```python
sql_query = "SELECT * FROM users WHERE name LIKE ?"
cursor.execute(sql_query, ('%' + query + '%',))
```

As you can see Copilot is a powerful tool to detect security issues directly during development. When combined with the other security tools provided by GitHub such as GHAS you can help to reduce the overall attack surface of your application.

## Module 2 - Autofix (Optional)

### Objective

This module introduces GitHub's Autofix feature for resolving code vulnerabilities. By the end of this module, participants will be able to:

1. Understand how CodeQL detects vulnerabilities.
2. Use Autofix to apply AI-generated fixes to security issues in the codebase.

### Autofix

Before we wrap up, let's take a look at one of GitHub's newest features - Autofix.
Autofix combines the power of GHAS and OpenAI to detect security issues and recommend fixes, which are turned into pull requests.

### CodeQL and Autofix

This module demonstrates how GitHub Advanced Security (GHAS) helps identify and fix security vulnerabilities in your code. We'll focus on exploring existing security findings and Autofix suggestions.

#### Prerequisites

- In order to complete this part of the workshop your company must have GHAS licenses and you should have the ability to switch on CodeQL and Autofix on your repository.
- Access to the copilot-training repository

#### Exploring Security Features

1. Open the copilot-training repository in your browser
2. Click the "Security" tab in the top navigation
3. Observe two key security features:
   - Code scanning alerts (powered by CodeQL)
   - Dependabot alerts (for dependency vulnerabilities)

#### Exploring CodeQL Findings

1. In the Security tab, click "Code scanning alerts"
2. You should see two alerts about Flask running in debug mode:
   - One in `app101.py`
   - One in `appSecureCoding.py`
     These alerts were generated because both files contain:
   ```python
   app.run(debug=True)
   ```

#### Exploring Autofix Suggestions

1. Click the alert for app101.py
2. Notice the "Generate fix" button but DO NOT click it yet
   - This represents the "before" state of an Autofix suggestion
3. Return to Code scanning alerts and click the alert for appSecureCoding.py
4. Here you'll see a complete Autofix suggestion containing:
   - A detailed explanation of the security risk
   - The proposed solution using environment variables
   - Specific code changes:
   ```python
   # Before
    app.run(debug=True)
    # After
    app.run(debug=os.getenv('FLASK_DEBUG') == '1')
   ```

#### Understanding the Fix

- The Autofix suggestion makes the debug mode configurable through an environment variable
- This prevents accidental deployment with debug mode enabled
- The fix includes proper imports and clear implementation steps
- You can choose to accept the suggestion provided by Autofix, edit in Codespaces, fix locally and push the change, or dismiss the finding.

#### Key Takeaways

1. CodeQL automatically identifies security vulnerabilities
2. Autofix provides AI-generated fix suggestions
3. Each suggestion includes:

- Problem description
- Security impact
- Ready-to-implement solution

---

## 💡 _The following section contains optional self-paced exercises you can try independently_

#### Try It Yourself (Self-Paced Exercise)

Want to see CodeQL and Autofix in action with your own code? Follow these steps:

1. **Create a Security Vulnerability**
   - Create a new branch from main
   - Add this simple Flask route with a SQL injection vulnerability:
   ```python
   @app.route('/user/<username>')
   def get_user(username):
       # DO NOT USE IN PRODUCTION - SQL Injection vulnerability!
       query = f"SELECT * FROM users WHERE username = '{username}'"
       cursor.execute(query)
       return cursor.fetchone()
   ```
2. **Create Pull Request**
   - Commit your changes and push to your branch
   - Create a pull request to main
   - Title it "feat: add user lookup route"
3. **Watch CodeQL Work**

   - Wait 1-2 minutes for CodeQL scan to complete
   - Check the "Security" tab in your PR
   - You should see a new security alert for SQL injection
   - Observe Autofix's suggested solution

4. **Review the Fix**
   - Autofix will suggest using parameterized queries
   - The suggestion will look similar to:
   ```python
   @app.route('/user/<username>')
    def get_user(username):
        query = "SELECT * FROM users WHERE username = ?"
        cursor.execute(query, (username,))
        return cursor.fetchone()
   ```
5. **Apply the Fix**
   - You can either: - Accept Autofix's suggestion directly - Create a new commit with the fixed code -
     Note: Remember to remove this test code after completing the exercise! Never deploy vulnerable code to production.

That completes our Autofix example.

### Wrap up

This completes the hands-on section of this workshop. You've successfully tried a number of Copilot features including writing tests, documentation and adding new features.
