from flask import Flask, render_template

app = Flask(__name__)

jobs = [
    {'id': 1, 'title': 'teacher', 'location': 'New York', 'salary': 50000},
    {'id': 2, 'title': 'engineer', 'location': 'San Francisco', 'salary': 100000},
    {'id': 3, 'title': 'doctor', 'location': 'Los Angeles', 'salary': 150000},
    {'id': 4, 'title': 'lawyer', 'location': 'Chicago', 'salary': 80000},
    {'id': 5, 'title': 'programmer', 'location': 'Seattle', 'salary': 90000}
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=jobs)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


