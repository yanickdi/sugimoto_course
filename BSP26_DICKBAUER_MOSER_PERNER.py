"""
    BSP 26 - Garantiezertifikat
    Dickbauer Yanick 1030489, Moser Patrick 1114954, Perner Manuel 0633155
    WS 2016
"""
from math import exp
from lib import random_std

PRINT_BASKET_EACH_ITERATION = True

VOLATILITY = {
               'Alianz' : .352,
                  'BMW' : .276,
                'Canon' : .293,
                 'E.On' : .217,
       'France Telecom' : .276,
	  'Hewlett Packard' : .346,
	        'ING Group' : .314,
	            'Intel' : .323,
	           'Lloyds' : .234,
	        'Microsoft' : .246}

NR_PERIODS = 5
MARKET_INTEREST_RATE = .03
RISK_FREE_INTEREST_RATE = .02

def all_shares_above_initial_val(certificate, share_prices, percentage):
    """ Returns True if all shares of our certificate are currently
        listed above `percentage` percentage of their initial prices"""
    all_above = [True if share_prices[name] > percentage * certificate['initial_prices'][name] else False for name in certificate['underlyings']]
    return False not in all_above
    
def cash_coupon(certificate, percentage):
    """ Returns the amount of money we get in case of a coupon payment"""
    return sum(stake for name, stake in certificate['underlyings'].items()) * percentage

def calc_period_cash_flow(t, certificate, share_prices):
    underlyings = list(certificate['underlyings'].items())
    inital_prices = certificate['initial_prices']
    if t == 0:
        # we have to buy the certificate incl. extra charge of 3 % of each underlying
        buying_price = sum(share_prices[name] * stake for name, stake in underlyings) * 1.03
        cash_flow = -buying_price
    elif t == 1:
        # we get fixed 6 % interests
        cash_flow = sum(stake for name, stake in underlyings) * 0.06
    elif t == 2:
        # we get a coupon of 10%, if there is no share which is listed below 68% of its initial value
        if all_shares_above_initial_val(certificate, share_prices, 0.68):
            coupon = .1
        else:
            coupon = .0
        cash_flow = cash_coupon(certificate, coupon)
    elif t == 3:
        if all_shares_above_initial_val(certificate, share_prices, 0.68):
            # coupon is at least 10%, maybe even 20 % if there was no coupon in prev period
            coupon = .2 if certificate['cash_flow_in_period'][t-1] == 0 == 0 else .1
        else:
            coupon = .0
        cash_flow = cash_coupon(certificate, coupon)
    elif t == 4:
        if all_shares_above_initial_val(certificate, share_prices, 0.68):
            cf_last_per = certificate['cash_flow_in_period'][t-1]
            cf_last_but_one_per = certificate['cash_flow_in_period'][t-2]
            if cf_last_but_one_per == .0 and cf_last_per == .0:
                coupon = .3
            elif cf_last_per == .0:
                coupon = .2
            else:
                coupon = .1
        else:
            coupon = .0
        cash_flow = cash_coupon(certificate, coupon)
    elif t == 5:
        if all_shares_above_initial_val(certificate, share_prices, 0.68):
            cf_last_periods = certificate['cash_flow_in_period'][-3:]
            if cf_last_periods == [.0, .0, .0]:
                coupon = .4
            elif cf_last_periods[-2:] == [.0, .0]:
                coupon = .3
            elif cf_last_periods[-1:] == [.0]:
                coupon = .2
            else:
                coupon = .1
        else:
            coupon = .0
        cash_flow = cash_flow = cash_coupon(certificate, coupon)
        # also pay back 100 % of Nominal
        cash_flow += sum(stake for name, stake in underlyings)
    else: raise RuntimeError('no more periods coded')
    return cash_flow

def simulate_share_price_change(share_prices, t):
    """ Changes all share prices with the help of a stochastic formula """
    time = 1
    for name in share_prices:
        Wt = share_prices[name]
        vola = VOLATILITY[name]
        exp_f = exp( (MARKET_INTEREST_RATE - vola**2/2)*time  +  vola * random_std(0,1) * time**(1/2) )
        share_prices[name] = max(Wt * exp_f, 0)

def print_basket(share_prices):
    for name, price in sorted(share_prices.items()):
        print('  {} : {:.2f}'.format(name.ljust(20), price*100))
    min_key = min(share_prices, key=lambda k: share_prices[k])
    print('  Minimum val: {:.2f} ({})'.format(share_prices[min_key]*100, min_key))
        
def net_present_value(certificate, t):
    """ calculates the sum of all discounted cash flows until t=`t`"""
    return sum(certificate['cash_flow_in_period'][i] / (1+RISK_FREE_INTEREST_RATE)**i for i in range(t+1))
        
def main():
    share_prices = { name: 1 for name in VOLATILITY.keys()}
    certificate = {
        'cash_flow_in_period' : [],
        'underlyings' : {name : 1 for name in share_prices.keys()},
        'initial_prices' : { name: share_prices[name] for name in share_prices.keys()}}
    
    for t in range(6):
        cash_flow = calc_period_cash_flow(t, certificate, share_prices)
        certificate['cash_flow_in_period'].append(cash_flow)
        
        if PRINT_BASKET_EACH_ITERATION:
            print_basket(share_prices)
        # evaluation of this period:
        npv = net_present_value(certificate, t)
        print('Cash-Flow at t={}: {:+f}'.format(t, certificate['cash_flow_in_period'][t]))
        print('NPV of Certificate: {:.2f}\n\n'.format(npv))
        
        # change share prices for next iteration
        simulate_share_price_change(share_prices, t)

main()
