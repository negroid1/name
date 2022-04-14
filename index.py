from flask import Flask


app = Flask("index")


@app.route('/')
def index():
  return "hello world"
  
  
  app.run(port='8000')
