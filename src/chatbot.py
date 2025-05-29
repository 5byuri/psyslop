
from ollama import chat
from ollama import ChatResponse

def aiResponse(comment: str):

    response: ChatResponse = chat(model='cria-a4-b3-02-critical', messages=[
        {
            'role': 'user',
            'content': f'{comment}',
        },
        ])    
   
    return response.message.content

