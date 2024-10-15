from django.shortcuts import render
from django.http import JsonResponse
from .models import Chat  # remove if you didn't create a Chat model

def chatbot(request):
    if request.method == 'POST':
        message = request.POST['message']
        # Here you will add your chatbot logic

        # Storing the chat message (remove if you didn't create a Chat model)
        chat = Chat(message=message)
        chat.save()

        # Return the chatbot's response
        response = {"message": "This is a response from the chatbot"}
        return JsonResponse(response)

    return render(request, 'chatapp/chatbot.html')
