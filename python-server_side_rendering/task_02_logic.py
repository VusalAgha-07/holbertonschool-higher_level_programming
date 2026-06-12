from flask import Flask, render_template

app = Flask(__name__)

@app.route('/items')
def items():
    # Example data: a list of items
    items_list = ["Flask", "HTML", "Templates"]
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
