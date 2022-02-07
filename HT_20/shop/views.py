from django.shortcuts import render
from .forms import LoginForm, EditForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from .models import Product, Cart
from django.utils.datastructures import MultiValueDictKeyError


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


def __remove_from_cart(product_id, username, product_count):
    cart = Cart.objects.get_or_create(username=username)[0]
    if cart.products:
        if cart.products[str(product_id)] == product_count:
            del cart.products[str(product_id)]
        else:
            cart.products[str(product_id)] = int(cart.products[str(product_id)]) - product_count

    cart.save()


def __add_to_cart(product_id, username, product_count):
    cart = Cart.objects.get_or_create(username=username)
    if cart[0].products:
        if str(product_id) in cart[0].products.keys():
            cart[0].products[str(product_id)] = int(cart[0].products[str(product_id)]) + int(product_count)
        else:
            cart[0].products[str(product_id)] = int(product_count)
    else:
        cart[0].products = {str(product_id): int(product_count) }

    cart[0].save()


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
        count = int(request.POST['count'])
        __remove_from_cart(request.POST['id'], str(request.user), count)
        return HttpResponseRedirect(
            f'../cart/?success=Successfully-removed-{count}-{"item" if count == 1 else "items"}!'
        )
    else:
        try:
            error = request.GET['error'].replace('-', ' ')
        except MultiValueDictKeyError:
            error = None

        try:
            success = request.GET['success'].replace('-', ' ')
        except MultiValueDictKeyError:
            success = None

        user = request.user

        raw_products = Cart.objects.get_or_create(username=str(user))[0].products

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
                                 'total': product_obj.price*raw_products[product]})
                max_count[int(product)] = raw_products[product]
                total += product_obj.price*raw_products[product]

        if request.user.is_authenticated:
            return render(request, 'cart.html', {'username': user if str(user) != 'AnonymousUser' else None,
                                                 'superuser': request.user.is_superuser,
                                                 'products': products,
                                                 'total': total,
                                                 'max_count': max_count,
                                                 'error': error,
                                                 'success': success})
        else:
            return HttpResponseRedirect('/?error=You-are-not-logged-in!!!')


def buy(request):
    cart = Cart.objects.get_or_create(username=str(request.user))[0]
    if cart.products:
        cart.delete()
        return HttpResponseRedirect('/?success=You-have-successfully-bought-products.')
    else:
        return HttpResponseRedirect('/?error=You-have-no-products-in-your-cart!!!')


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
        if request.user.is_authenticated:
            __add_to_cart(product_id, str(request.user), request.POST['count'])
            return HttpResponseRedirect('/?success=You-have-successfully-added-product-to-your-cart.')
        else:
            return HttpResponseRedirect('/?error=You-are-not-logged-in!!!')
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
