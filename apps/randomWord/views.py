from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string


# Create your views here.

def randomWord(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1
    
    request.session['word'] = get_random_string(length = 14)

    return render(request, 'randomWord.html')

def reset(request):
    if 'counter' in request.session:
        request.session['counter'] = 0

    return redirect('/randomWord/word/')

