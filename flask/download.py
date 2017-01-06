import os
from flask import Flask, send_from_directory, request

app = Flask(__name__)

app.config.update({'file_key': 'XXX'})
app.config.update({'file_path': 'FILE'})


@app.route('/download/<path:filename>/', methods=['GET', ])
def download_file(filename):
    sign = request.args.get('sign')
    if sign != app.config['file_key']:
        return 'sign is required'
    file_name = os.path.join(app.config['file_path'], filename)
    print(filename)
    if os.path.isfile(file_name):
        print(file_name)
        return send_from_directory(app.config['file_path'], filename, as_attachment=True)
    return 'test'


if __name__ == '__main__':
    app.run(debug=True)
