from flask import Flask, request, make_response

from utils import verify_sign, rsa_encrypt

app = Flask(__name__)

app.config.update({'pri_key': 'private_key.pem'})
app.config.update({'pub_key': 'public_key.pem'})


@app.route('/<path:signature>', methods=['GET', ])
def index(signature):
    remote_ip = request.headers.get('X-Forwarded-For')
    remote_ip = remote_ip if remote_ip else request.remote_addr
    msg = verify_sign(bytes(signature, 'utf-8'), app.config['pri_key'])
    if msg is not None:
        signature = msg
    else:
        msg = rsa_encrypt(signature, app.config['pub_key'])
        # print(signature)
    show_msg = '{}: {}'.format(remote_ip, signature)
    resp = make_response(show_msg)
    resp.headers['custom'] = str(msg)
    return resp


if __name__ == '__main__':
    app.run(debug=True)
