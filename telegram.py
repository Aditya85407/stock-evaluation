import telegram
import apireds 

ellie = telegram.Bot(token=apireds.TELEGA_TOKEN)

def SendMessage(chatid = '961191888', message = 'Test Message'):
    ellie.sendMessage(chatid, message)
