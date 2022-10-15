from gtts import gTTS
import os

msg = 'whatsapp virus created by Omotosho Gbolahan Hammed Facebook Omotosho Gbolahan Whatsapp: 08022648626 Instagram lord of hacker This is a whatsapp virus for both IOS and Android This virus can crash your victim whatsapp Disclaimer Do not use this script for revenge or to harm anyone I wont be responsible for any illegal or malicious use NB This whatsapp virus is very dangerous, so use it wisely For Educational Purpose only Copy full text and send to victim copy all the full text for it to work perfectly'
language = 'en'

obj=gTTS(text=msg, lang=language, slow=false)

obj.save('virus.mp4')

os.system('mpg321 virus.mp4')
