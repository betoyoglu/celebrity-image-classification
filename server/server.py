from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/classify_image', methods=['POST'])
def classify_image():
    image_data = request.form["image_data"]  # base64 string
    response = jsonify(util.classify_image(image_data))  # convert to json
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == "__main__":
    print("starting python flask server for celebrity image classification")
    util.load_saved_artifacts()  # assuming this function loads your model or other necessary artifacts
    app.run(port=5000)