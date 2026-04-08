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
