from flask import Flask

app = Flask(__name__) #constructor of the flask

@app.route('/')
def base_route():
    return "Welcome to Praxis"

@app.route("/my_name/<name>")
def print_name(name):
    return f"Welcome" 

if __name__ == "__main__":
    app.run( port = 8000,debug = True)