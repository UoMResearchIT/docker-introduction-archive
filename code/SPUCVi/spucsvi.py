from flask import Flask, request, render_template
import requests

import os
import sys
from datetime import datetime

import uvicorn

app = Flask(__name__)


@app.route("/")
def spucsvi():
    # get data (hit localhost 8321 at export endpoint)
    data = requests.get("http://localhost:8321/export")
    print(data)

    return render_template("spucsvi.html", data=data)


if __name__ == "__main__":
    app.run()
