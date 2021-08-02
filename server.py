from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/armstrong/<string:n>")
def iseven(n)
    if(n%2 == 0):
       return "True"
    else:
        return "False"
if __name__ == "__main__":
    app.run()