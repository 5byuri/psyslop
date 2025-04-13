from seleniumbase import SB
# https://github.com/seleniumbase/SeleniumBase/blob/9c1909e00731697b91ee6f2a53512e648878f13e/examples/cdp_mode/raw_easyjet.py#L36
# note to check all the element types
import main
from invalidToken import invalidTokenCheck


def youtubeFetch():

    with SB(uc=True, test=True, locale_code="en") as sb:
        sb.activate_cdp_mode(main.url)
        sb.open(main.url)
        
        if not invalidTokenCheck("saved_cookies/token.txt"):
            exit()
        try:
            sb.sleep(3)
            sb.load_cookies(name="saved_cookies/token.txt")
            with open(file="saved_cookies/token.txt", mode= "r") as file:
                print(file.read())
        except NameError:
            print("did not work")
            sb.sleep(3)
            sb.load_cookies(name="saved_cookies/token.txt")

        sb.open("https://www.youtube.com/feed/subscriptions")
        sb.sleep(3)


        sb.get_element('#video-title')  # id="video-title"

        for i in range(5):
            sb.sleep(1)
            sb.scroll_to_bottom()
        video_elements = sb.find_elements('a#video-title-link')
        video_links = []
        for video in video_elements:
            href = video.get_attribute("href")
            video_links.append(href)

        return video_links







