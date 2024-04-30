import sqlite3

with sqlite3.connect('contacts.db') as db:
    cursor = db.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts(
    first_name VARCHAR,
    last_name VARCHAR,
    phone_number VARCHAR
    )
    """
                   )
    cursor.execute("""
    INSERT INTO contacts (first_name, last_name, phone_number)
    VALUES ('Bob', 'Smith', '12345')
    """)

    cursor.execute(
        """
        SELECT * FROM contacts
        """
    )
    rows = cursor.fetchall()
    print(rows)
