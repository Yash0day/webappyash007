from urllib import request
from flask import Flask, request
import numpy as np

app = Flask(__name__)

@app.route("/")
def window():
    return "<h1>To get the calculations Usage: /index?lower=0&upper=10</p>"

def calc(lower, upper, list1 = [1, 10, 100, 1000, 10000, 100000, 1000000]): 
    list_calc = []
    for i in list1:
        int_len = (upper - lower)/i
        centers = np.arange(lower+int_len/2, upper, int_len)
        values = np.abs(np.sin(centers))*int_len
        list_calc.append(np.sum(values))
    return list_calc

@app.route("/index")
def index():
    lower = request.args.get('lower')
    upper = request.args.get('upper')
    lower = float(lower) if lower else None
    upper = float(upper) if upper else None

    results = calc(lower, upper)
    return '''<h1>The Calculator</h1> \
        <p>Inputs: \n<em> Lower: </em> {} <br> \
            <em> Upper: </em> {} <br> \
            <em>Results: </em> <b>{}</b></p>'''.format(lower, upper, results)
            
            #az group list

       #az vmss list-instance-connection-info --resource-group resource_yash007 --name scalset_yash007
       #{
       # "instance 1": "52.188.62.216:50001",
        #"instance 2": "52.188.62.216:50002"
        #}
