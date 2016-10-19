# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def long_short_call (K, preC ,interval ):
    ST = np.arange(K - interval , K + interval)
    pf_buyCall = np.maximum(ST-K, 0) - preC
    pf_sellCall = - pf_buyCall
    plt.plot()
    plt.plot(ST,pf_buyCall)
    plt.plot(ST,pf_sellCall)
    plt.axhline(y=0,color="black" )
    plt.axvline(x=K+preC,color="black" )
    
long_short_call(9100,179,500)


def long_short_put (K, preP ,interval ):
    ST = np.arange(K - interval , K + interval)
    pf_buyCall = np.maximum(K - ST, 0) - preP
    pf_sellCall = -pf_buyCall
    plt.plot(ST,pf_buyCall)
    plt.plot(ST,pf_sellCall)
    plt.axhline(y=0,color="black" )
    plt.axvline(x=K-preP,color="black" )
    
long_short_put(9100,179,500)


#2 : bull strategy
K = 9100
buy_K = 9000
sell_K = 9300
interval= 500
pre = 180
ST = np.arange(K - interval , K + interval )
pf_buyCall = np.maximum(ST - buy_K , 0) - pre
pf_sellCall = -(np.maximum(ST - sell_K,0) - pre)
pf = pf_buyCall + pf_sellCall
plt.plot(ST,pf)
plt.plot(ST,pf_buyCall)
plt.plot(ST,pf_sellCall)
plt.axhline(y=0,color="black" )
