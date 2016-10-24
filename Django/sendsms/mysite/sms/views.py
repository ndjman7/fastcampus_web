from django.shortcuts import render
from apis import send_sms


def index(request):
    if request.method == 'POST':
        send_sms(request.POST['to'], request.POST['text'])

    return render(request, 'sms/index.html', {})
