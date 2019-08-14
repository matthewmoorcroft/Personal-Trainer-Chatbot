from flask import Flask, request, send_file

app = Flask(__name__)


@app.route('/photo', methods=['GET'])
def get_photo():
    image_name = request.args['name']
    type = request.args['type']

    return send_file(image_name, mimetype=('image/'+type))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5089, debug=True)
