from flask import Flask
app = Flask(__name__)

@app.route('/')
def home_page():
   return 'Home Page'

@app.route('/hw/')
def hello_world():
   return 'Hello World'

if __name__ == '__main__':
   app.run('127.0.0.1',3001,True)