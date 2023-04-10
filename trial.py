from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def start():

    return render_template("car_html.html")

@app.route('/predict',methods=["POST"])
def predict_price():
    print("hi")
    self.data = request.form
    print(self.data)

    return "ok"


if __name__ == "__main__":
    app.run(debug=True, port = 6000, host="0.0.0.0")