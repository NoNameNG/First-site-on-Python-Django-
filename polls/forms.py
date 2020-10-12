from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class RegitrationForm(forms.ModelForm):
    password_check = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'password_check',
            'first_name',
            'last_name',
            'email'
        ]

    def __init__(self, *args, **kwargs):
        super(RegitrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['username'].help_text = 'Обязательное поле'
        self.fields['password'].label = 'Пароль'
        self.fields['password'].help_text = 'Обязательное поле'

        self.fields['first_name'].label = 'Имя'
        self.fields['email'].label = 'Почта'
        self.fields['password_check'].label = 'Подтвердить пароль'
