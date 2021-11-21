# set up a flask server to serve in localhost:5000
from datetime import datetime
from flask import Flask, render_template, request, send_file
import requests
import os
import random
import string


app = Flask(__name__, template_folder='.')

# declare folder to save files from requests to the server (in this case, folder)
# (this is the folder where the files will be saved)
UPLOAD_FOLDER = './uploads'
TEMPLATES = './templates'


def template_path(template):
    return TEMPLATES + '/' + template


time_now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# create a session token to be used in the requests to the server
# (this is the token that will be used in the requests to the server)
secure_token = 'yourdamntoken'.join(random.choice(
    string.ascii_uppercase + string.digits) for _ in range(32))
session_token = 'secure_token' + time_now


@app.after_request
def after_request(response):
    secure_token = ''.join(random.choice(
        string.ascii_uppercase + string.digits) for _ in range(256))
    session_token = secure_token + time_now
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET, POST'),
    response.headers.add('X-Session-Token:', session_token)
    return response


@app.route("/", methods=["GET", "POST"])
# get data from the POST request and print it out to the console for debugging purposes
def index():
    if request.method == "POST":
        # print json.dumps(request.json)
        print(request.json)
        return "OK"
    else:
        # print the ip address of the client that is connecting to the server (in this case, the client)
        print(request.remote_addr)
        # print SO from client
        print(request.headers.get('User-Agent'))
        # print all information about the client that is connecting to the server (in this case, the client)
        print(request.headers)

        # save request.remote_addr to file ips.txt
        with open("ips.txt", "a") as f:
            f.write("Time: " + time_now + " | " + "X-Forwarded-For: " + request.headers.get('X-Forwarded-For') + " | " + "IP: " + str(request.remote_addr) +
                    " | " + "OS: " + request.headers.get('User-Agent') + "\n")
        return "OK"


@app.route("/files", methods=["GET", "POST"])
# get data from the POST request and print it out to the console for debugging purposes
def files():
    if request.method == "POST":
        # save file from the request to folder "folder"
        file = request.files['file']
        # save file to UPLOAD_FOLDER
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        return "OK"
    else:
        return render_template(template_path('files.html'))


@app.route("/directory", methods=["GET"])
def my_directory():
    # get all files in the UPLOAD_FOLDER
    files = os.listdir(UPLOAD_FOLDER)
    # return the list of files in the UPLOAD_FOLDER
    return render_template(template_path('directory.html'), files=files)


@app.route("/cookies", methods=["GET", "POST"])
def cookies():
    # get all cookies from the request
    cookies = request.cookies
    # print all cookies from the request
    print(cookies)
    return render_template(template_path('index.html'))


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_file(os.path.join(UPLOAD_FOLDER, filename))


@app.route("/message", methods=["GET", "POST"])
# receive a json payload from the client and print it out to the console for debugging purposes
def message():
    if request.method == "POST":
        # print json body from the request
        print(request.json)
        return "OK"
    else:
        return render_template(template_path('chat.html'))


if __name__ == "__main__":
    app.run(debug=True, host="192.168.1.2", port=5000)
