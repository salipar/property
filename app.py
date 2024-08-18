from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('invoices.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    offset = (page - 1) * per_page

    conn = get_db_connection()
    invoices = conn.execute('SELECT * FROM invoice_headers order by invoice_number LIMIT ? OFFSET ?', 
                            (per_page, offset)).fetchall()
    total_invoices = conn.execute('SELECT COUNT(*) FROM invoice_headers').fetchone()[0]
    conn.close()

    total_pages = (total_invoices + per_page - 1) // per_page

    return render_template('index.html', invoices=invoices, page=page, total_pages=total_pages)

@app.route('/invoice/<invoice_number>')
def invoice_details(invoice_number):
    conn = get_db_connection()
    invoice = conn.execute('SELECT * FROM invoice_headers WHERE invoice_number = ?', 
                           (invoice_number,)).fetchone()
    details = conn.execute('SELECT * FROM invoice_details WHERE invoice_number = ?', 
                           (invoice_number,)).fetchall()
    conn.close()
    return render_template('invoice_detail.html', invoice=invoice, details=details)

@app.route('/create_invoice', methods=['GET', 'POST'])
def create_invoice():
    if request.method == 'POST':
        invoice_number = request.form['invoice_number']
        customer_name = request.form['customer_name']
        invoice_date = request.form['invoice_date']
        products = request.form.getlist('product_name')
        quantities = request.form.getlist('quantity')
        prices = request.form.getlist('price')

        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute('''
                INSERT INTO invoice_headers (invoice_number, customer_name, invoice_date)
                VALUES (?, ?, ?)
            ''', (invoice_number, customer_name, invoice_date))

            for product, quantity, price in zip(products, quantities, prices):
                cursor.execute('''
                    INSERT INTO invoice_details (invoice_number, product_name, quantity, price)
                    VALUES (?, ?, ?, ?)
                ''', (invoice_number, product, quantity, price))

            conn.commit()
            flash('Invoice created successfully!', 'success')
        except sqlite3.IntegrityError:
            flash('Invoice number already exists. Please choose another one.', 'danger')
        finally:
            conn.close()

        return redirect(url_for('index'))

    return render_template('create_invoice.html')


if __name__ == '__main__':
    app.run(debug=True)

