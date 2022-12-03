import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


flask_app = Flask(__name__)
model = pickle.load(open("regressor.pickle", "rb"))


@flask_app.route("/")
def Home():
    return render_template("index.html")


@flask_app.route("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    # sumi = sum(float_features)
    max = [10, 10, 10, 50, 10, 100, 10, 10, 5, 5, 10, 200, 1000, 10, 10, 1500, 100, 250, 250, 100, 1, 1, 300, 1]

    score = 0
    print(len(max), len(float_features))

    for i in range(24):
        l = np.linspace(0,max[i],10)
        if float_features[i] > max[i]:
            score+=10
        for i in range(1,10):
            if float_features[i] > l[i-1] and float_features[i] <=l[i]:
                score+=i
    percentage = (score/240)*100
    print(percentage)
    features = [np.array(float_features)]
    print(float_features)
    print(score)
    prediction = model.predict(features)
    prediction = int(prediction[0])
    return render_template("index.html", prediction_text = f"The expected profit is ${prediction}M \n\nEstimated success rate: {score}%")

if __name__ == "__main__":
    flask_app.run(debug=False)