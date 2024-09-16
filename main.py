from fastapi import FastAPI

app = FastAPI()

@app.get("/helloworld")
async def root():
   return {"message": "Hello World"}

@app.get("/funcaoteste")
async def fucaoteste():
    return {"teste": "deu certo"}