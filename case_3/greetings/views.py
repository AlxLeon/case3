from django.shortcuts import render, redirect
from greetings.forms import GreetingForm
from greetings.models import UserGreeting


def index(request):
    if request.method == 'POST':
        form = GreetingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            _, created = UserGreeting.objects.get_or_create(name=name)
            request.session['last_name'] = name
            request.session['is_new_user'] = created

            return redirect('submit')
    else:
        form = GreetingForm()

    return render(request, 'greetings/index.html', {'form': form})


def submit(request):
    name = request.session.get('last_name', 'Anonymous')
    is_new_user = request.session.get('is_new_user', False)

    welcome_message = "Добро пожаловать, " if is_new_user else "Рады вас снова видеть, "

    return render(request, 'greetings/submit.html', {
        'name': name,
        'welcome_message': welcome_message
    })
