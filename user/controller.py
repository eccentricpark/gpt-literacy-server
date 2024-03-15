# controller/user.py
from fastapi import APIRouter
from user.service import create_user
from user.model import UserDto
# from chatgpt.service import print_response
from chatgpt.service import print_response

router = APIRouter()

@router.get("/user")
async def create(prompt: str):
    assistant_response = print_response([], prompt)
    print(assistant_response)
    return assistant_response