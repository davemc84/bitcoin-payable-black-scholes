# bitcoin-payable-black-scholes
Simple Bitcoin Payable Black-Scholes Calculator

This endpoint returns in JSON format the implied call and put price of an option as well as the major associated "Greeks."  This is a basic Black-Scholes formula, so returns infomration assuming a European-style option on a stock that is assumed to not pay a dividend.

On the 21.co Bitcoin network, this can be accessed by entering the following into the command line:

```21  buy --maxprice 100 url 'http://10.244.190.107:5000/bs?price=35&strike=40&time=0.25&rate=0.03&vol=0.4'```

* price  = current stock price
* strike = strike price
* time   = portion of a year until expiration (e.g., 0.25 = a quarter of a year, 0.5 = half a year)
* rate   = assumed risk free rate
* vol    = assumed volatility

The format of the returned JSON data starts with either a "c" or "p" to denote "call" or "put" and then lists what the data item is (e.g., "cPrice" = the implied price of a call option, "pTheta" = implied Theta for a put option).
