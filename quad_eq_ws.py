from math import sqrt
from flask import Flask, render_template, request

app = Flask('main')

def quad_eq_solve(a, b, c):
    x = []
    d = b ** 2 - 4 * a * c  # Calculate the discriminant
    if d < 0:
        return x, d  # No real roots
    elif d == 0:
        x.append(-b / (2 * a))  # One real root
    else:
        x.append((-b + sqrt(d)) / (2 * a))  # Two real roots
        x.append((-b - sqrt(d)) / (2 * a))
    return x, d

@app.route("/")
def quad_eq_get():
    a, b, c, x1, x2, D = '', '', '', '', '', ''
    showDisplay = 'roots'  # Default to showing roots
    return render_template('index.html', a=a, b=b, c=c, X1=x1, X2=x2, D=D, showDisplay=showDisplay)

@app.route("/quad_eq", methods=['POST'])
def quad_eq_post():
    a = request.form['a']
    b = request.form['b']
    c = request.form['c']
    showDisplay = request.form['display']  # Get selected display option

    x, D = quad_eq_solve(float(a), float(b), float(c))
    x1, x2 = '', ''
    if len(x) == 0:
        x1 = 'Нет корней'
    if len(x) >= 1:
        x1 = str(x[0])  # First root
    if len(x) == 2:
        x2 = str(x[1])  # Second root

    return render_template('index.html', a=a, b=b, c=c, X1=x1, X2=x2, D=D, showDisplay=showDisplay)

app.run(debug=True)