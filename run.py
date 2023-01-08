from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

context = {}


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        model = pickle.load(open("./Scripts/model.pkl", "rb"))
        user_input = request.form.get("text")
        prediction = model.predict([user_input])[0].upper()
        y_pred = model.predict_proba([user_input])
        prob_fake = round(y_pred[0][0] * 100, 2)
        prob_true = round(y_pred[0][1] * 100, 2)

        context.update(
            {
                "status": "valid",
                "prediction": prediction,
                "user_input": user_input,
                "prob_fake": prob_fake,
                "prob_true": prob_true,
            }
        )
    return render_template("index.html", context=context)


if __name__ == "__main__":
    app.run(debug=True)
