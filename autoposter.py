import vk_api
import requests
import time
from PIL import Image

LOGIN='+7000000000'       #Your VK login
PASSWORD='YourPassWord' #Your VK Password
GROUP_ID= -11111111         #Group ID (Should be negative)
IMAGE_SIZE=600              #Size of final image (IMAGE_SIZE * IMAGE_SIZE)
IMAGE_NAME='cat'            #Name of final image starts with IMAGE_NAME
HEADERS={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'} #Headers

def logger(n=-1):
    #Logger values
    dict = ["Authentificated","Got an API","Starting to process image","Sleep for 5 seconds","Woke up","Image requested","Image written to file","Image uploaded","Sleep for 3 hours","Nothing to log"]
    print('['+time.asctime()+']: '+ dict[n])

def scrapper(g=0,sizeX=IMAGE_SIZE,sizeY=IMAGE_SIZE,url='https://thiscatdoesnotexist.com/'):
    img_data = requests.get(url, headers=HEADERS).content
    logger(5) #Image requested
    with open(IMAGE_NAME+str(g)+".PNG", 'wb') as handler:
        handler.write(img_data)
    size = sizeX, sizeY
    im = Image.open(IMAGE_NAME+str(g)+".PNG")
    im_resized = im.resize(size, Image.ANTIALIAS)
    im_resized.save(IMAGE_NAME+str(g)+".PNG", "PNG")
    logger(6) #Image written to file

def auth_handler():
    key = input("Enter authentification code: ")
    remember_device = True
    return key, remember_device

vk_session = vk_api.VkApi(LOGIN, PASSWORD, auth_handler=auth_handler)
vk_session.auth()
logger(0) #Authentificated
vk = vk_session.get_api()
logger(1) #Got an API

upload = vk_api.VkUpload(vk_session)

x=0
while True:
    logger(2) #Starting to process image
    logger(3) #Sleep for 5 seconds
    time.sleep(5)
    logger(4) #Woke up
    scrapper(x)
    upload.photo_profile(IMAGE_NAME+str(x)+'.PNG', owner_id=GROUP_ID, crop_x=IMAGE_SIZE, crop_y=IMAGE_SIZE, crop_width=IMAGE_SIZE)
    logger(7) #Image uploaded
    logger(8) #Sleep for 3 hours
    time.sleep(10800)
    logger(4) #Woke up
    x+=1
