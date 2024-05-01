from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
# '<h1>Hello, This is my webpage.</h1> <style>body { display: flex; align-items: center; justify-content: center; height: 100vh; }</style>'
