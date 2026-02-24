from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get():
    return {"message": "Hello Internet"}

@app.get('/author')
def getAuthor():
    return {'Author Name': 'Finn', 'Age': '24'}