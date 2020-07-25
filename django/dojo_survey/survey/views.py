from django.shortcuts import render, redirect

def survey(request):
    return render(request, "index.html")

def process(request):
    if request.method == 'GET':
        return redirect('/')
    request.session['result'] = {
            'user_name': request.POST['user_name'],
            'language': request.POST['language'],
            'location': request.POST['location']
        }
    return redirect('/result')
    return render(request, 'result.html')

def result(request):
    context = {
        'result': request.session['result']
    }
    return render(request, 'result.html', context)
