from django.shortcuts import render,HttpResponse
from edelweiss.Edelweiss import Edelweiss
from topper.models import InsertSymbols
from topper.forms import DropdownForm
import csv as CV
import time
# Create your views here.
# def home(request):
#     form = DropdownForm()
#     symbols = InsertSymbols.objects.all()
#     selected ='None'
#     if request.method == 'POST':
#         form = DropdownForm(request.POST)

#         if form.is_valid():
#             selected = DropdownForm.cleaned_data['select_box']
#             return render(request,"index.html")
#     print("selected:::",selected)
    
    # return render(request,"index.html",{'data':symbols,'selected':selected})
# def home(request):  
#     sym =InsertSymbols.objects.all() 
#     return render (request,'index3.html',{'data':sym})
def home(request): 
    sym =InsertSymbols.objects.all()
    sel ="HDFCBANK"
    if request.method == 'POST':
        sel = request.POST['select_box']
    return render (request,'index.html',{'data':sym,'sel':sel})

def csv(request):
    path = r'C:\Users\harsh\Dropbox\Python\Django\Deployment\nse\edelweiss\media\CSV\preopen.csv'
    with open(path) as f:
        reader = CV.reader(f)
        for i, row in enumerate(reader):
            if i>9:
                symbol = InsertSymbols.objects.get_or_create(symbol=row[0],)
            
    return render (request,'excel.html')
    
  
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