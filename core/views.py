from django.shortcuts import render
from .forms import NameForm
from .models import UserName

def home_view(request):
    greeting_name = None

    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            # Сохраняем имя в базу данных
            name = form.cleaned_data['name']
            UserName.objects.create(name=name)
            greeting_name = name
            # Очищаем форму после успешной отправки
            form = NameForm() 
    else:
        form = NameForm()

    return render(request, 'core/home.html', {
        'form': form,
        'greeting_name': greeting_name,
    })