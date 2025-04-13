
from ollama import chat
from ollama import ChatResponse

def aiResponse(comments_list):

    ai_response = []

    for i in range(len(comments_list)):
        response: ChatResponse = chat(model='cria-a4-b3-02-critical', messages=[
        {
            'role': 'user',
            'content': f'{comments_list[i].text}',
        },
        ])
        ai_response.append(response.message.content)

    print(ai_response)    
    return ai_response

