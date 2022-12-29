from flask import Flask, jsonify, request
from flask_cors import CORS
import calidad_del_aire
app = Flask(__name__)
CORS(app)

@app.route("/getDataClassifier", methods=['POST'])
def hello():
    user_input= request.json['']
    return jsonify({'msg':str(calidad_del_aire.brain(user_input))})

if __name__ == "__main__":
    app.run(host='0.0.0.0')    