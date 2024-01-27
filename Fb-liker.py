
import os,random

try:
    import requests
except:
    os.system('pip install requests')
##############################################################
def LIKES(ups,l):
    for h in range(500):
        if 1==1:
            n=random.randint(4,999999999)
            H={
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Encoding":"gzip, deflate, br",
                "Accept-Language":"en-US,en;q=0.5",
                "Connection": "keep-alive",
                "Content-Length": "376",
                "Content-Type": "application/x-www-form-urlencoded",
                "Cookie": f"_ga_ZPJZ7N0W5H=GS1.1.1702051184.75.1.1702053493.0.0.0; _ga=GA1.1.1757472153.1698914586; dom3ic8zudi28v8lr6fgphwffqoz0j6c=41520917-6e38-4a20-8ca7-753736477797%3A3%3A1; sb_main_3b26b900e2ca51bd9d1f99ba0f02f187=1; sb_count_3b26b900e2ca51bd9d1f99ba0f02f187=5; pp_main_62e5d1f5af7906bc73246c2a32f4ea31=1; pp_sub_62e5d1f5af7906bc73246c2a32f4ea31=4; PHPSESSID=4re8gaahha2be0v0vpehihgela; access_token=EAAAAUaZA8jlABO7l6VW6vuLpnD2NpssC4zetKaR1KFoJOU6owrjnXyJz8sSJ0QhBZCZApLKWKL3VrmTGtHDZBuOpPMwRouHCjVRbTXgm1kWSfazE3SjWZBCtYnZAXuOWzZA8bTZBVzycmfhtCOFW0DHi52d8racoGuwf9LU8aA1quwF4yp9XBknv4lYhdrdXSPENNSZBy16jGoQZDZD; user_id={n}; session_key=5.Jrjn0UBp4aCLAw.1699107057.7-61552765178248",
                "Host": "machine-likers.com",
                "Origin": "https://machine-likers.com",
                "Referer": "https://machine-likers.com/autoliker.php",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "TE": "trailers",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0"
            }

            D={
                "id":f"{ups}",
                "token":"EAAAAUaZA8jlABO7l6VW6vuLpnD2NpssC4zetKaR1KFoJOU6owrjnXyJz8sSJ0QhBZCZApLKWKL3VrmTGtHDZBuOpPMwRouHCjVRbTXgm1kWSfazE3SjWZBCtYnZAXuOWzZA8bTZBVzycmfhtCOFW0DHi52d8racoGuwf9LU8aA1quwF4yp9XBknv4lYhdrdXSPENNSZBy16jGoQZDZD"
            }

            r=requests.post(url="https://machine-likers.com/autoliker.php",headers=H,data=D)
            l=l+10
            print(f"[+] done! likes sent {l}",end="\r")

        else:
            pass
############################################################################

def COMONET(ucm,cm,l):
    for o in range(500):
        if 1==1:
            ra=random.randint(4,999999999)
            HE={
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Encoding":"gzip, deflate, br",
                "Accept-Language":"en-US,en;q=0.5",
                "Connection": "keep-alive",
                "Content-Length": "376",
                "Content-Type": "application/x-www-form-urlencoded",
                "Cookie": f"_ga_ZPJZ7N0W5H=GS1.1.1702051184.75.1.1702053493.0.0.0; _ga=GA1.1.1757472153.1698914586; dom3ic8zudi28v8lr6fgphwffqoz0j6c=41520917-6e38-4a20-8ca7-753736477797%3A3%3A1; sb_main_3b26b900e2ca51bd9d1f99ba0f02f187=1; sb_count_3b26b900e2ca51bd9d1f99ba0f02f187=5; pp_main_62e5d1f5af7906bc73246c2a32f4ea31=1; pp_sub_62e5d1f5af7906bc73246c2a32f4ea31=4; PHPSESSID=4re8gaahha2be0v0vpehihgela; access_token=EAAAAUaZA8jlABO7l6VW6vuLpnD2NpssC4zetKaR1KFoJOU6owrjnXyJz8sSJ0QhBZCZApLKWKL3VrmTGtHDZBuOpPMwRouHCjVRbTXgm1kWSfazE3SjWZBCtYnZAXuOWzZA8bTZBVzycmfhtCOFW0DHi52d8racoGuwf9LU8aA1quwF4yp9XBknv4lYhdrdXSPENNSZBy16jGoQZDZD; user_id={ra}; session_key=5.Jrjn0UBp4aCLAw.1699107057.7-61552765178248",
                "Host": "machine-likers.com",
                "Origin": "https://machine-likers.com",
                "Referer": "https://machine-likers.com/autoliker.php",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "TE": "trailers",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0"
            }

            DA={
                "id":f"{ucm}",
                "comment" :f"{cm}",
                "token":"EAAAAUaZA8jlABO7l6VW6vuLpnD2NpssC4zetKaR1KFoJOU6owrjnXyJz8sSJ0QhBZCZApLKWKL3VrmTGtHDZBuOpPMwRouHCjVRbTXgm1kWSfazE3SjWZBCtYnZAXuOWzZA8bTZBVzycmfhtCOFW0DHi52d8racoGuwf9LU8aA1quwF4yp9XBknv4lYhdrdXSPENNSZBy16jGoQZDZD"
            }

            r=requests.post(url="https://machine-likers.com/autocommenter.php",headers=HE,data=DA)
            l=l+10
            print(f"[+] done! commentes sent {l}",end="\r")

        else:
            pass
##########################################################################################################################
os.system('cls || clear')
print('''

             -------------------------------------------
                  F A C E B O O K    L I K E R
            -------------------------------------------
      
                           coder by: $Badreddine
                                     $INSTA: x_mtr

[01] FB likes
[02] FB comments

''')
l=0                                                                                                                                                                                                                                                                                                     
try:
    nu=int(input("[+]>_ :"))

    if nu ==1:
        ups=input("[+] URL_POST:")
        LIKES(ups,l)
    if nu ==2:
        ucm=input("[+] URL_POST:")
        cm=input("[+] tybe Comonte for sent:")
        COMONET(ucm,cm,l)


except ValueError:
    print("[!] try again!")
except ZeroDivisionError:
    print("[!] try again!")
