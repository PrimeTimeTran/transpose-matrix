from flask import Flask, request, jsonify

app = Flask(__name__)


class MatrixTransformer:
    def __init__(self, matrix):
        self.matrix = matrix

    def transpose(self):
        # O(M*N) where m is the length of the shortest list and n is the number of lists
        return [col for col in zip(*self.matrix)]


@app.route("/", methods=['POST'])
def home():
    matrix = request.get_json()
    matrix_transformer = MatrixTransformer(matrix)
    res = matrix_transformer.transpose()
    return jsonify(res)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
