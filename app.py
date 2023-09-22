from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        input_text = request.form['text']
        output = predict_genres(request.form['text'])[0]
        print(output)
        return render_template("results.html", input_text=input_text, output_text=output)
    else:
        return render_template("index.html")


def predict_genres(input_text):
    response = requests.post("https://tdnathmlenthusiast-laptop-guru.hf.space/run/predict", json={
        "data": [input_text]
    }).json()

    data_list = response.get('data', [])

    return data_list


if __name__ == "__main__":
    app.run(debug=True)
