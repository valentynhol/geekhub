import random
import datetime

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

from .forms import LogInForm, SignUpForm, CardForm, BankAccountForm
from .models import Card, BankAccount, User


def __generate_card_num(payment_system):
    if payment_system == 'visa':
        card_num = '4'
    else:
        card_num = '5'

    for i in range(14):
        card_num += str(random.randint(1, 9))

    last_digit_sum = 0
    for digit in card_num:
        if int(digit) % 2 == 1:
            digit = str(int(digit)*2)
            digit = sum(map(int, [i for i in digit]))

        last_digit_sum += int(digit)

    last_digit = 10 - (last_digit_sum % 10)
    card_num += '0' if last_digit == 10 else str(last_digit)
    return card_num


def __generate_iban(ba_type):
    bi_num = '380982'
    ba = '00000'

    if ba_type == 'checking':
        ba += '2600'
    elif ba_type == 'deposit':
        ba += '2620'
    else:
        ba += '2640'

    for i in range(10):
        ba += str(random.randint(1, 9))

    iban_raw = int(bi_num + ba + '301000')

    control_sum = str(98 - (iban_raw - 97*(iban_raw//97)))

    iban = 'UA' + ('0'+control_sum if int(control_sum) <= 9 else control_sum) + bi_num + ba
    return iban


def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(email=request.POST['email'],
                                                password=request.POST['password1'],
                                                first_name=request.POST['first_name'],
                                                last_name=request.POST['last_name'],
                                                patronymic=request.POST['patronymic'],
                                                phone_number=request.POST['phone_number'])
                login(request, user)
                return HttpResponseRedirect('../')
            except IntegrityError as signup_error:
                request.session['error'] = \
                    'Ця електронна адреса вже використовується' \
                    if 'email' in str(signup_error) \
                    else 'Цей номер телефону вже використовується'
        else:
            request.session['error'] = 'Паролі не збігаються!'
    else:
        form = SignUpForm()

    try:
        error = request.session['error']
        del request.session['error']
    except KeyError:
        error = None

    context = {'form': form, 'error': error}
    return render(request, 'signup.html', context)


def user_login(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        user = authenticate(request, email=request.POST['email'], password=request.POST['password'])
        if user:
            login(request, user)
            return HttpResponseRedirect('../')
        else:
            request.session['error'] = 'Неправильна електронна адреса або пароль!'
    else:
        form = LogInForm()

    try:
        error = request.session['error']
        del request.session['error']
    except KeyError:
        error = None

    context = {'form': form, 'error': error}
    return render(request, 'login.html', context)


@login_required(redirect_field_name=None)
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('../')


@login_required(redirect_field_name=None)
def home(request):
    user = request.user

    raw_cards = Card.objects.all().filter(cardholder_email=user.email)
    raw_bas = BankAccount.objects.all().filter(email=user.email)

    cards = []
    for card in raw_cards:
        cards.append({'title': card.title, 'number': card.beautiful_number(), 'color': card.color,
                      'payment_system': card.payment_system, 'id': card.id})
    bas = []
    for ba in raw_bas:
        bas.append({'title': ba.title, 'currency': ba.currency, 'iban': ba.beautiful_iban(), 'id': ba.id, 'balance': ba.balance})

    try:
        error = request.session['error']
        del request.session['error']
    except KeyError:
        error = None
    try:
        success = request.session['success']
        del request.session['success']
    except KeyError:
        success = None

    return render(request, 'cards.html', {'email': user, 'cards': cards, 'bank_accounts': bas,
                                          'error': error, 'success': success})


@login_required(redirect_field_name=None)
def create_card(request):
    user = request.user
    if request.method == 'POST':
        for i in range(60):
            try:
                card_number = __generate_card_num(request.POST['payment_system'])
                expiry_date = datetime.date(year=datetime.date.today().year+3,
                                            month=datetime.date.today().month,
                                            day=datetime.date.today().day).strftime('%m/%y')
                card = Card(title=request.POST['title'], color=request.POST['color'],
                            payment_system=request.POST['payment_system'],
                            card_number=card_number, cvv=''.join([str(random.randint(1, 9)) for i in range(3)]),
                            bank_account=request.POST['bank_account'], expiry_date=expiry_date,
                            cardholder_name=user.first_name, cardholder_surname=user.last_name,
                            cardholder_email=user.email)
                card.save()
                return HttpResponseRedirect('../')
            except IntegrityError:
                pass
        request.session['error'] = 'Помилка створення карти'
        return HttpResponseRedirect('../')
    else:
        form = CardForm()
        bas = BankAccount.objects.all().filter(email=user.email)

        form.fields['bank_account'].choices += [(bank_account.id, bank_account.title) for bank_account in bas]

        try:
            error = request.session['error']
            del request.session['error']
        except KeyError:
            error = None
        try:
            success = request.session['success']
            del request.session['success']
        except KeyError:
            success = None

        context = {'form': form, 'email': user, 'error': error, 'success': success}
        return render(request, 'add_card.html', context)


@login_required(redirect_field_name=None)
def create_ba(request):
    user = request.user
    if request.method == 'POST':
        for i in range(60):
            try:
                iban = __generate_iban('checking')
                ba = BankAccount(title=request.POST['title'], iban=iban, currency='UAH', balance='0', name=user.first_name,
                                 surname=user.last_name, patronymic=user.patronymic, email=user.email)
                ba.save()
                return HttpResponseRedirect('../')
            except IntegrityError:
                pass
        request.session['error'] = 'Помилка створення рахункy'
        return HttpResponseRedirect('../')
    else:
        try:
            error = request.session['error']
            del request.session['error']
        except KeyError:
            error = None
        try:
            success = request.session['success']
            del request.session['success']
        except KeyError:
            success = None

        form = BankAccountForm()
        context = {'form': form, 'email': user, 'error': error, 'success': success}
        return render(request, 'add_bank_account.html', context)


@login_required(redirect_field_name=None)
def card_page(request, card_id):
    user = request.user
    try:
        card = Card.objects.get(id=card_id)
    except Card.DoesNotExist:
        request.session['error'] = 'Такої карти не існує!'
        return HttpResponseRedirect('../')

    if user.email == card.cardholder_email:
        card_ba = BankAccount.objects.get(id=card.bank_account)

        try:
            error = request.session['error']
            del request.session['error']
        except KeyError:
            error = None
        try:
            success = request.session['success']
            del request.session['success']
        except KeyError:
            success = None

        context = {'email': user, 'error': error, 'success': success,
                   'card': {'number': card.beautiful_number(), 'title': card.title, 'bank_account': card_ba.beautiful_iban(),
                            'ba_title': card_ba.title, 'color': card.color, 'payment_system': card.payment_system,
                            'cardholder': f'{card.cardholder_surname} {card.cardholder_name}', 'cvv': card.cvv,
                            'expiry_date': card.expiry_date, 'id': card.id}}
        return render(request, 'card_page.html', context)
    else:
        request.session['error'] = 'Ви не є власником цієї картки!'
        return HttpResponseRedirect('../')


@login_required(redirect_field_name=None)
def ba_page(request, ba_id):
    user = request.user
    try:
        ba = BankAccount.objects.get(id=ba_id)
    except BankAccount.DoesNotExist:
        request.session['error'] = 'Такого рахунку не існує!'
        return HttpResponseRedirect('../')

    if user.email == ba.email:
        try:
            error = request.session['error']
            del request.session['error']
        except KeyError:
            error = None
        try:
            success = request.session['success']
            del request.session['success']
        except KeyError:
            success = None

        context = {'email': user, 'error': error, 'success': success,
                   'ba': {'iban': ba.beautiful_iban(), 'title': ba.title, 'balance': ba.balance, 'currency': ba.currency,
                          'full_name': f'{ba.surname} {ba.name} {ba.patronymic}'}}
        return render(request, 'ba_page.html', context)
    else:
        request.session['error'] = 'Ви не є власником цього рахунку!'
        return HttpResponseRedirect('../')


@login_required(redirect_field_name=None)
def edit_card(request, card_id):
    user = request.user
    try:
        card = Card.objects.get(id=card_id)
    except Card.DoesNotExist:
        request.session['error'] = 'Такої карти не існує!'
        return HttpResponseRedirect('../')

    if user.email == card.cardholder_email:
        if request.method == 'POST':
            card.title = request.POST['title']
            card.color = request.POST['color']
            card.save()

            request.session['success'] = 'Картку успішно змінено'
            return HttpResponseRedirect('/cards/'+str(card_id))
        else:
            form = CardForm(initial={'color': card.color, 'title': card.title})

            try:
                error = request.session['error']
                del request.session['error']
            except KeyError:
                error = None
            try:
                success = request.session['success']
                del request.session['success']
            except KeyError:
                success = None

            context = {'form': form, 'email': user, 'error': error, 'success': success, 'card_title': card.title, 'card_id': card_id}
            return render(request, 'edit_card.html', context)
    else:
        request.session['error'] = 'Ви не є власником цієї картки!'
        return HttpResponseRedirect('../')