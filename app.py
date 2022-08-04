from fastapi import FastAPI
from mangum import Mangum
from fastapi.middleware.cors import CORSMiddleware



from routes.handlecsv import handlecsv

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get('/hello')
async def get_hello():
    return {"message": "you are in hello url"}

app.include_router(handlecsv)

handler = Mangum(app)

