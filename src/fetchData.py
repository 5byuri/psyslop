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
            sb.load_cookies(name="saved_cookies/token.txt")
            with open(file="saved_cookies/token.txt", mode= "r") as file:
                print(file.read())
        except NameError:
            print("did not work")
            sb.sleep(3)
            sb.load_cookies(name="saved_cookies/token.txt")

        sb.open(main.url)
        sb.sleep(3)


        sb.get_element('#video-title')  # id="video-title"

        for i in range(20):
            sb.scroll_to_bottom()
        video_elements = sb.find_elements('a#video-title-link')
        video_links = []
        for video in video_elements:
            href = video.get_attribute("href")
            video_links.append(href)
            print(href)


        elem_list = sb.find_elements("div.contents")
        video = sb.find_elements("href")
        video = sb.find_elements("video-title-link")
        sb.sleep(100000000)

        print(video)
        print(elem_list)
        sb.sleep(3)

# yt-core-image yt-core-image--fill-parent-height yt-core-image--fill-parent-width yt-core-image--content-mode-scale-aspect-fill yt-core-image--loaded
        
        # Find all elements with href containing "  "
        # watch_links = sb.driver.find_elements("//a[contains(@href, '/watch?v=')]")
def startUp():
    youtubeFetch()





