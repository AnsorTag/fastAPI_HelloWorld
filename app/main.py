from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
async def helloWorld():
    string = {"text": "Hello world"}
    print("hello World!")

    return string
