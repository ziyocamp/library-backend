from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

books_db = [
    {
        "id": 1,
        "title": "O‘tkan kunlar",
        "author": "Abdulla Qodiriy",
        "genre": "Tarixiy roman",
        "year": 2008,
        "pages": 380,
        "description": "O‘zbek adabiyotining birinchi romani bo‘lib, o‘tgan davr hayoti, sevgi va ijtimoiy muammolarni tasvirlaydi."
    },
    {
        "id": 2,
        "title": "Mehrobdan chayon",
        "author": "Abdulla Qodiriy",
        "genre": "Roman",
        "year": 2024,
        "pages": 400,
        "description": "XX asr boshidagi o‘zbek jamiyati, fitnalar va qatag‘on davri haqida yozilgan asar."
    },
    {
        "id": 3,
        "title": "Kecha va kunduz",
        "author": "Cho‘lpon",
        "genre": "Roman",
        "year": 2026,
        "pages": 450,
        "description": "O‘zbek xalqining ma’naviy uyg‘onishi, o‘zlikni anglash va jamiyat muammolarini aks ettiruvchi roman."
    },
    {
        "id": 4,
        "title": "Yulduzli tunlar",
        "author": "Pirimqul Qodirov",
        "genre": "Tarixiy roman",
        "year": 1978,
        "pages": 520,
        "description": "Zahiriddin Muhammad Bobur hayoti va faoliyati haqida yozilgan mashhur tarixiy roman."
    },
    {
        "id": 5,
        "title": "Ulug‘bek xazinasi",
        "author": "Odil Yoqubov",
        "genre": "Tarixiy roman",
        "year": 1974,
        "pages": 370,
        "description": "Ulug‘bek davrining ilmiy va siyosiy hayoti haqida qiziqarli badiiy asar."
    },
    {
        "id": 6,
        "title": "Shum bola",
        "author": "G‘afur G‘ulom",
        "genre": "Qissa",
        "year": 1936,
        "pages": 220,
        "description": "O‘zbekiston xalq yozuvchisining bolalik xotiralari asosida yozilgan mashhur qissa."
    },
    {
        "id": 7,
        "title": "Sarob",
        "author": "G‘afur G‘ulom",
        "genre": "Roman",
        "year": 1935,
        "pages": 340,
        "description": "Jamiyatdagi adolatsizlik va o‘zbek ziyolilarining hayoti haqida yozilgan roman."
    },
    {
        "id": 8,
        "title": "Boburnoma",
        "author": "Zahiriddin Muhammad Bobur",
        "genre": "Tarixiy memuar",
        "year": 1526,
        "pages": 600,
        "description": "Boburning shaxsiy kundaligi va o‘z davrining madaniy, siyosiy, ijtimoiy hayotidan guvohlik beruvchi bebaho asar."
    },
    {
        "id": 9,
        "title": "Oltin zanglamas",
        "author": "Odil Yoqubov",
        "genre": "Roman",
        "year": 1965,
        "pages": 310,
        "description": "O‘zbek xalqining ma’naviy pokligi va halollik timsoli bo‘lgan obrazlar yaratilgan roman."
    },
    {
        "id": 10,
        "title": "Qutlug‘ qon",
        "author": "Oybek",
        "genre": "Tarixiy roman",
        "year": 1940,
        "pages": 480,
        "description": "XVI asrdagi o‘zbek xalqi hayoti, ijtimoiy kurashlari haqida yozilgan mashhur tarixiy roman."
    }
]

next_id = 11

@app.get("/")
async def home():
    total_books = len(books_db)
    total_genres = len(set([book['genre'] for book in books_db]))
    total_authors = len(set([book['author'] for book in books_db]))

    return {
        "books": total_books,
        "genres": total_genres,
        "authors": total_authors
    }


@app.get("/books")
async def get_books(title: str | None = None, author: str | None = None):
    if title or author:
        result = []
        for book in books_db:
            if (
                (isinstance(title, str) and title.lower() in book['title'].lower())
                or (isinstance(author, str) and author.lower() in book['author'].lower())
            ):
                result.append(book) 
        return result

    return books_db


@app.get("/books/{book_id}")
async def get_book_detail(book_id: int, username: str):
    for book in books_db:
        if book['id'] == book_id:
            return book


@app.post("/books")
async def create_books(book: dict):
    global next_id
    book['id'] = next_id

    books_db.append(book)

    next_id += 1
    return book


@app.delete("/books/{book_id}")
async def delete_books(book_id: int):
    for book in books_db:
        if book['id'] == book_id:
            books_db.remove(book)
            return 


@app.put("/books/{book_id}")
async def delete_books(book_id: int, book: dict):
    for book_item in books_db:
        if book_item['id'] == book_id:
            book_item.update(book)

