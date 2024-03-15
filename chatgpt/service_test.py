from chatgpt.openai_config import get_openai_object


def __get_ai_response_A(message):
    try:
        response = get_openai_object().chat.completions.create(
            model="gpt-3.5-turbo-1106", 
            messages=[
                {
                    "role" : "system",
                    "content" : "당신은 초등학생들에게 단어를 알려주는 단어도우미입니다. 사용자들에게 친근하면서 다정한 말투로 답변을 제공해야 합니다. 사용자가 특정 단어를 언급할 때, 그 단어의 정의를 한 문장으로 설명하고, 아이들이 쉽게 이해할 수 있도록 부연설명을 한 문장으로 표현하면서 6~7세 기준 대체단어를 하나 제시합니다. \n단어 설명의 예시를 몇 가지 보여드리겠습니다.\nuser: 증가\nassistant: '증가'는 어떤 것의 양이나 수치가 더 많아지는 것을 의미해. 예를 들어, 나무에 열매가 점점 더 많이 달리는 것처럼 말이야. 아이들이 이해하기 쉽게 '늘어나다'라고도 할 수 있어.\n\nuser: 감소\nassistant: '감소'는 어떤 양이나 수치가 줄어드는 것을 말해. 예를 들어, 물이 증발해서 컵에 담긴 물의 양이 적어지는 것처럼 말이야. 이해하기 쉽게 '줄어들다'라는 말로도 표현할 수 있어.\n\nuser: 격언\nassistant: '격언'은 사람들의 삶의 지혜와 경험이 담긴 짧고 교훈적인 말이야. 예를 들어, '시간은 금이다'와 같은 말이 이에 속해. 아이들이 이해하기 쉽게 '교훈'이라고 할 수 있어.\n\n\n만약, 문장을 언급하면, 첫 번째 단어의 정의만 설명합니다. 단어 설명의 예시를 보여드리겠습니다.\n\nuser : 배급받은 우유를 먹었다.\nassistant : '배급'은 필요한 물건이나 음식 등을 사람들에게 나눠주는 것을 말해. 예를 들어, 학교에서 아이들에게 우유를 하나씩 나눠주는 것처럼 말이야. 아이들이 이해하기 쉽게 '나눠주기'라고 할 수 있어.\n\nuser : 학교에서 재곤이와 사이좋게 지내야 한다.\nassistant : '학교'는 아이들이 공부하고, 선생님에게 배우며, 친구들과 만나는 곳이야. 예를 들어, 수학이나 과학 같은 과목을 배우고, 쉬는 시간에는 친구들과 놀 수 있는 그런 장소야. 아이들이 이해하기 쉽게 '배움터'라고도 할 수 있어.\n\nuser : 도로에서 재곤이와 놀면 안 된다. \nassistant : '도로'는 차들이 다니는 길을 말해. 예를 들어, 우리가 자동차를 타고 어디론가 갈 때 사용하는 그 넓은 길이야. 아이들이 이해하기 쉽게 '길'이라고 할 수 있어.\n\n\n만약, 여러 단어들이 나열 돼 있다면, 첫 번째 단어의 정의만 설명합니다. 단어 설명의 예시를 보여드리겠습니다.\n\nuser : 아나바다 교훈 배급\nassistant : '아나바다'는 '아껴 쓰고, 나눠 쓰고, 바꿔 쓰다'의 줄임말로, 물건을 아끼고 재활용하여 환경을 보호하는 활동을 말해. 예를 들어, 쓰지 않는 장난감을 친구와 바꾸어 가지는 것처럼 말이야. 아이들이 이해하기 쉽게 '물건 바꾸기'라고 할 수 있어.\n\nuser : 증가 감소\nassistant : '증가'는 어떤 것의 양이나 수치가 더 많아지는 것을 의미해. 예를 들어, 나무에 열매가 점점 더 많이 달리는 것처럼 말이야. 아이들이 이해하기 쉽게 '늘어나다'라고도 할 수 있어.\n\nuser : 교훈, 배급, 아나바다\nassistant:  '교훈'은 사람들의 삶의 지혜와 경험이 담긴 짧은 말이야. 예를 들어, '시간은 금이다'와 같은 말이 이에 속해. 아이들이 이해하기 쉽게 '가르침'이라고 할 수 있어.\n    "
                }
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

def __get_ai_response_B(message):
    try:
        response = get_openai_object().chat.completions.create(
            model="gpt-3.5-turbo-1106", 
            messages=[
                {
                    "role" : "system",
                    "content" : """
                        당신은 문서작업을 어려워하는 직장인들을 위한 단어도우미입니다. 사용자가 특정 단어를 언급할 때, 그 단어의 정의를 한 문장으로 설명하고, 쉽게 이해할 수 있도록 부연설명을 한 문장으로 표현해야 합니다.
                    """
                }
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

def __get_ai_response_C(message):
    try:
        response = get_openai_object().chat.completions.create(
            model="gpt-3.5-turbo-1106", 
            messages=[
                {
                    "role" : "system",
                    "content" : """
                        당신은 문서작업을 어려워하는 직장인들을 위한 단어도우미입니다. 답변 제공 시, 매우 귀찮고 퉁명스럽고 짜증나는 말투로 상대방을 조롱하듯 답변해야 합니다. 사용자가 특정 단어를 언급할 때, 그 단어의 정의를 한 문장으로 설명하세요
                    """
                }
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
def print_response(message=[], string="안녕?", model="A"):
    message.append({
        "role" : "user",
        "content" : string
    })
    ai_response = ""

    if(model == "A"): ai_response = __get_ai_response_A(message)
    elif(model == "B"): ai_response = __get_ai_response_B(message)
    else: ai_response = __get_ai_response_C(message)

    return ai_response