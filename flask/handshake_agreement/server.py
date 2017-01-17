from flask import Flask, request

app = Flask(__name__)

app.config.update({'pri_key': '123456789'})
app.config.update({'pub_key': '987654321'})


@app.route('/<path:signature>', methods=['GET', ])
def index(signature):
    sign = request.args.get(signature, '')
    print(signature)
    print(sign)
    return signature


if __name__ == '__main__':
    app.run(debug=True)
