from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# --- Köhnə funksiyalar (JSON və CSV) ---
def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)

def read_csv():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

# --- Yeni: SQL funksiyası ---
def read_sql():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()
    conn.close()
    
    # Nəticəni JSON/CSV ilə eyni formatda qaytarırıq (List of Dictionaries)
    products = []
    for row in rows:
        products.append({
            'id': row[0],
            'name': row[1],
            'category': row[2],
            'price': row[3]
        })
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    data = []
    error = None

    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    elif source == 'sql':
        data = read_sql()
    else:
        error = "Wrong source"

    if not error and product_id:
        filtered_data = [p for p in data if str(p['id']) == product_id]
        if not filtered_data:
            error = "Product not found"
        else:
            data = filtered_data

    return render_template('product_display.html', products=data, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
