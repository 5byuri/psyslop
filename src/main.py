import session 
import fetchData
import os


url = "youtube.com"

if __name__ == "__main__":

    if os.path.isfile("saved_cookies/token.txt"):
        fetchData.youtubeFetch()
    else:
        session.createToken()

    