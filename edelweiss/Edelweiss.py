import json
from requests import Session

class Edelweiss:
    '''
    a = Edelweiss () 
    d= a.volumebuzzers()
    d
    '''
    base_url = "https://ewmw.edelweiss.in/api/Market"
        
    _routes = {
            "deep_dive": "/MarketsModule/DeepDive",
            "option_chain":"/optionchaindetails",
            "volumebuzzers":"/volumebuzzers",
            "symbol_expiry":"/Process/GetSymbolExpiry",
            "market_indices":"/MarketsModule/MarketsIndices",
            "market_overview":"/MarketsModule/Overview",
            "market_overview":"/MarketsModule/Overview",
            "fii_dii":"/MarketsModule/FIIDII",
            "symbol_expiry":"/Process/GetSymbolExpiry",
            "index_expiry":"/Process/GetBankNiftySymbolExpiry",
            "most_liquid_derivative":"/Process/GetMostLiquidFuturesOrOptions",
            "top_gainers_Losers":"/Process/GetDerivativesTopGainersOrLosers",
            "advance_decline_nse":"/advdec/NSE",
            "advance_decline_bse":"/advdec/BSE",
            "events":"/MarketsModule/Events",
        
           
    }
    
    def __init__(self):
        self.s = Session()

    def get_(self, route, payload={}):
        url = self.base_url + self._routes[route]
        r = self.s.get(url, params=payload)
        return json.loads(r.json())
    def post_(self, route, payload={}):
        url = self.base_url + self._routes[route]
        r = self.s.post(url, data=payload)
        return json.loads(r.json())
    def get_without_json(self, route, payload={}):
        url = self.base_url + self._routes[route]
        r = self.s.get(url, params=payload)
        return r.json()
    def post_without_json(self, route, payload={}):
        url = self.base_url + self._routes[route]
        r = self.s.post(url, data=payload)
        return r.json()
    
    def deep_dive(self, activity="active"):
        ''' activity => ActiveStocks/TopGainers/TopLosers '''
        value={"active":"ActiveStocks","gainer":"TopGainers","loser":'TopLosers'}
        return self.get_("deep_dive")['JsonData']#[value.get(activity)]
    
    def option_chain(self,expiry,der='OPTIDX',symbol="BANKNIFTY"):
        if symbol not in ["BANKNIFTY","NIFTY"]:
            der='OPTSTK'
        '''
        stocks=> {'exp': "25 Aug 2022", 'aTyp': "OPTSTK", 'uSym': symbol}
        index=> {'exp': "25 Aug 2022", 'aTyp': "OPTIDX", 'uSym': NIFTY}
        e.g.  a = Edelweiss () 
              d= a.option_chain("04 Aug 2022",symbol="NIFTY") 
              Defalut => BANKNIFTY
        '''   
        data = {'exp':expiry, 'aTyp': der, 'uSym': symbol}   
        return self.post_("option_chain",data)
    def most_liquid_derivative(self,expiry,der="fut"):
        '''a = Edelweiss() 
            d= a.most_liquid_derivative('25 Aug 2022',der='fut')'''
        value={"opt":"mLOpt","fut":'mLFut'}
        data = {'exp':expiry}   
        return self.post_("most_liquid_derivative",data)['JsonData']['response']['data'][value.get(der)]
    
    def top_gainers_Losers(self,expiry,der="opt"):
        '''a = Edelweiss() 
           d= a.top_gainers_Losers('25 Aug 2022',der='fut')'''
        value={"opt":"mLOpt","fut":'mLFut'}
        data = {'exp':expiry}   
        return self.post_("most_liquid_derivative",data)#['JsonData']['response']['data'][value.get(der)]
    
    def volumebuzzers(self):
        '''
        a = Edelweiss () 
        d= a.volumebuzzers()
        d
        '''   
        data = {'exp': "NSE", 'idx': "-44", 'ped': "FTD"} 
        return self.post_without_json("volumebuzzers",data)['data']['vBuzz']
    def market_indices(self):
        return self.get_("market_indices")
    def symbol_expiry(self):
        return self.get_("symbol_expiry")['JsonData']['response']['data']['validExpiry']
    def index_expiry(self):
        return self.get_("index_expiry")#['JsonData']['response']['data']['validExpiry']
    def fii_dii(self):
        return self.get_("fii_dii")['JsonData']
    def market_overview(self):
        return self.get_("market_overview")
    def global_indices(self):
        return self.get_("market_overview")['JsonData']['GMPIndices']
    def usd_cumo(self):
        return self.get_("market_overview")['JsonData']['OKIndices']
    def top_sector(self,exchange="Nse"):
        "exchange => NSE or BSE"
        exchange=exchange.capitalize()
        return self.get_("market_overview")['JsonData'][f'TopPerformingSectors{exchange}']
    def advance_decline_nse(self):
        return self.get_without_json("advance_decline_nse")['data']['aDList']
        # output is already in json format so we use without json function
    def advance_decline_bse(self):
        return self.get_without_json("advance_decline_bse")['data']['aDList']
        # output is already in json format so we use without json function
    def events(self):
        data = {}  
        return self.post_("events",data)
       

