# CustomerApp

This project is a demo of a basic application for storing customer data.

## Setup
Python Version: 3.9.18

### Virtual Environment
1. Set up a Python virtual environment: `python -m venv .venv`
1. Activate the virtual environment:
    - Bash: `source .venv/bin/activate`
    - Powershell: `.venv/Scripts/Activate.ps1`
1. Install Python packages: `pip install -r requirements.txt`

### Setup Django
The Django database needs to be initialized. It is using Sqlite3 by default, but the database file is excluded from the repository. To set it up, run:

```
python manage.py makemigrations customers
python manage.py migrate
```

Once this is complete, you can run the server.

### VS Code
I use Visual Studio Code as my primary IDE.

These are my main Python extensions:
* Python
* Pylance
* Pylint
* Python Debugger
* Black Formatter (Controversial, other formatters are available)

Be sure to add this pylint configuration to your settings JSON file:
```
"pylint.args": [
        "--load-plugins=pylint_django"
    ]
```

## Running the App
From the `customerapp` directory, run: `python manage.py runserver`

If using VS Code over SSH and using the builtin terminal, this will automatically forward a port and prompt you to open the browser.

The "Add Customer" page should work with auto-populated addresses common in modern web browsers. At minimum, it works with Google Chrome.

### Unit Tests
To run the unit tests and generate a coverage report, run the following from the `customerapp` directory:
```
coverage run --source='.' manage.py test
coverage html
```

I recommend using the "Live Preview" VS Code extension from Microsoft to view the coverage report.

## Future Work
### Adding Features
By making heavy use of Django's tools, I minimize the amount of work required to add new features. For instance, I use Django's `TemplateViews` to make the app's views as simple as possible, and using Django's `Forms` helps minimize the amount of HTML I need to write.

There is still room for code reuse. Both apps use the same header, while in a production application you would expect a common header and footer to be used accross all pages. I did not set it up here because the header I chose requires a bit of Javascript to highlight the current page, but this would be a common script that can be reused between pages.

### Code Quality
To ensure consistency, I'm using the Black formatter. This formatter is very aggressive, so it takes minimal effort on my part to format the code. I also use pylint to ensure the code follows the PEP8 style guide.

### Testing
Using the `coverage` package to measure code coverage makes it very easy to determine which parts of the code still need to be tested. For simple behaviors, simply testing coverage is fine, but any external API or user interface should be tested more thoroughly since they can generate unexpected results in production.
