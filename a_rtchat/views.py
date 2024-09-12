from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

@login_required
def chat_view(request):
    chat_group = get_object_or_404(ChatGroup, group_name="public-chat")
    chat_messages = chat_group.chat_messages.all()[:30]
    form = ChatmessageCreateForm()

                # without htmx
    # if request.method == 'POST':
    #     form = ChatmessageCreateForm(request.POST)
    #     if form.is_valid:
    #         message = form.save(commit=False)
    #         message.author = request.user
    #         message.group = chat_group
    #         message.save()
    #         return redirect('home')   
    # return render(request, 'a_rtchat/chat.html', {'chat_messages': chat_messages, 'form': form})

#part 1: setup
                #with htmx
    if request.htmx:
            form = ChatmessageCreateForm(request.POST)
            if form.is_valid:
                message = form.save(commit=False)
                message.author = request.user
                message.group = chat_group
                message.save()
                context = {
                     'message': message,
                     'user': request.user
                }
                return render(request, 'a_rtchat/partials/chat_message_p.html', context)  

    return render(request, 'a_rtchat/chat.html', {'chat_messages': chat_messages, 'form': form})
