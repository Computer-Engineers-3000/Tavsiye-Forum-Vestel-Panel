from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
page_number = 1
messages_text = []
cevap = 1
f = open("Mytext.txt", "w",encoding="utf-8")

while page_number <= 854:

    browser.get("https://tavsiyeforumu.com/konu/vestel-panel-bilgi-hatti.449/page-"+str(page_number))
    messages = browser.find_elements(By.CLASS_NAME, "bbWrapper")
    alintilar = browser.find_elements(By.CLASS_NAME,"bbCodeBlock-content")

    f.write("SAYFA-"+str(page_number)+"\n"+"\n"+"\n")


    for i in messages:
        try:
            f.write("Cevap-"+str(cevap)+"\n"+i.text+"\n")
            f.write("\n---------------------------------------------------------------------------\n")

        except:
            pass

        cevap += 1


    page_number+=1





