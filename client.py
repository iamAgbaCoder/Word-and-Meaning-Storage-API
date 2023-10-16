"""
    this program/script is only added or written to test and consume
    our Dictionary FastAPI.. Softwares like Postman can used instead of this piece of 
    code to test out this API and access more functionalities.
    
    Therefore, this pratice is not the best way to test out APIs!
    Also, the JSON file that conatains words and their meaning aren't complete i.e doesn't 
    contain all words in English. it's just created to test out this software. You can get your own
    word bank or data from a reliable source!
    
    Dont forget to follow and leave a star!
    Thank you!

"""
    
import requests

def searchAPI():
    print()
    word = input("Enter a word: ").lower() # prompts user for a word
    api_url = f"http://127.0.0.1:8000/word-search?q={word.lower()}" # API url - "127.0.0.1:8000" is used to test on loacl machine
    
    # fetchs data from HTTP Response
    response = requests.get(api_url)
    data = response.json()
    
    # print(response.json(), response.status_code, response.headers)  
    for key in data:
        print(f"{key} - {data[key]}")
        
        
def addWordAPI():
    print()
    
    word = input("[PROMPT] ==> Type word: ").lower() # coverts string to all lowercase
    meaning = input("[PROMPT] ==> Enter word meaning: ")
     
    content = {"word": word.lower(), "meaning": meaning }
    
    api_url = f"http://127.0.0.1:8000/add-word/" # API url - "127.0.0.1:8000" is used to test on loacl machine
    
    try:     
        # sends POST request to add word and meaning
        response = requests.post(api_url, json=content)
        
        # check HTTP response status code
        if response.status_code == 200:
            print()
            print("[SUCCESS] ==> Word and meaning added to Database successfully")
            
        elif response.status_code == 201:
            print("[INFO] ==> Word already exist in Database")
            
        else:
            print(f"[ERROR] ==> Failed to add word and meaning. Status code: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] ==> Oops!. An error occured: {e}")
        

def removeAPI():
    pass
        

def main():
    print()
    print("WARNING: This program/script is only added or written to test and consume our Dictionary FastAPI.. Softwares like Postman can used instead of this piece of code to test out this API and access more functionalities.\n Also, the JSON file that conatains words and their meaning aren't complete i.e doesn't contain all words in English. it's just created to test out this software. You can get your own word bank or data from a reliable source! \nTherefore, this pratice is not the best way to test out APIs!")
    print("\n")
    print("[1]. Search for a word")
    print("[2]. Add a word")
    print("[3]. delete a word")
    
    try:
        res = int(input("Choose option: "))
    
        if res == 1:
            searchAPI()
        elif res == 2:
            addWordAPI()
        elif res ==3:
            removeAPI()
        else:
            print("Invalid Response!. Rerun program and try again")
            
    except ValueError as e:
        print(f"[ERROR] You entered an Alphabet/AlphaNumeric character. {e}")


if __name__  == "__main__":
    main()