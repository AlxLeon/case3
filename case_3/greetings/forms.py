from django import forms


class GreetingForm(forms.Form):
    name = forms.CharField(label='Введите имя', max_length=100)
