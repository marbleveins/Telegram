


#usar parametro pattern con regEx
def GetItemAmountFromStock(item_name:str, stock):
    if item_name.lower() in stock.lower():
        arr = stock.lower().split(item_name.lower() + ' (')
        return int(arr[1].split(')', 1)[0])
    return 0

def GetRemoveHashFromExchange(item_name:str, exchange):
    iteml = item_name.lower()
    exl = exchange.lower()
    if iteml in exl:
        return exl.split(iteml)[1].split('] ')[1].split('\n')[0]
    return None

def GetItemAmountFromExchange(item_name:str, exchange):
    iteml = item_name.lower()
    exl = exchange.lower()
    if iteml in exl:
        return int(exl.split(iteml + '\n')[1].split(' x')[0])
    return 0