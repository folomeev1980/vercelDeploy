from flask import Flask
import time


class Value:
    val = 0

    def valueCalculator(self):
        while True:
            Value.val = Value.val + 1
            time.sleep(10)


app = Flask(__name__)

v = Value()
v.valueCalculator()


@app.route("/")
def home():
    return "<h2>Flask Vercel {} </h2>".format(v.val)


@app.route("/other_route")
def other():
    return "<h2>Other Pagel</h2>"

# if __name__ == '__main__':
#     app.run(debug=True)
