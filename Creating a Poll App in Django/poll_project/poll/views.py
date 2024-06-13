from django.shortcuts import render, redirect
from django.http import HttpResponse


from .forms import CreatePollForm
from .models import Poll

def home(request):
    polls = Poll.objects.all()
    context = {
        'polls' : polls
    }
    return render(request, 'poll/home.html', context)


def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreatePollForm()
    context = {
        'form' : form
    }
    return render(request, 'poll/create.html', context)


def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    if request.method == 'POST':
        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        else:
            return HttpResponse(400, 'Invalid form')

        poll.save()

        return redirect('results', poll.id)

    context = {
        'poll' : poll
    }
    return render(request, 'poll/vote.html', context)


def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {
        'poll' : poll
    }
    return render(request, 'poll/results.html', context)


def login(request):
    # if request.method == 'POST':
    #     form = AuthenticationForm(request, data=request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data.get('username')
    #         password = form.cleaned_data.get('password')
    #         user = authenticate(request, username=username, password=password)
    #         if user is not None:
    #             auth_login(request, user)
    #             return redirect('home')
    #         else:
    #             return HttpResponse('Invalid username or password')
    #     else:
    #         return HttpResponse('Invalid form data')
    # else:
    #     form = AuthenticationForm()

    # context = {
    #     'form' : form
    # }

    polls = Poll.objects.all()
    context = {
        'polls' : polls
    }
    return render(request, 'poll/login.html', context)


def register(request):
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get('username')
    #         raw_password = form.cleaned_data.get('password1')
    #         user = authenticate(username=username, password=raw_password)
    #         auth_login(request, user)
    #         return redirect('home')
    #     else:
    #         return HttpResponse('Invalid form data')
    # else:
    #     form = UserCreationForm()
    
    # context = {
    #     'form': form
    # }

    polls = Poll.objects.all()
    context = {
        'polls' : polls
    }
    
    return render(request, 'poll/register.html', context)