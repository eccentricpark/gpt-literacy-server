from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from chatgpt.controller import router as chatgpt_router

app = FastAPI()

origins = [
	"*"
]

app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"]
)


@app.get('/')
async def read_root():
	return {
		"message" : "hello world"
	}


app.include_router(chatgpt_router)