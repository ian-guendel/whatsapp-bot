import pywhatkit as kit
import time
import time


# To schedule messages
# kit.sendwhatmsg('+50688138143',"Bot message")


# print('Starting to send the message...')
# # To send instant messages
try:
    # kit.sendwhatmsg_instantly('+50687133953',"Guapa",9,True,1)
    kit.sendwhats_image('+50687133953',"/Users/ianguendel/Documents/GitHub/whatsapp-bot/gif1.gif","Los acordes... :P",10,True,2)
    print('message send!')

except Exception as ex:
    print(ex)

