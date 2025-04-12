from fetchComments import getComments
from ollama import chat
from ollama import ChatResponse

comment_elements = getComments()
print(comment_elements)
ai_response = []

def aiResponse():

    for i in range(5):
        response: ChatResponse = chat(model='crAI-a3', messages=[
        {
            'role': 'user',
            'content': f'{comment_elements[i].text}',
        },
        ])

        # print(response['message']['content'])
        # or access fields directly from the response object
        ai_response.append(response.message.content)

    print (aiResponse())
    return ai_response