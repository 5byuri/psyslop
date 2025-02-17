import os
import pickle

from seleniumbase import SB
url = "youtube.com"


def createToken():

    with SB(uc=True, test=True, locale_code="en") as sb:
        
        sb.activate_cdp_mode(url)
        sb.uc_gui_click_captcha()

        
        #On Linux, you can either set 'export SB_MAIL="string"' in your terminal for quick testing
        #if used permanently then copy into your shell ./{shell}rc config! !
        #Your IDE debugger might not find the environ, for that create a .env in this repo and add values there 

        email_input = os.environ.get("SB_MAIL") 
        password_input = os.environ.get("SB_PW")

        sb.uc_click('span:contains("Reject all")', reconnect_time=4)
        sb.uc_click('span:contains("Sign in")', reconnect_time=4)
        sb.press_keys("#identifierId",email_input)
        sb.assert_element('#identifierId')
        sb.uc_click('span:contains("Next")', reconnect_time=4)
        sb.press_keys('input[aria-label="Enter your password"]', password_input)
        sb.uc_click('span:contains("Next")', reconnect_time=4)
        
        print("debug")
        sb.sleep(2)

        sb.save_cookies(name="token.txt")

def loginYoutube():
    with SB(uc=True, test=True, locale_code="en") as sb:
       sb.activate_cdp_mode(url)
       sb.open(url)
       sb.load_cookies(name="saved_cookies/token.txt")
       sb.open(url)
       print("test")




def startUp():
    if os.path.isfile("saved_cookies/token.txt"):
        loginYoutube()
    else:
        createToken()


