from fastapi import FastAPI

app = FastAPI()


@app.get("/wellcome")
def wellcome():
    return {
        "bilgi": "Merhaba"
    }