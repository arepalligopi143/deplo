from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/gopi')
def gopi():
    return 'this is gopi file'
@app.route('/laasya')
def laasya():
    return render_template('/laasya.html')


if __name__ == '__main__':
    app.run(debug=True)
