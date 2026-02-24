from django import forms

class NameForm(forms.Form):
    name = forms.CharField(
        label='Ваше имя',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Пример: Роман', 'class': 'form-input'}),
        error_messages={'required': 'Пожалуйста, введите ваше имя. Это поле не может быть пустым.'}
    )

    def clean_name(self):
        name = self.cleaned_data['name']
        # Проверка: имя не должно начинаться с цифры
        if name and name[0].isdigit():
            raise forms.ValidationError("Имя не может начинаться с цифры.")
        return name