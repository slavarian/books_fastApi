# Python
import requests
from requests import Response


# FastApi
import fastapi
import pydantic


app = fastapi.FastAPI()
BOOK_URL = (
    'https://raw.githubusercontent.com/benoitvallon/100-best-books/master/books.json'
)
response: Response = requests.get(BOOK_URL)
books: list[dict] = response.json()


class Book(pydantic.BaseModel):
    id:int
    title:str
    author:str
    country:str
    language:str
    year:int


forms = []
for i,b in enumerate(books):
    forms.append({  
        "id":i+1,
        "title":b["title"],
        "author":b["author"],
        'country':b["country"],
        'language':b["language"],
        'year':b["year"]
                    })


@app.get("/")
def main_page():
    return forms


@app.get("/book/{book_id}")
def get_user(book_id:int):
    result:dict = None
    for i in forms:
        if i.get('id') == book_id:
            result = i 
    return [book for book in forms if book.get('id') == book_id][0]