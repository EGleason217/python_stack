from django.shortcuts import render

def survey(request):
    return render(request, "index.html")

def process(request):
    if request.method == 'POST':
        context = {
            'user_name': request.POST['user_name'],
            'language': request.POST['language'],
            'location': request.POST['location']
        }
        return render(request, 'result.html', context)
    return render(request, 'result.html')