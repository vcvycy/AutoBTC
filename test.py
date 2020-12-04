# from huobi_api.huobi import *
import sys
from utils import *
sys.path.append("./huobi_api")
from huobi.client.generic import *
from huobi.client.market import *
def test_generic_client():
    generic_client = GenericClient()
    ts = generic_client.get_exchange_timestamp()
    print(ts)

def test_market_client():  # Create the market client instance and get the latest btcusdt‘s candlestick
    market_client = MarketClient()
    list_obj = market_client.get_candlestick("btcusdt", CandlestickInterval.MIN5, 20)
    print(len(list_obj))
    # LogInfo.output_list(list_obj)
    # print(type(list_obj[0]))
    # for item in list_obj:
    #     print(ts2str(item.id))

if __name__ == "__main__":
    # test_generic_client()
    test_market_client()