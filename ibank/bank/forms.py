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


class CardForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'shadow m-1',
                                                          'placeholder': 'Назва картки'}))
    bank_account = forms.ChoiceField(widget=forms.Select(attrs={'class': 'shadow m-1 dropdown dropdown-menu-dark'}),
                                     choices=[('', 'Виберіть рахунок')])
    color = forms.ChoiceField(widget=forms.Select(attrs={'class': 'shadow m-1 dropdown dropdown-menu-dark'}),
                              choices=[('', 'Виберіть колір'), ('blue', 'Cиній'), ('cyan', 'Бірюзовий'),
                                       ('green', 'Зелений'), ('grey', 'Сірий'), ('magenta', 'Пурпурний'),
                                       ('orange', 'Оранжевий'), ('purple', 'Фіолетовий'), ('red', 'Червоний'),
                                       ('yellow', 'Жовтий')])
    payment_system = forms.ChoiceField(widget=forms.Select(attrs={'class': 'shadow m-1 dropdown dropdown-menu-dark'}),
                                       choices=[('', 'Виберіть платіжну систему'), ('mastercard', 'Mastercard'), ('visa', 'Visa')])


class BankAccountForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'shadow m-1',
                                                          'placeholder': 'Назва рахунку'}))
