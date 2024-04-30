from prettytable import from_db_cursor
import sys
import sqlite3


class ContactsRepo:
    def __init__(self, db):
        self.db = db

    def add(self, first_name, last_name, phone_number):
        cursor = self.db.cursor()
        cursor.execute(
            """
            INSERT INTO contacts (first_name, last_name, phone_number)
            VALUES (?,?,?)
            """,
            (first_name, last_name, phone_number)
        )

    def list(self):
        cursor = self.db.cursor()
        cursor.execute("""
        SELECT * FROM contacts
        """)

        return from_db_cursor(cursor)

    def search(self, first_name):
        cursor = self.db.cursor()
        cursor.execute(
            """
            SELECT * FROM contacts WHERE first_name = ?
            """,
            (first_name,)
        )

        return from_db_cursor(cursor)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("only 1 argument is required")

    available_commands = ["add", "list", "search"]
    command = sys.argv[1]

    if command not in available_commands:
        sys.exit(f"invalid command: {command}, available commands: {available_commands} ")

    with sqlite3.connect("contacts.db") as db:
        repo = ContactsRepo(db)
        if command == "add":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            phone_number = input("Enter phone number: ")
            repo.add(first_name, last_name, phone_number)
            print("Added contact successfully")
        elif command == "list":
            contacts = repo.list()

            print(contacts)
        elif command == "search":
            first_name = input("Enter first name: ")
            contacts = repo.search(first_name)
            print(contacts)