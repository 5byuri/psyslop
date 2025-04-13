from fetchComments import getComments
from ollama import chat
from ollama import ChatResponse

comment_elements = getComments()
ai_response = []

def aiResponse(comment_elements):

    for i in len(comment_elements):
        response: ChatResponse = chat(model='cria-a4-b3-02-critical', messages=[
        {
            'role': 'user',
            'content': f'{comment_elements[i].text}',
        },
        ])
        ai_response.append(response.message.content)

    print(ai_response)    
    return ai_response