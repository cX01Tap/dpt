from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, BU:1650703554'

if __name__ == 'phanuruj':
    app.run(debug=True, port=80)
