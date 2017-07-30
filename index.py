from flask import Flask


app = FLask(__name__)

@app.route('/')
def index():
    return 'Hello Flask !!'

app.run()