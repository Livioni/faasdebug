# Copyright (c) Alex Ellis 2017. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

from flask import Flask, request, jsonify
from function import handler
from waitress import serve
import os,json
 
app = Flask(__name__)

# distutils.util.strtobool() can throw an exception
def is_true(val):
    return len(val) > 0 and val.lower() == "true" or val == "1"

@app.before_request
def fix_transfer_encoding():
    """
    Sets the "wsgi.input_terminated" environment flag, thus enabling
    Werkzeug to pass chunked requests as streams.  The gunicorn server
    should set this, but it's not yet been implemented.
    """

    transfer_encoding = request.headers.get("Transfer-Encoding", None)
    if transfer_encoding == u"chunked":
        request.environ["wsgi.input_terminated"] = True

@app.route("/", defaults={"path": ""}, methods=["POST", "GET"])
@app.route("/<path:path>", methods=["POST", "GET"])
def main_route(path):
    if (request.method == 'POST'):
        json_data = request.get_data().decode('utf-8').replace("'", '"')
        body = json.loads(json_data)
        ret = handler.handle(body)
        return ret
    else:
        return request.method


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)