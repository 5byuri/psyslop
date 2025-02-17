import pickle
from seleniumbase import SB
def youtubeFetch():

    with SB(uc=True, test=True, locale_code="en") as sb:
        url = "youtube.com"
        sb.activate_cdp_mode(url)
        sb.uc_click('span:contains("Accept all")', reconnect_time=4)


        sb.save_cookies(name="cookies.txt")




youtubeFetch()


