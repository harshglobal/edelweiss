from django.shortcuts import render,HttpResponse
from edelweiss.Edelweiss import Edelweiss
import time
# Create your views here.
def home(request):
    return render(request,"advancedecline.html")

def indices(request):
    q=Edelweiss()
    oc = q.market_indices()
    nse_index = oc['JsonData']['KI']['NSE'] +  oc['JsonData']['SI']['NSE'] 
    bse_index = oc['JsonData']['KI']['BSE'] +  oc['JsonData']['SI']['BSE']    
    
    index_data = {'nse_index':nse_index, 'bse_index':bse_index}
    return render(request,'indices.html',index_data)

def globals(request):
    q=Edelweiss()
    oc = q.market_indices()
    eur_index = oc['JsonData']['GI']['Europe'] + oc['JsonData']['GI']['America']      
    asia_index = oc['JsonData']['GI']['Asia']     
    data = {'eur_index':eur_index,'asia_index':asia_index}
    return render(request,'globals.html',data)

def advdec(request):
    q=Edelweiss()
    adv_nse = q.advance_decline_nse()
    time.sleep(0.5)
    adv_bse = q.advance_decline_bse()     
    data = {'adv_nse':adv_nse,'adv_bse':adv_bse}
    return render(request,'advancedecline.html',data)

def topmost(request):
    q=Edelweiss()
    d = q.deep_dive()
    active_stocks=d['ActiveStocks'] 
    gainers_stocks=d['TopGainers']     
    losers_stocks=d['TopLosers']     

    data = {'active_stocks':active_stocks,'gainers_stocks':gainers_stocks,'losers_stocks':losers_stocks}
    return render(request,'topmost.html',data)