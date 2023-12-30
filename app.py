from flask import Flask, jsonify, request
import subprocess

app = Flask(__name__)

@app.route('/add', methods=["POST"])
def add():
    dataDict = request.get_json()
    x = dataDict["x"]
    y = dataDict["y"]
    z = x + y
    retJSON = {"z": z}
    return jsonify(retJSON), 200

@app.route('/')
def classify_image():
    return "hello world"

@app.route('/hi')
def mat():
    c = 2 * 64
    s = str(c)
    retjson = {"name": "rohit", "name1": "mohit"}
    return jsonify(retjson)

@app.route('/run-script')
def run_script():
    try:
        result = subprocess.check_output(['python', 'test.py'], stderr=subprocess.STDOUT)
        return result, 200
    except subprocess.CalledProcessError as e:
        return e.output, 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
