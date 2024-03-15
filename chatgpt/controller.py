# controller/user.py
from fastapi import APIRouter
from .service import print_response

router = APIRouter()

@router.get('/gpt')
async def inference(prompt: str):
	return print_response([], prompt)