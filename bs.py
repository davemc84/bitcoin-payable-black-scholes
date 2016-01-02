import json
from flask import Flask, request
from two1.lib.wallet import Wallet
from two1.lib.bitserv.flask import Payment
from scipy.stats import norm
from math import *

app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)

@app.route('/bs')
@payment.required(10)
def BlackScholes():
    data = {}
    S = float(request.args.get('price'))
    K = float(request.args.get('strike'))
    T = float(request.args.get('time'))
    R = float(request.args.get('rate'))
    V = float(request.args.get('vol'))

    d1 = (log(float(S)/K)+(R+V*V/2.)*T)/(V*sqrt(T))
    d2 = d1-V*sqrt(T)

    data['cPrice'] = S*norm.cdf(d1)-K*exp(-R*T)*norm.cdf(d2)
    data['pPrice'] = K*exp(-R*T)-S+data['cPrice']

    data['cDelta'] = norm.cdf(d1)
    data['cGamma'] = norm.pdf(d1)/(S*V*sqrt(T))
    data['cTheta'] = (-(S*V*norm.pdf(d1))/(2*sqrt(T))-R*K*exp(-R*T)*norm.cdf(d2))/365
    data['cVega'] = S*sqrt(T)*norm.pdf(d1)/100
    data['cRho'] = K*T*exp(-R*T)*norm.cdf(d2)/100

    data['pDelta'] = data['cDelta']-1
    data['pGamma'] = data['cGamma']
    data['pTheta'] = (-(S*V*norm.pdf(d1))/(2*sqrt(T))+R*K*exp(-R*T)*norm.cdf(-d2))/365
    data['pVega'] = data['cVega']
    data['pRho'] = -K*T*exp(-R*T)*norm.cdf(-d2)/100

    return json.dumps(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
