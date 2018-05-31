from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'msg': 'yup... i am operational...'}), 200

@app.route('/uthere')
def uthere():
    return jsonify({'msg': 'of course I am!... where did you think I was?...'}), 200

@app.route("/get-my-ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=18080)
