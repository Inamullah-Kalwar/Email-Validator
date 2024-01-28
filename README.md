# Email Validator

## Description

This Python script uses Selenium to validate a list of email addresses by attempting to log in to Microsoft accounts. It checks the validity of each email and highlights the results in both the console and a CSV file.

## Features

- Validates email addresses using Microsoft login.
- Highlights valid and invalid emails.
- Prints real-time results in the console.
- Saves results in a CSV file with color-coded formatting.

## Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Inamullah-Kalwar/Email-Validator.git
   cd Email-Validator
   ```

2. **Install Dependencies:**
   ```bash
   pip install selenium pandas termcolor
   ```

3. **Run the Script:**
   ```bash
   python email_validator.py
   ```

4. **Results:**
   - Real-time validation results will be displayed in the console.
   - The updated CSV file, "highlighted_emails.csv," will contain color-coded email statuses.

## Usage

- Add your list of emails to "emails.csv" (one per line).
- Customize the script if needed, e.g., specifying the path to your ChromeDriver executable.
- Run the script and observe real-time email validation results.

## Contributors

- [Inamullah Kalwar](https://github.com/Inamullah-Kalwar)

## License

This project is licensed under the [MIT License](LICENSE).
