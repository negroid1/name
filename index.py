from flask import Flask


app = Flask(index.py)


@app.route('/')
def index():
  return "hello world"
  
  
  app.run(port='8000')
