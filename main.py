
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import time



try:
    # url = 'https://drive.google.com/drive/folders/1vc6RS2dYWuu8c6RZFkRpWXR4Hj4cwsiX?usp=sharing'
    url = 'https://drive.google.com/drive/folders/1vc6RS2dYWuu8c6RZFkRpWXR4Hj4cwsiX?usp=sharing'
    status = requests.get(url)
    sts = status.status_code
    code = 404
    browser = webdriver.Chrome('D:\whatsapp\chromedriver')
    browser.get('https://web.whatsapp.com')
except:
    print('connect to  the internet')
    print('connect to  the internet')

time.sleep(2)


def search():
    try:

        friend = input('Enter your friend name: ')
      
        searchbox = browser.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
        searchbox.send_keys(friend)
        searchbox.send_keys(Keys.ENTER)

       
    except:
        print("friend is wrong!!!!!")





def send():
    # file1 = open("D:\whatsapp\Text.txt", "r")
    # text1 = file1.read()
    # text1 = text1.replace('\n' , '$')

    file1 = open("D:\whatsapp\Text.txt", "r")
    text1 = file1.readlines()
    text2 =[]




    messagebox = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')


    # count = 0
    # for line in text1:
    #
    #     if line == '$':
    #         messagebox.send_keys(Keys.SHIFT, Keys.ENTER)
    #         count=count+1
    #         if count==20:
    #             count=0
    #             messagebox.send_keys(Keys.ENTER)
    #
    #
    #
    #     else:
    #
    #         messagebox.send_keys(line)
    for line in text1:
        text2.append(line.replace(' ', ''))
        text2.append(line.replace('\n', ''))

    messagebox.send_keys(text2)

    messagebox.send_keys(Keys.ENTER)
    file1.close()

def main():
    if sts == code:
        print('jarvis server is offline')
    else:

        search()

        yes = input('Are you conform to send ...?  [y] :')
        if 'y' == yes:
            send()
            print("Done......................")
            main()
        else:
            main()
    # file1 = open("D:\whatsapp\Text.txt", "r")
    # text1 = file1.readlines( )
    #
    # for line in text1:
    #     text2 = line.replace('\n', ' ')
    #
    #     print (text2)


main()












    
    
 
    

