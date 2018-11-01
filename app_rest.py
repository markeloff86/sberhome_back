from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/home/v1.0/recommendations')
def get_motions():
    return "Pes"


if __name__ == '__main__':
    app.run(debug=True, host='192.168.43.150')
