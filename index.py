from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h2>Flask Vercel</h2>"


@app.route("/other_route")
def other():
    return "<h2>Other Pagel</h2>"

# if __name__ == '__main__':
#     app.run(debug=True)