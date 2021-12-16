from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'GET':
        return 'Hello World'
    else:
        json_request = request.get_json()
        if json_request is None:
            return jsonify(code=500, message='Error')
        else:
            is_valid_request = json_request.get('valid')
            if is_valid_request is not None:
                return jsonify(code=200, message='Success Request')
            else:
                return jsonify(code=403, message='Invalid Request')


@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return 'Tuan Anh'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)