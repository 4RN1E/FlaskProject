from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello World</h1>"

@app.route("/aboutUs")
def aboutus():
    return "<h2>About Us</h2>"

@app.route("/contactUs/<string:name>")
def contactUs(name):
    return f"<h2>Hi, {name}, contact Us at 305-348-7852</h2>"

if __name__ == '__main__':
    app.run(debug=True)   # Through app.run(   ) we can add debug=True to get a console on the web app, we can also use it to add a specific port
    #for example port=8080 if port 5000 is busy. We can also add a host to here.

