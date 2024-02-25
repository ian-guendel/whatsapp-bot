import pywhatkit as kit
import time
total_messages = range(4)
phone = "phone_number"
group_id = "group_id"
image_path = "image_local_path"

try:
    for msg in total_messages:
        kit.sendwhats_image(group_id,image_path,"Ya esta el video!",10,True,1)
        print(f'Message {str(msg)} of {str(5)}')
        time.sleep(2)
except Exception as ex:
    print(ex)

