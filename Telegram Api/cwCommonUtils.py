
startingCall = ['agusbot','cw']

items = {
    "thread": "01",
    "stick": "02",
    "pelt": "03",
    "bone": "04",
    "coal": "05",
    "charcoal": "06",
    "powder": "07",
    "silver ore": "10",
    "magic stone": "13",
    "steel": "19",
    "bone powder": "21",
    "coke": "23",
    "purified powder": "24",
    "silver alloy": "25",
    "silver frame": "32"
}

commands = {
    "back": "⬅Back",
    "castle": "🏰Castle",
    "exchange": "⚖Exchange",
    "stock": "/stock",
    "me": "🏅Me",
    "/t": "/t"
}


def GetCommand(command):
    return commands.get(command)

def GetItemId(name):
    return items.get(name)

def GetItemName(id):
    ids = items.values()
    if id not in ids:
        return None
    for key, val in items.items():
        if val == id:
            return key

def GetItemIdFromCraftOrder(order, separator=' '):
    return order.split(separator)[0]
def GetItemQttyFromCraftOrder(order, separator=' '):
    return order.split(separator)[1]

#usar parametro pattern con regEx


def GetRequiredItemsFromCraftResult(craft_result, separator=' '):
    items = []
    if TestCraftResult(craft_result) == 'REQUIRED':
        item_list = craft_result.lower().split('required:\n ')[1].split('\n ')
        for item in item_list:
            item_qtty = item.split(' x ')[0]
            item_name = item.split(' x ')[1]
            items.extend([GetItemId(item_name) + separator + item_qtty])
    
    return items

def GetFirstItemFromCraftResult(craft_result, separator=' '):
    item = ''
    if TestCraftResult(craft_result) == 'REQUIRED':
        first_line = craft_result.lower().split('required:\n ')[1].split('\n ')[0]
        item_qtty = first_line.split(' x ')[0]
        item_name = first_line.split(' x ')[1]
        item = GetItemId(item_name) + separator + item_qtty
    return item

def GetFirstItemNameFromCraftResult(craft_result):
    first = ''
    if 'required:' in craft_result.lower():
        req_list = craft_result.lower().split('required:\n ')[1]
        first = req_list.split('\n')[0].split(' x ')[1]
    return first

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


def TestFollowingWords(words, text):
    head, *tail = words
    if isinstance(words, list) and len(words) > 0 and isinstance(text, str) and text:
        if head in text:
            if (len(tail) == 0):
                return True
            else:
                return TestFollowingWords(tail, text.split(head, 1)[1])
    else:
        return False


def TestCommandInText(words, text):
    return TestFollowingWords(words, text.lower())

def TestCraftResult(craft_result):
    result = ''
    if 'required:' in craft_result.lower():
        result = 'REQUIRED'
    elif 'crafted:' in craft_result.lower():
        result = 'CRAFTED'
    elif 'not enough mana' in craft_result.lower():
        result = 'MANA'
    return result

def GetItemFromOrder(order_items, word_before_item, separator = ' '):
    words = order_items.split(word_before_item + ' ')[1].split(' ')
    qtty = ''
    if words[0].isdigit():
        qtty = words[0]
        words.pop(0)
    elif words[len(words)-1].isdigit():
        qtty = words[len(words)-1]
        words.pop(len(words)-1)
    else:
        return ''
    
    item_name = ' '.join(words)
    item_id = GetItemId(item_name)
    if item_id is None:
        return ''
    else:
        return item_id + separator + qtty
