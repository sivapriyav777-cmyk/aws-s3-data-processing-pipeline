import sqlite3

def load_records(records):
    connection = sqlite3.connect("customers.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            city TEXT
        )
    """)

    for record in records:
        cursor.execute("""
            INSERT OR REPLACE INTO customers
            VALUES (?, ?, ?, ?)
        """, (
            record["customer_id"],
            record["name"],
            record["email"],
            record["city"]
        ))

    connection.commit()
    connection.close()
