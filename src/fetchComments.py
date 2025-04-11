import fetchVideos

from seleniumbase import SB

array = fetchVideos.youtubeFetch()
print(array)

with SB(uc=True, test=True, locale_code="en") as sb:
    for i in range(10):
        sb.sleep(3)

        
        sb.activate_cdp_mode(array[i])
        sb.sleep(3)
        print("not loaded")
        sb.load_cookies(name="saved_cookies/token.txt")
        print("loaded")
        sb.sleep(3)
        print("click reject")
        sb.load_cookies(name="saved_cookies/token.txt")
        sb.sleep(3)
        print("should work")
        sb.load_cookies(name="saved_cookies/token.txt")
        sb.load_cookies(name="saved_cookies/token.txt")
        sb.load_cookies(name="saved_cookies/token.txt")
        sb.load_cookies(name="saved_cookies/token.txt")
        sb.load_cookies(name="saved_cookies/token.txt")
        sb.load_cookies(name="saved_cookies/token.txt")
        sb.load_cookies(name="saved_cookies/token.txt")
        sb.load_cookies(name="saved_cookies/token.txt")
        sb.load_cookies(name="saved_cookies/token.txt")
        sb.load_cookies(name="saved_cookies/token.txt")
        sb.load_cookies(name="saved_cookies/token.txt")

        sb.sleep(3)

        print("loaded cookie")
        # sb.scroll_to_bottom("div#icon-label")
        sb.scroll_to("div#icon-label")
        sb.click("div#icon-label")
        sb.click("div#item-with-badge div")
        #sb.slow_scroll_to("div#icon-label")
        # sb.slow_scroll_to_element("div#icon-label")



        sb.sleep(10)



# with SB(uc=True, test=True, locale_code="en") as sb:
#     for i in range(10):
#         sb.load_cookies(name="saved_cookies/token.txt")
#         sb.activate_cdp_mode(fetchVideos.youtubeFetch()[i])
#         sb.sleep(10)
