from datetime import datetime

import flask
from flask import jsonify, request 

app = flask.Flask(__name__)
app.config["DEBUG"] = True
results = []

@app.route("/results", methods=["GET"])
def recent_results():
    
    return jsonify(results[-10:][::-1]), 200
    
@app.route("/operate", methods=["GET"])
def operate():

    if "operation" in request.args:
        operation = request.args["operation"]
    else:
        return dict(error="Calculation Error", message="Invalid operation"), 400
    result = 0
    # Check for the operation type and get the result.
    try:
        if "+" in operation:
            num = operation.split("+")
            result = int(num[0]) + int(num[1])
        if "-" in operation:
            num = operation.split("-")
            result = int(num[0]) - int(num[1])
        if "*" in operation:
            num = operation.split("*")
            result = int(num[0]) * int(num[1])
        if "/" in operation:
            num = operation.split("/")
            result = int(num[0]) / int(num[1])
        response = {"updated_date": datetime.now(
        ), "operation": operation, "result": result}
        results.append(response)
        return response, 200
    except Exception as e:
        return dict(error="Calculation Error", exception=str(e), message="Review operation and try again"), 400

@app.errorhandler(404)
def page_not_found(error):
    return dict(response="This page does not exist"), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0")
