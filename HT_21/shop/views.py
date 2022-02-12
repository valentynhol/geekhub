from .forms import LoginForm, EditForm
from .models import Product
from .serializers import ProductSerializer

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError

from rest_framework import viewsets


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def __get_products(category=None):
    products = []
    if category:
        for product in Product.objects.all().filter(category=category):
            products.append({'title': product.title,
                             'desc': product.description[0:39]+'...' if len(product.description) > 40
                             else product.description,
                             'url': product.image_url,
                             'price': product.price,
                             'id': product.id})

    else:
        for product in Product.objects.all():
            products.append({'title': product.title,
                             'desc': product.description[0:39]+'...' if len(product.description) > 40
                             else product.description,
                             'url': product.image_url,
                             'price': product.price,
                             'id': product.id})

    return products


def __get_cart(session):
    try:
        raw_products = session.load()['cart']
    except KeyError:
        raw_products = None

    products = []
    max_count = {}
    total = 0
    if raw_products:
        for product in raw_products.keys():
            product_obj = Product.objects.get(id=int(product))
            products.append({'id': int(product),
                             'title': product_obj.title,
                             'count': raw_products[product],
                             'price': product_obj.price,
                             'total': product_obj.price * raw_products[product]})
            max_count[int(product)] = raw_products[product]
            total += product_obj.price * raw_products[product]

    return products, total, max_count


def __remove_from_cart(product_id, product_count, session):
    if 'cart' in session.keys():
        if session.get('cart')[product_id] == product_count:
            cart = session.get('cart')
            del cart[product_id]
            session['cart'] = cart
        else:
            cart = session.get('cart')
            cart[product_id] -= product_count
            session['cart'] = cart
    session.save()


def __add_to_cart(product_id, product_count, session):
    if 'cart' in session.keys():
        if str(product_id) in session.get('cart').keys():
            cart = session.get('cart')
            cart[str(product_id)] += int(product_count)
            session['cart'] = cart
        else:
            cart = session.get('cart')
            cart[str(product_id)] = int(product_count)
            session['cart'] = cart
    else:
        session['cart'] = {str(product_id): int(product_count)}


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid:
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect('../')
            else:
                context = {'form': form, 'error': 'Invalid username or password!'}
        else:
            context = {'form': form, 'error': 'Invalid input!'}
    else:
        form = LoginForm()
        context = {'form': form}
    return render(request, 'login.html', context)


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('../')


def edit_product(request, product_id):
    user = request.user
    product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        form = EditForm(request.POST)

        if form.is_valid:
            product.title = request.POST['title']
            product.description = request.POST['description']
            product.price = request.POST['price']
            product.image_url = request.POST['image_url']
            product.category = request.POST['category']
            product.save()

            return render(request, 'edit.html', {'username': user if str(user) != 'AnonymousUser' else None,
                                                 'superuser': user.is_superuser,
                                                 'form': form,
                                                 'success': 'Success!'})
        else:
            return render(request, 'edit.html', {'username': user if str(user) != 'AnonymousUser' else None,
                                                 'superuser': user.is_superuser,
                                                 'form': form,
                                                 'error': 'Invalid input!'})
    else:
        form = EditForm(initial={'title': product.title,
                                 'description': product.description,
                                 'price': product.price,
                                 'image_url': product.image_url,
                                 'category': product.category})

        if request.user.is_authenticated and request.user.is_superuser:
            return render(request, 'edit.html', {'username': user if str(user) != 'AnonymousUser' else None,
                                                 'superuser': user.is_superuser,
                                                 'form': form})
        elif request.user.is_authenticated and not request.user.is_superuser:
            return HttpResponseRedirect('/?error=You-are-not-superuser!!!')
        else:
            return HttpResponseRedirect('/?error=You-are-not-logged-in!!!')


def shop_site(request):
    user = request.user
    try:
        error = request.GET['error'].replace('-', ' ')
    except MultiValueDictKeyError:
        error = None

    try:
        success = request.GET['success'].replace('-', ' ')
    except MultiValueDictKeyError:
        success = None

    return render(request, 'products.html', {'username': user if str(user) != 'AnonymousUser' else None,
                                             'superuser': user.is_superuser,
                                             'products': __get_products(),
                                             'error': error,
                                             'success': success})


def cart(request):
    if request.method == 'POST':
        if request.body.decode('utf-8') == 'buy':
            if request.session.get('cart'):
                del request.session['cart']
                return JsonResponse({'success': 'You have successfully bought items from the cart.'})
            else:
                return JsonResponse({'error': 'You have no products in your cart!!!'})
        else:
            count, product_id = request.body.decode('utf-8').split(',')
            __remove_from_cart(product_id, int(count), request.session)
            cart_products, total, _ = __get_cart(request.session)
            return JsonResponse({'success': f'You have successfully removed {count} '
                                            f'{"item" if int(count) == 1 else "items"} from the cart.',
                                 'products': cart_products,
                                 'total': total})

    else:
        user = request.user

        products, total, max_count = __get_cart(request.session)

        if request.user.is_authenticated:
            return render(request, 'cart.html', {'username': user if str(user) != 'AnonymousUser' else None,
                                                 'superuser': request.user.is_superuser,
                                                 'products': products,
                                                 'total': total,
                                                 'max_count': max_count})
        else:
            return HttpResponseRedirect('/?error=You-are-not-logged-in!!!')


def show_category(request, category):
    user = request.user
    try:
        error = request.GET['error'].replace('-', ' ')
    except MultiValueDictKeyError:
        error = None

    try:
        success = request.GET['success'].replace('-', ' ')
    except MultiValueDictKeyError:
        success = None

    return render(request, 'products.html', {'username': user if str(user) != 'AnonymousUser' else None,
                                             'superuser': request.user.is_superuser,
                                             'products': __get_products(category),
                                             'error': error,
                                             'success': success})


def product_page(request, product_id):
    if request.method == "POST":
        count = int(request.body.decode('utf-8'))
        if request.user.is_authenticated:
            __add_to_cart(product_id, count, request.session)
            return JsonResponse({'success': f'Successfully added {count} {"item" if count == 1 else "items"} to cart.'})
        else:
            return JsonResponse({'error': 'You are not logged in!!!'})
    else:
        user = request.user
        product = Product.objects.get(id=product_id)

        return render(request, 'product.html', {'username': user if str(user) != 'AnonymousUser' else None,
                                                'superuser': request.user.is_superuser,
                                                'id': product_id,
                                                'title': product.title,
                                                'price': product.price,
                                                'description': product.description,
                                                'url': product.image_url,
                                                'category': product.category})
