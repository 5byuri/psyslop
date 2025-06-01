import fetchVideos

from seleniumbase import SB
import main
import chatbot

def spreadMessage(video_links : list):
    with SB(uc=True, test=True, locale_code="en") as sb:
        sb.activate_cdp_mode(main.url)
        sb.open(main.url)
        sb.load_cookies(name="saved_cookies/token.txt") 
        print("cookie loaded")
        
        for j in range(len(video_links)):
            sb.open(video_links[j])     
            sb.slow_scroll_to_element('ytd-continuation-item-renderer')
            comment_elements = sb.find_elements('//yt-attributed-string[@id="content-text"]', by="xpath")
            replyElements = sb.find_elements('button[aria-label="Antworten"]')
            

            fusionElements : list = []
            for i in range(len(comment_elements)):
                fusionElements.append({
                    "commentElement": comment_elements[i],
                    "replyElement": replyElements[i]
                })


            for idx,element in enumerate(fusionElements):
                # element.is_displayed()
                x = element["replyElement"]
                x.click()
                cancelElement = sb.find_element('button[aria-label="Abbrechen"]')
                
                sb.press_keys('div#contenteditable-root', f"{chatbot.aiResponse(comment_elements[idx].text)}")
                cancelElement.click()

                # sb.uc_click('//ytd-button-renderer[@id="submit-button"]')



            # for i in range(10):
            #     sb.sleep(3)
            #     print(replyElements[i].id)
            #     print("breakpoint")
            #     sb.click(replyElements[i])
            #     #sb.uc_click(f'button[@id="{replyElements[i].id}"]')
            #     sb.press_keys('div#contenteditable-root', f"{chatbot.aiResponse(comment_elements[i].text)}")
            #     #sb.uc_click('//ytd-button-renderer[@id="submit-button"]')
                
        

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


