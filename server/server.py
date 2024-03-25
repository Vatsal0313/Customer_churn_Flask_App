from flask import Flask, request, jsonify
app = Flask(__name__)

import util

@app.route('/get_contract_types')
def get_contract_types():
    response = jsonify({
        'contract': util.get_contract_types()
    })
    response.headers.add('Access-control-Allow-origin', '*')
    return response

@app.route('/get_internetservice_types')
def get_internetservice_types():
    response = jsonify({
        'internetservices': util.get_internetservice_types()
    })
    response.headers.add('Access-control-Allow-origin', '*')
    return response

@app.route('/get_paymentmethod_types')
def get_paymentmethod_types():
    response = jsonify({
        'paymentmethod': util.get_paymentmethod_types()
    })
    response.headers.add('Access-control-Allow-origin', '*')
    return response

@app.route('/predict_customer_churn', methods=['POST'])
def predict_home_price():
    gender = request.form["gender"]
    seniorcitizen = request.form["seniorcitizen"]
    partner = request.form["partner"]
    dependents = request.form["dependents"]
    tenure = request.form["tenure"]
    phoneservice = request.form["phoneservice"]
    multiplelines = request.form["multiplelines"]
    onlinesecurity = request.form["onlinesecurity"]
    onlinebackup = request.form["onlinebackup"]
    deviceprotection = request.form["deviceprotection"]
    techsupport = request.form["techsupport"]
    streamingtv = request.form["streamingtv"]
    streamingmovies = request.form["streamingmovies"]
    paperlessbilling = request.form["paperlessbilling"]
    monthlycharges = request.form["monthlycharges"]
    totalcharges = request.form["totalcharges"]
    internetservice = request.form["internetservice"]
    contract = request.form["contract"]
    paymentmethod = request.form["paymentmethod"]
    if gender=="Male":
        gender=0
    else:
        gender=1
    print(gender, seniorcitizen, partner, dependents, tenure, phoneservice, multiplelines, onlinesecurity, onlinebackup, deviceprotection, techsupport, streamingtv, streamingmovies, paperlessbilling, monthlycharges, totalcharges, internetservice, contract, paymentmethod)
    response = jsonify({
        'estimated_price': int(util.get_estimated_price(gender, seniorcitizen, partner, dependents, tenure, phoneservice, multiplelines, onlinesecurity, onlinebackup, deviceprotection, techsupport, streamingtv, streamingmovies, paperlessbilling, monthlycharges, totalcharges, internetservice, contract, paymentmethod))
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Customer Churn Prediction...")
    util.load_saved_artifacts()
    app.run()