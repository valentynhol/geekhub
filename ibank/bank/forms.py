from django import forms


class LogInForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'shadow m-1',
                                                           'placeholder': "Електронна адреса"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'shadow m-1',
                                                                 'placeholder': 'Пароль'}))


class SignUpForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'shadow m-1',
                                                           'placeholder': "Електронна адреса"}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'shadow m-1',
                                                                 'placeholder': "Номер телефону"}),
                                   max_length=13,
                                   required=True)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'shadow m-1',
                                                               'placeholder': "Ім'я"}),
                                 max_length=30,
                                 required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'shadow m-1',
                                                              'placeholder': "Прізвище"}),
                                max_length=30,
                                required=True)
    patronymic = forms.CharField(widget=forms.TextInput(attrs={'class': 'shadow m-1',
                                                               'placeholder': "По-батькові"}),
                                 max_length=30,
                                 required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'shadow m-1', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'shadow m-1',
                                                                  'placeholder': 'Повторіть пароль'}))
