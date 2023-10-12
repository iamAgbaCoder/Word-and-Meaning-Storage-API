from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

import json

app = FastAPI()

# data = json.loads(open("simple_english_dictionary.json", "r")) #
with open("simple_english_dictionary.json", "r") as json_file:
    data = json.load(json_file)
    

class Word(BaseModel):
    word: str
    meaning: str


@app.get("/")
async def home():
    # returns every word and its meaning in key-value format
	return data


'''
    this API wordSearch() gets word search query
    using database query i.e "?word=help". wordSearch() receives users search query,
    validates it by checking if such word exists and then return a HTTP response with 
    data(word search meaning) or error messages
'''
@app.get("/word-search")
async def wordSearch(*, q: Optional[str] = None):
    # loop through words
    for word in data:
        # validate word search
        if q in data:
            print(q)
            # concantenate word and it meaning into a dict/json format
            x = {q : data[q]}
            # returns data 
            return x
        else:
            return {"Oops": "Word not found!"}


@app.post("/add-word/")
async def addWord(word_item: dict):
    
    # parsing json response
    word = word_item["word"]
    meaning = word_item["meaning"]
    
    # checks if word exists 
    if word_item["word"] in data:
        return {"INFO": "Word already exist in Database!"}
    
    # save word and meaning to DB
    data[word] = meaning
    return {"INFO": "Word added to Database!"}


    