import fetchVideos

from seleniumbase import SB
import main
import chatbot





def spreadMessage(video_links):
    with SB(uc=True, test=True, locale_code="en") as sb:
        sb.activate_cdp_mode(main.url)
        sb.open(main.url)
        sb.load_cookies(name="saved_cookies/token.txt") 
        sb.open(main.url)
        with open(file="saved_cookies/token.txt", mode= "r") as file:
            print(file.read())
        sb.activate_cdp_mode("youtube.com")
        sb.sleep(3)
        comment_elements = []
        for i in range(10):
            sb.activate_cdp_mode(video_links[i])
            sb.sleep(3)
            sb.slow_scroll_to_element('ytd-continuation-item-renderer')
            comment_elements = sb.find_elements('//yt-attributed-string[@id="content-text"]', by="xpath")

        sb.uc_click('button[aria-label="Antworten"] yt-touch-feedback-shape div:nth-of-type(2)')
        sb.press_keys('div#contenteditable-root', f"{chatbot.aiResponse(comment_elements)[0]}")
        # # sb.uc_click('//*[@id="submit-button"]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]')
        # sb.uc_click('button[aria-label="Antworten"]')
        # sb.sleep(10)


        # for element in comment_elements:
        #     print(element.text)

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


