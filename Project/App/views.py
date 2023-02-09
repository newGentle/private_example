from django.shortcuts import render, redirect
from .forms import Uploadform
from .models import upload_file
from Project.settings import BASE_DIR
# Create your views here.


def findword(request):

    if request.method == 'POST':
        form = Uploadform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # file = request.FILES['file']
            # with open(file=file, encoding='utf8') as uploaded:
            #     for word in uploaded.readline:
            #         print(word)

        return redirect('success/')
    else:
        form = Uploadform
    return render(request, 'index.html', {'form': form})

def success(request):
    cnt = 0
    file = upload_file.objects.last().file
    word = upload_file.objects.last().word
    file = str(file).split('/')
    with open (file='App/files/' + file[1], encoding='utf8') as filename:
        words = filename.read().split()
        for item in words:
            if word.lower() == item.lower():
                cnt +=1
    return render(request, 'next.html', {'success': cnt})
        