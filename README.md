# CLI Password Generator

A Command-Line Interface (CLI) based Password Generator built using Python that generates secure random passwords with customizable length, character selection, password strength checking, input validation, and clipboard support.

##  Features

* Generate secure random passwords
* Custom password length
* Include:

  * Uppercase letters
  * Lowercase letters
  * Numbers
  * Symbols
* Password strength checker
* Input validation
* Clipboard copy support
* Exclude specific characters

##  Technologies Used

* Python
* Random module
* String module
* Pyperclip

##  Project Structure

```txt
Password_Generator/
│── password_generator_cli.py
│── requirements.txt
│── README.md
```

##  Installation

Clone the repository:

```bash
git clone https://github.com/vishnu-charitha/Password_generator.git
```

Move into project folder:

```bash
cd Password_generator
```

Install dependencies:

```bash
pip install -r requirements.txt
```

##  Run the Project

```bash
python password_generator_cli.py
```

## 📸 Example Output

```txt
Enter password length: 12
Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include numbers? (y/n): y
Include symbols? (y/n): y

Generated Password:
A#7kLm!92QwP

Password Strength: Strong 🟢
```

## 👨‍💻 Author

Vishnu Charitha
