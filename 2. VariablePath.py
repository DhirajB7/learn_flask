from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/hello/<name>/')
def greet_user(name):
   return f'Hello {name}'

@app.route('/hello/<name>/<int:age>/')
def greet_user_age(name,age):
   return f'Hello {name} you are {age} years.'

if __name__ == '__main__':
   app.run('127.0.0.1',3001,True)