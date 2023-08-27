# Anom Password Manager

Welcome to the Anom Password Manager GitHub project!

## Requirements:

- Ensure you have a MySQL server installed on your system.
- Update the "user" and "password" settings for your MySQL server in `dbconfig.py` (line 10 and 11 respectively).

## Python Modules (Install these modules by running the program):

- Maskpass module: Install with `pip install maskpass`.
- Rich module: Install with `python -m pip install rich`.
- Cryptography module: Install with `pip install cryptography`.
- MySQL connector: Install with `python -m pip install MySQL-connector-python`.

## File System:

- `main.py`: Main program.
- `login.py`: Manages user logins.
- `passgen.py`: Generates passwords.
- `dbconfig.py`: Manages database connections.
- `pipconfig.py`: Installs required Python modules.
- `cryptoGraphy.py`: Handles encryption and decryption.

## Common Issues:

- If you no longer need a database, you can log in and delete all stored passwords.

