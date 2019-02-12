import ccxt
import argparse

parser = argparse.ArgumentParser(description='Estimate the cost of an xRapid-style fiat transfer between two exchanges.')

parser.add_argument('source_amount', help='Source amount', type=float)
parser.add_argument('source_ex', help='Source exchange name')
parser.add_argument('source_cur', help='Source currency')
parser.add_argument('dest_ex', help='Destination exchange name')
parser.add_argument('dest_cur', help='Destination currency')
parser.add_argument('--transport', default='XRP')

args = parser.parse_args()

source_ex = getattr(ccxt, args.source_ex)()
dest_ex = getattr(ccxt, args.dest_ex)()

source_cur = args.source_cur.upper()
dest_cur = args.dest_cur.upper()
transport = args.transport.upper()

source_pair = "{}/{}".format(transport, source_cur)
dest_pair = "{}/{}".format(transport, dest_cur)

source_markets = source_ex.load_markets()
dest_markets = dest_ex.load_markets()

source_orderbook = source_ex.fetch_order_book(source_pair)
dest_orderbook = dest_ex.fetch_order_book(dest_pair)

total_xrp_bought = 0.0
source_amount = args.source_amount

print("Getting order book for {} from {}".format(source_pair, source_ex.name))
for price,amount in source_orderbook['asks']:

    used_amount = min(source_amount, amount*price)
    xrp_bought = used_amount / price
    total_xrp_bought += xrp_bought
    source_amount -= used_amount

    print('+ Bought {:.2f} {} @ {:.4f}'.format(xrp_bought, transport, price))

    if source_amount <= 0:
        break

buy_fee = source_markets[source_pair]['taker'] * total_xrp_bought
print('Total Bought: {:.2f} {}'.format(total_xrp_bought, transport))
print('Buy trade fee: {:.2f} {}'.format(buy_fee, transport))
total_xrp_bought -= buy_fee
print('Net: {:.2f} {}'.format(total_xrp_bought, transport))


print()
print('Sending the {:.2f} {} from {} to {}'.format(total_xrp_bought, transport, source_ex.name, dest_ex.name))
print()

xrp_to_sell = total_xrp_bought
dest_amount = 0.0

print("Getting order book for {} from {}".format(dest_pair, dest_ex.name))
for price,amount in dest_orderbook['bids']:

    sold_amount = min(xrp_to_sell, amount)
    dest_amount += sold_amount * price
    xrp_to_sell -= sold_amount

    print('- Sold {:.2f} {} @ {:.4f}'.format(sold_amount, transport, price))

    if xrp_to_sell <= 0:
        break

try:
    sell_fee = dest_markets[dest_pair]['taker'] * dest_amount
except KeyError: # Bitso doesn't have fees in ccxt API
    sell_fee = (0.65/100) * dest_amount
print('Total dest amount: {:.2f} {}'.format(dest_amount, dest_cur))
print('Sell trade fee: {:.2f} {}'.format(sell_fee, dest_cur))
dest_amount -= sell_fee
print('Net: {:.2f} {}'.format(dest_amount, dest_cur))


    
    
    
        
    
    
