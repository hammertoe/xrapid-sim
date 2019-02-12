# xrapid-sim
A simulator to simulate the costs of an xRapid transfer based on current prices

## Install

```
# virtualenv . -python=python3
# . bin/activate
# pip install -r requirements.txt
```

## Running

```
$ python xrapid-sim.py 4000 braziliex BRL bitso MXN 
Getting order book for XRP/BRL from Braziliex
+ Bought 515.37 XRP @ 1.1400
+ Bought 1571.54 XRP @ 1.1600
+ Bought 1358.55 XRP @ 1.1700
Total Bought: 3445.45 XRP
Buy trade fee: 17.23 XRP
Net: 3428.22 XRP

Sending the 3428.22 XRP from Braziliex to Bitso

Getting order book for XRP/MXN from Bitso
- Sold 3428.22 XRP @ 5.6500
Total dest amount: 19369.46 MXN
Sell trade fee: 125.90 MXN
Net: 19243.56 MXN
```

You can specify an alternate transport currency too, eg:

```
$ python xrapid-sim.py 4000000 indodax IDR bitso MXN --transport BTC
Getting order book for BTC/IDR from INDODAX
+ Bought 0.08 BTC @ 50340000.0000
Total Bought: 0.08 BTC
Buy trade fee: 0.00 BTC
Net: 0.08 BTC

Sending the 0.08 BTC from INDODAX to Bitso

Getting order book for BTC/MXN from Bitso
- Sold 0.00 BTC @ 67880.1200
- Sold 0.00 BTC @ 67879.7900
- Sold 0.07 BTC @ 67877.1900
Total dest amount: 5377.34 MXN
Sell trade fee: 34.95 MXN
Net: 5342.38 MXN
```