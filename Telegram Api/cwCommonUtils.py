


#usar parametro pattern con regEx
def GetItemAmountFromStock(item_name, stock):
    if item_name.lower() in stock.lower():
        arr = stock.lower().split(item_name.lower() + ' (')
        return arr[1].split(')', 1)[0]
    return 0

def GetRemoveHashFromExchange(item_name, exchange):
    iteml = item_name.lower()
    exl = exchange.lower()
    if iteml in exl:
        return exl.split(iteml)[1].split('] ')[1].split(' ')[0]
    return None

def GetItemAmountFromExchange(item_name, exchange):
    iteml = item_name.lower()
    exl = exchange.lower()
    if iteml in exl:
        return int(exl.split(iteml)[1].split(' x')[0])
    return 0