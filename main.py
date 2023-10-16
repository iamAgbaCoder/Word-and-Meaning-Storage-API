from fastapi import FastAPI, Path
from fastapi.responses import JSONResponse
from typing import Optional
from pydantic import BaseModel

import json

app = FastAPI()

with open("simple_english_dictionary.json", "r+") as json_file:
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
async def wordSearch(*, query: Optional[str] = None):
    # loop through words
    for word in data:
        # validate word search
        if query in data:
            # concantenate word and it meaning into a dict/json format
            x = {query : data[query]}
            # returns data 
            return JSONResponse(content=x, status_code=200)
        else:
            error = {"Oops": "Word not found!"}
            return JSONResponse(content=error, status_code=404)


@app.post("/add-word/")
async def addWord(word_item: dict):
    # parsing json response
    word = word_item["word"]
    meaning = word_item["meaning"]
    
    # checks if word exists 
    if word in data.keys():
        return JSONResponse(content="Word already exist in Database", status_code=201)
    
    else:
        # data to be added as a new key-value pair
        new_data = {word:meaning}
        
        # read the existing JSON data from the file in read mode ('r')
        with open("simple_english_dictionary.json", "r") as file:
            db_file = json.load(file)
            
        # add the new key-value pair to the exxisting data
        db_file.update(new_data)
        
        # write the modified data back to the file
        with open("simple_english_dictionary.json", "w") as file:
            json.dump(db_file, file, indent=4)
            
        return JSONResponse(content="Word added to Database!", status_code=200) 
