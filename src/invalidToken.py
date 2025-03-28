def invalidTokenCheck(pathToToken):
    try:   
        with open(file=f"{pathToToken}", mode = "r") as file:
            assert file.read() != "[]" 
            return True
    except AssertionError  as msg:
        print("Token was saved falsely, please delete saved_cookies folder and run main.py again")
        return False


    

        
