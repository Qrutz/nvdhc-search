import yfinance as yf
from yfinance import ticker


# class CurrentHoldings:
#     def __init__(self, Ticker, earnings, financials, stockinfo):
#         self.Ticker = Ticker
#         self.earnings = earnings
#         self.financials = financials
#         self.stockinfo = stockinfo

#     def getData(self):
#         print(self.Ticker)


class CurrentHoldings:
    def __init__(self, PLTR, AAPL, NOS, TSLA):
        self.PLTR = PLTR
        self.AAPL = AAPL
        self.NOS = NOS
        self.TSLA = TSLA

    def getData(self):
        print(self.PLTR)
        print(self.AAPL)
        print(self.NOS)
        print(self.TSLA)


PLTRR = yf.Ticker("PLTR")
PLTR_H = PLTRR.history(period="max")

AAPLL = yf.Ticker("AAPL")
AAPL_H = AAPLL.history(period="max")

NOSS = yf.Ticker("NOS.OL")
NOS_H = NOSS.history(period="max")

TSLAA = yf.Ticker("TSLA")
TSLA_H = TSLAA.history(period="max")


x = CurrentHoldings(PLTR_H, AAPL_H, NOS_H, TSLA_H)

x.getData()
