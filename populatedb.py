import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('invoices.db')
cursor = conn.cursor()

# Insert some data into invoice_headers
cursor.executemany('''
    INSERT INTO invoice_headers (invoice_number, customer_name, invoice_date)
    VALUES (?, ?, ?)
''', [
    ('INV015', 'John Doe', '2024-08-01'),
    ('INV016', 'Jane Smith', '2024-08-05'),
    ('INV003', 'Shiju Chandroth', '2024-08-01'),
    ('INV004', 'Sha Khan', '2024-08-05'),
    ('INV005', 'Amar Kumar', '2024-08-01'),
    ('INV006', 'Jane Smith', '2024-08-05'),
    ('INV007', 'John Doe', '2024-08-01'),
    ('INV008', 'Jane Smith', '2024-08-05'),
    ('INV009', 'John Doe', '2024-08-01'),
    ('INV010', 'Jane Smith', '2024-08-05'),
    ('INV011', 'John Doe', '2024-08-01'),
    ('INV012', 'Jane Smith', '2024-08-05'),
    ('INV013', 'John Doe', '2024-08-01'),
    ('INV014', 'Jane Smith', '2024-08-05'),
    # Add more records as needed
])

# Insert some data into invoice_details
cursor.executemany('''
    INSERT INTO invoice_details (invoice_number, product_name, quantity, price)
    VALUES (?, ?, ?, ?)
''', [
    ('INV015', 'Product A', 2, 30.0),
    ('INV015', 'Product B', 1, 20.0),
    ('INV016', 'Product C', 5, 15.0),
    ('INV003', 'Product A', 2, 30.0),
    ('INV003', 'Product B', 1, 20.0),
    ('INV004', 'Product C', 5, 15.0),
    ('INV005', 'Product A', 2, 30.0),
    ('INV005', 'Product B', 1, 20.0),
    ('INV006', 'Product C', 5, 15.0),
    ('INV007', 'Product A', 2, 30.0),
    ('INV007', 'Product B', 1, 20.0),
    ('INV002', 'Product C', 5, 15.0),
    ('INV001', 'Product A', 2, 30.0),
    ('INV001', 'Product B', 1, 20.0),
    ('INV008', 'Product C', 5, 15.0),
    ('INV009', 'Product A', 2, 30.0),
    ('INV009', 'Product B', 1, 20.0),
    ('INV010', 'Product C', 5, 15.0),
    ('INV011', 'Product A', 2, 30.0),
    ('INV011', 'Product B', 1, 20.0),
    ('INV012', 'Product C', 5, 15.0),
    ('INV013', 'Product A', 2, 30.0),
    ('INV013', 'Product B', 1, 20.0),
    ('INV014', 'Product C', 5, 15.0),
    # Add more records as needed
])

# Commit and close
conn.commit()
conn.close()
