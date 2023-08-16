from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hi, this is my first app with Flask!'

if __name__ == '__main__':
    app.run()
