import os
import datetime
from flask import Flask, send_from_directory, request, redirect, url_for
from werkzeug import secure_filename

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


@app.route('/upload/', methods=['GET', 'POST'])
def upload_file():
    if request.method in ['POST', ]:
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            if os.path.isfile(os.path.join(app.config['file_path'], filename)):
                o_filename = os.path.join(app.config['file_path'], filename)
                c_time = datetime.datetime.fromtimestamp(os.stat(o_filename).st_ctime)
                os.rename(o_filename, '{}.bak.{}'.format(o_filename, c_time.strftime('%Y_%m_%d_%H_%M_%S')))
            file.save(os.path.join(app.config['file_path'], filename))
            return redirect(url_for('upload_file', filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''


if __name__ == '__main__':
    app.run(debug=True)
