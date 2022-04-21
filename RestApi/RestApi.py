from flask import Flask, jsonify
import requests
import json


app = Flask(__name__)

@app.route('/')
def index():
    return """use +
        \nqueryAirportTemp +
        \nqueryStockPrice +
        \nqueryEval"""

@app.route("/queryAirportTemp=<string:iaia>", methods=['GET'])
def get_airport(iaia):
    key = "fkoL0RhWHAFCZVlxMt5JA7AnGy4HXxw2"
    q = ("http://dataservice.accuweather.com/locations/v1/poi/search?apikey=fkoL0RhWHAFCZVlxMt5JA7AnGy4HXxw2&q=" + iaia +"&type=38&language=EN&details=false")
    response = requests.get(q)
    js = response.json()

    locationk = js[0]["Key"]
    qe = "http://dataservice.accuweather.com/currentconditions/v1/" + locationk + "?apikey=fkoL0RhWHAFCZVlxMt5JA7AnGy4HXxw2&language=EN"
    response = requests.get(qe)
    r = response.json()
    t = r[0]["Temperature"]["Metric"]["Value"]

    return jsonify({"queryAirportTemp" : t})

@app.route("/queryStockPrice=<string:s>")
def get_stock(s):   
    url = "https://yfapi.net/v6/finance/quote?"
    querystring = {"symbols":s}
    headers = {
        'x-api-key': "Q68FavI2RXatqNZG8VVax6xON8eslOok8nnnoEiG"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    j = response.json()
    val = j["quoteResponse"]["result"][0]["bookValue"]

    return jsonify({"queryStockPrice" : val})
    
@app.route("/queryEval=<string:s>")
def get_eval(s):
    return jsonify({"/queryEval" : eval(s)})
    


if __name__ == "__main__":
    app.run(debug=True)