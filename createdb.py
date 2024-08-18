import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('invoices.db')
cursor = conn.cursor()

# Create invoice_headers table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS invoice_headers (
        id INTEGER PRIMARY KEY,
        invoice_number TEXT UNIQUE NOT NULL,
        customer_name TEXT NOT NULL,
        invoice_date TEXT NOT NULL
    )
''')

# Create invoice_details table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS invoice_details (
        id INTEGER PRIMARY KEY,
        invoice_number TEXT NOT NULL,
        product_name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        price REAL NOT NULL,
        FOREIGN KEY(invoice_number) REFERENCES invoice_headers(invoice_number)
    )
''')

# Commit and close
conn.commit()
conn.close()
