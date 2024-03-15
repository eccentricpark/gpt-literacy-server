from chatgpt.openai_config import get_openai_object
import json
def read_json_file(file='./prompt.json'):
    with open(file, "r", encoding='UTF8') as f:
        data = json.load(f) 
    return data


def __get_ai_response(message):
    try:
        response = get_openai_object().chat.completions.create(
            model="gpt-3.5-turbo-1106", 
            messages=[
                read_json_file()
                ,*message],
            temperature=0.9,
            max_tokens=300,
            top_p=0.8,
            frequency_penalty=1,
            presence_penalty=0.4
        )
        message = response.choices[0].message.content
        return message
    except Exception as e:
        print(f"An error occurred: {e}")
        raise "An error occurred while processing your request."



# message : GPT 응답 형식, 구조가 없으면 기본적인 배열을 삽입합니다.
# string : GPT에게 물어볼 내용. 질문이나 프롬프트 등이 해당됩니다.
def print_response(message=[], string="안녕?"):
    message.append({
        "role" : "user",
        "content" : string
    })
    return __get_ai_response(message)