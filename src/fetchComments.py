import fetchVideos

from seleniumbase import SB

array = fetchVideos.youtubeFetch()
print(array)

with SB(uc=True, test=True, locale_code="en") as sb:
    sb.activate_cdp_mode("youtube.com")
    sb.load_cookies(name="saved_cookies/token.txt")
    for i in range(10):
        sb.activate_cdp_mode(array[i])
        sb.sleep(3)
        sb.slow_scroll_to_element('ytd-continuation-item-renderer')
        comment_elements = sb.find_elements('//yt-attributed-string[@id="content-text"]', by="xpath")
        for element in comment_elements:
            print(element.text)

        # comments_list = []
        # for video in comments_elements:
        #     comment = sb.get_beautiful_soup(comments_elements.get_html()).text.strip()
        #     print(comment)
        #     comments_list.append(comment)








# with SB(uc=True, test=True, locale_code="en") as sb:
#     for i in range(10):
#         sb.load_cookies(name="saved_cookies/token.txt")
#         sb.activate_cdp_mode(fetchVideos.youtubeFetch()[i])
#         sb.sleep(10)


