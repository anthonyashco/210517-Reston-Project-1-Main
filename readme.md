# Expensey

## Description

Expensey is a REST-ful service for managing your expense requests.

## Technologies Used

- Flask
- Vue
- Postgres

## Features

- Secure password hashing via pbkdf2-hmac-sha1 algorithm.
  - Plaintext passwords are never stored!
- Fully stateless server and permissions authentication via JWT tokens.
  - Users can't fake identity by guessing endpoint ids.
- Per-item employee and manager comment chains.
  - Archived storage for audits and oversight.
- Blob-based database storage of images.
- Intuitive single-screen application interface.

## Getting Started

- Database
  - Set up a postgres database locally or remotely.
  - Using the DB Management software of your choice, run the script `Server/sql/tables.sql` to set up the appropriate tables.
- Server
  - Install the Python requirements in `Server/requirements.txt`, preferably in a virtual environment.
    ```
    python3 -m pip install -r requirements.txt
    ```
  - Run the `main.py` script.
    ```
    python3 main.py
    ```

## Usage
