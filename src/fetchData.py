import os
from seleniumbase import SB
def loginYoutube():
    with SB(uc=True, test=True, locale_code="en") as sb:
        url = "youtube.com"
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
        getVideos()

loginYoutube()


def comment():
    with SB(uc=True, test=True, locale_code="en") as sb:
        sb.activate_cdp_mode(url)



def getVideos(): #this part I copied from my old repo with selenium so it has to be updated for SeleniumBase
    with SB(uc=True, test=True, locale_code="en") as sb:
        videos = sb.find_elements(By.CLASS_NAME, "style-scope ytd-rich-grid-renderer") 
        elem_list = sb.find_elements(By.ID, "contents")

        video = sb.find_elements(By.CLASS_NAME, "ytp-title-link yt-uix-sessionlink")
        
        print(video)
        print(elem_list)

        # Find all elements with href containing "/watch?v="
        watch_links = sb.driver.find_elements(By.XPATH, "//a[contains(@href, '/watch?v=')]")