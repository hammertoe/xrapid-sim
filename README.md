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
