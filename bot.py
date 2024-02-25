import pywhatkit as kit
import time
total_messages = range(4)
phone = ""
group_id = ""
image_path = ""
image_caption = ""

try:
    for msg in total_messages:
        kit.sendwhats_image(phone,image_path,image_caption,10,True,5)
        print(f'Message {str(msg)} of {str(5)}')
        time.sleep(2)
except Exception as ex:

    print(ex)

