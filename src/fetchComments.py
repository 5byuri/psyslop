import fetchVideos

from seleniumbase import SB

array = fetchVideos.youtubeFetch()
print(array)

with SB(uc=True, test=True, locale_code="en") as sb:
    sb.activate_cdp_mode("youtube.com")
    sb.load_cookies(name="saved_cookies/token.txt")
    for i in range(10):
        sb.activate_cdp_mode(array[i])

        sb.sleep(6)
        sb.slow_scroll_to_element('ytd-continuation-item-renderer')
        print("scrolled.")
        sb.sleep(6)
        # sb.uc_click('span:contains("Reject all")', reconnect_time=4)
        # sb.scroll_to_bottom("div#icon-label")
        # sb.scroll_to("#ghost-cards")
        # sb.click("div#icon-label")
        # sb.click("div#item-with-badge div")
        # sb.sleep(30)
        # print("timer start 6 seconds to scroll down")
        # sb.click("div#icon-label")
        # sb.click("div#item-with-badge div")


        sb.sleep(5)
        #sb.slow_scroll_to("div#icon-label")
        # sb.slow_scroll_to_element("div#icon-label")






# with SB(uc=True, test=True, locale_code="en") as sb:
#     for i in range(10):
#         sb.load_cookies(name="saved_cookies/token.txt")
#         sb.activate_cdp_mode(fetchVideos.youtubeFetch()[i])
#         sb.sleep(10)


