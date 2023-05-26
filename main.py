from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def get_hello():
    return f"Hello world!"
