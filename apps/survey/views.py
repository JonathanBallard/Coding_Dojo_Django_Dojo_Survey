from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, 'index.html')

def result(request):
    if request.method == 'POST':
        print(request.POST)

        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        

        return redirect('displayResult/')

    elif request.method == 'GET':
        return redirect('displayResult/')

def displayResult(request):

    return render(request, 'result.html')