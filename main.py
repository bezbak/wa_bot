import os
from flask import Flask, request, render_template, redirect
from twilio.twiml.messaging_response import MessagingResponse
from werkzeug.utils import secure_filename
from create_db import create_table
from answers import *
# BASE_DIR = 
UPLOAD_FOLDER = './media'
# Init the Flask App
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/incoming', methods=['POST'])
def incoming():
    incoming_que = request.values.get('Body', '').lower()
    bot_resp = MessagingResponse()
    msg = bot_resp.message()
    menu1 = menu(incoming_que)
    msg.body(str(menu1))
    print('работай')
    return str(bot_resp)

@app.route('/test', methods=['GET', "POST"])
def test():
    bot_resp = MessagingResponse()
    msg = bot_resp.message()
    msg.body(hello_text)
    return str(bot_resp)
@app.route('/admin', methods=['POST', "GET"])
def admin():
    if request.method == 'POST':
        data = request.files
        data_text = request.values
        image = data['image']
        filename = secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # create_table(data_text['title'],data_text['description'], image.filename)
        return redirect(request.url)
    return render_template('admin.html')
# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=5000)
