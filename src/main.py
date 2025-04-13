import session 
import fetchVideos
import os
from chatbot import aiResponse

url = "youtube.com"

if __name__ == "__main__":

    if os.path.isfile("saved_cookies/token.txt"):
        fetchVideos.youtubeFetch()
    else:
        session.createToken()
    aiResponse()