import re
from flask import Flask,render_template, jsonify, request, url_for, redirect
import random
import json

# import json
from bson import json_util
from consumer import TrinitClient

import os
from werkzeug.utils import secure_filename
from datetime import datetime



app  = Flask(__name__)
PORT = 3000

trinitclient = TrinitClient()




@app.route("/", methods=["GET"])
def startpy():

    return render_template("login.html") 











if __name__ == "__main__":
    app.run(debug = True,host="0.0.0.0",port = PORT)