def invalidTokenCheck():
    try:   
        with open(file="saved_cookies/token.txt", mode = "r") as file:
            assert file.read() != "[]" 
            
    except AssertionError as msg:
        print("Token was saved falsely, please delete saved_cookies folder and run main.py again")
        exit()


    

        
