from flask import Flask, redirect, url_for
app = Flask(__name__)

# to be used in url_for
@app.route("/admin/")
def hello_admin():
   return "Yo yo admin wassup"

# to be used in url_for
@app.route('/guest/<name>')
def hello_guest(name):
   return f'Hello {name}'

@app.route('/user/<name>/')
def kinda_main(name):
   if name=='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',name=name))

if __name__ == '__main__':
   app.run('127.0.0.1',3001,True)