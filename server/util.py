import pickle
import json
import numpy as np

__internetservice = None
__contract = None
__paymentmethod = None
__data_columns = None
__model = None

# def get_estimated_price(location,sqft,bhk,bath):
def get_estimated_price(gender, seniorcitizen, partner, dependents, tenure, phoneservice, multiplelines, onlinesecurity, onlinebackup, deviceprotection, techsupport, streamingtv, streamingmovies, paperlessbilling, monthlycharges, totalcharges, internetservice, contract, paymentmethod):
    try:
        locser_index = __data_columns.index(internetservice.lower())
    except:
        locser_index = -1

    try:
        loccon_index = __data_columns.index(contract.lower())
    except:
        loccon_index = -1

    try:
        locpay_index = __data_columns.index(paymentmethod.lower())
    except:
        locpay_index = -1

    x = []
    x.append(int(gender))
    x.append(int(seniorcitizen))
    x.append(int(partner))
    x.append(int(dependents))
    x.append(int(tenure))
    x.append(int(phoneservice))
    x.append(int(multiplelines))
    x.append(int(onlinesecurity))
    x.append(int(onlinebackup))
    x.append(int(deviceprotection))
    x.append(int(techsupport))
    x.append(int(streamingtv))
    x.append(int(streamingmovies))
    x.append(int(paperlessbilling))
    x.append(float(monthlycharges))
    x.append(float(totalcharges))

    # x.append(locser_index)
    # x.append(loccon_index)
    # x.append(locpay_index)
    # x[0] = int(gender)
    # x[1] = int(seniorcitizen)
    # x[2] = int(partner)
    # x[3] = int(dependents)
    # x[4] = int(tenure)
    # x[5] = int(phoneservice)
    # x[6] = int(multiplelines)
    # x[7] = int(onlinesecurity)
    # x[8] = int(onlinebackup)
    # x[9] = int(deviceprotection)
    # x[10] = int(techsupport)
    # x[11] = int(streamingtv)
    # x[12] = int(streamingmovies)
    # x[13] = int(paperlessbilling)
    # x[14] = monthlycharges
    # x[15] = totalcharges

    # gender
    # seniorcitizen
    # partner
    # dependents
    # tenure
    # phoneservice
    # multiplelines
    # onlinesecurity
    # onlinebackup
    # deviceprotection
    # techsupport
    # streamingtv
    # streamingmovies
    # paperlessbilling
    # monthlycharges
    # totalcharges

    # internetservice
    # contract
    # paymentmethod

    # if locser_index>=0:
    #     x[locser_index] = int(1)
    # if loccon_index>=0:
    #     x[loccon_index] = int(1)
    # if locpay_index>=0:
    #     x[locpay_index] = int(1)
    for i in range(16,26):
        if i==locser_index:
            x.append(True)
        elif i==loccon_index:
            x.append(True)
        elif i==locpay_index:
            x.append(True)
        else:
            x.append(False)

    print("X:",x)
    return __model.predict([x])[0]
    # return round(__model.predict(a)[0])


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __internetservice
    global __contract
    global __paymentmethod

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __internetservice = __data_columns[16:19]
        __contract = __data_columns[19:22]
        __paymentmethod = __data_columns[22:26]

    global __model
    if __model is None:
        with open('./artifacts/model_cust_churn.pickle', 'rb') as f:
            __model = pickle.load(f)
            print(__model.predict([[0, 0, 0, 0, 2, 1, 0, 1, 1, 0, 0, 0, 0, 1, 53.85, 1000.15, True, False, False, True, False, False, False, False, False, True]]))
            print("loading saved artifacts...done",)

def get_internetservice_types():
    # print(__internetservice)
    return __internetservice

def get_contract_types():
    # print(__contract)
    return __contract

def get_paymentmethod_types():
    return __paymentmethod

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    # print(get_data_columns())
    print(get_internetservice_types())
    # print(get_paymentmethod__types())
    # print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    # print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    # print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
    # print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location
    # print(get_estimated_price([[1,0,1,0,1,0,0,0,1,0,0,0,0,1,29.85,29.85,True,False,False,True,False,False,False,False,True,False]]))

    # {"data_columns": ["gender", "seniorcitizen", "partner", "dependents", "tenure", "phoneservice", "multiplelines", "onlinesecurity", "onlinebackup", "deviceprotection", "techsupport", "streamingtv", "streamingmovies", "paperlessbilling", "monthlycharges", "totalcharges", "internetservice_dsl", "internetservice_fiber optic", "internetservice_no", "contract_month-to-month", "contract_one year", "contract_two year", "paymentmethod_bank transfer (automatic)", "paymentmethod_credit card (automatic)", "paymentmethod_electronic check", "paymentmethod_mailed check"]}