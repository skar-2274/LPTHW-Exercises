from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    greeting = "World"
    return f'Hello, {greeting}!'

if __name__ == "__main__":
    app.run()

# to activate the flask debugger run the following command on powershell:
# $env:FLASK_ENV = "development"

# to deactivate it:
# $env:FLASK_ENV = "production"

# to make the environment false:
# $env:FLASK_ENV = "false"

#never run the debugger with a created website online as it can get hacked.
