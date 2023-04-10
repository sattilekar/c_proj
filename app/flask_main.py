from flask import Flask, render_template,request
from app.utils import prediction

app = Flask(__name__)

@app.route("/")
def start():
    return render_template("car_html.html")

@app.route("/predict",methods=["POST","GET"])
def predict_price():
    data = request.form
    pred_obj = prediction(data)
    predicted_price = pred_obj.predict_price()
    print(predicted_price)
   
    

       
    return "ok"

if __name__ == "__main__":
    app.run(debug=True)
