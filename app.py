from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dashboard():
    data = {
        "users": 150,
        "uploads": 320,
        "urls": 210
    }
    return render_template("dashboard.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)