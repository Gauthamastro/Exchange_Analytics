import shrimpy
import time

exchange = 'binance'
start_date = "2020-07-01"
end_date = "2020-08-01"
api_client = shrimpy.ShrimpyApiClient("", "")
trading_pairs = api_client.get_trading_pairs(exchange)
total_count = 0
for i in range(len(trading_pairs)):
    count = api_client.get_historical_count(
        'trade',
        exchange,
        trading_pairs[i]["baseTradingSymbol"],
        trading_pairs[i]["quoteTradingSymbol"],
        start_date + 'T01:00:00.000Z',
        end_date + 'T02:00:00.000Z')
    print("Progress: ", i + 1,
          "/" + str(len(trading_pairs)) + " Trade Pair Count: " + str(count['count']) + " - " + trading_pairs[i]["baseTradingSymbol"] + "/" +
          trading_pairs[i]["quoteTradingSymbol"] + " Total Trades: ",total_count)
    total_count = total_count + count['count'] 
    time.sleep(7)
print("Total Trades in one month: {}", total_count)
print("Average Trades per second: {}", float(total_count) / float((30 * 24 * 60 * 60)))
