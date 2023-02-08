from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    res = []
    matrix = request.json['body']
    for col in zip(*matrix):
      res.append(col)
    return jsonify(res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)