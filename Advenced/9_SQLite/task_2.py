import sys
import sqlite3

class FinanceRepo:
    def __init__(self, db):
        self.db = db

    def earn(self, name, amount):
        cursor = self.db.cursor()
        cursor.execute("""
        INSERT INTO finance (name, amount)
        VALUES (?,?)        
        """,
        (name, amount)
        )

    def spend(self, name, amount):
        cursor = self.db.cursor()
        cursor.execute(
            """
            INSERT INTO finance (name, amount)
            VALUES (?,?)
            """,
            (name, amount)
        )

    def balance(self):
        cursor = self.db.cursor()
        cursor.execute(
            """
            SELECT * FROM finance WHERE name='kirim'
            """
        )
        balance = cursor.fetchall()
        summa  = 0
        for i in range(len(balance)):
            summa += int(balance[i][1])

        cursor.execute(
            """
            SELECT * FROM finance WHERE name='chiqim'
            """
        )
        balance = cursor.fetchall()

        for i in range(len(balance)):
            summa -= int(balance[i][1])

        return  summa


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit("only 1 argument is required")

    available_commands = ["earn", "spend", "balance"]
    command = sys.argv[1]

    if command not in available_commands:
        sys.exit(f"invalid command: {command}, available commands: {available_commands} ")

    with sqlite3.connect('finance.db') as db:
        cursor = db.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS finance (
            name VARCHAR,
            amount VARCHAR
            )
            """
        )
        repo = FinanceRepo(db)
        if command == "earn":
            name = "kirim"
            amount = int(input("Enter amount to earn: "))
            repo.earn(name, amount)
            print("successfully earned " + name)
        elif command == "spend":
            name = 'chiqim'
            amount = int(input("enter amount to spend: "))
            repo.spend(name, amount)
        elif command == "balance":
            sum_amount = repo.balance()
            print(sum_amount)
