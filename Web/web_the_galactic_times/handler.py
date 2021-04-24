from flask import Flask, request
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello():
    print(request.headers)
    print(str(request.get_data().decode("ascii")))
    return "Very very hot damn, like uhm 40deg celsius wow!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
