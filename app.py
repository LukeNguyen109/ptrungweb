from flask import Flask, render_template

app = Flask(__name__)

# Trang chủ (menu)
@app.route('/')
def menu():
    return render_template("index.html")

# Trang sinh nhật (index)
@app.route('/birthday')
def birthday():
    return render_template("birthday.html")

if __name__ == "__main__":
    app.run(debug=True)
