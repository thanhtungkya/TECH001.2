from flask import Flask, jsonify

app = Flask(__name__)

def is_prime(so):
    if so < 2:
        return False
    for i in range(2, int(so ** 0.5) + 1):
        if so % i == 0:
            return False
    return True

@app.route('/prime_number/<int:so>')
def kiem_tra(so):
    res = is_prime(so)
    return jsonify({
        "Number": so,
        "isPrime": res
    })


app.run(debug=True)
#data type
#var
#loop(for, while, range(start:stop:step))
#if else
#function
#string
#regular expression
#class(association, Aggregation, ke thua, da hinh, truu tuong, dong goi)
#API, backend service.