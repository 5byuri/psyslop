from seleniumbase import SB
import main
# https://github.com/seleniumbase/SeleniumBase/blob/9c1909e00731697b91ee6f2a53512e648878f13e/examples/cdp_mode/raw_easyjet.py#L36
# note to check all the element types


def youtubeFetch():

    with SB(uc=True, test=True, locale_code="en") as sb:
        sb.activate_cdp_mode(main.url)
        sb.open(main.url)
        sb.load_cookies(name="saved_cookies/token.txt")
        sb.open(main.url)
       
        #videos = sb.find_elements("style-scope ytd-rich-grid-renderer") 
        elem_list = sb.find_elements("div.contents")
        video = sb.find_elements("ytp-title-link yt-uix-sessionlink")
        
        print(video)
        print(elem_list)
        # Find all elements with href containing "/watch?v="
        watch_links = sb.driver.find_elements("//a[contains(@href, '/watch?v=')]")

def startUp():
    youtubeFetch()





