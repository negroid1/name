from flask import Flask


app = Flask(_name_)


@app.route('/')
def index():
  return "hello world"
app.run(port='8000')
