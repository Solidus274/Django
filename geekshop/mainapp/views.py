from django.shortcuts import render


# Create your views here.
def main(request):
    content = {
        'title': 'Главная'
    }
    return render(request, 'index.html', content)


def products(request):
    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]
    content = {
        'links_menu': links_menu,
        'title': 'Продукты'
    }
    return render(request, 'products.html', content)


def contact(request):
    return render(request, 'contact.html')


def products_all(request):
    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]
    content = {
        'links_menu': links_menu,
        'title': 'Продукты'
    }
    return render(request, 'products.html', content)


def products_home(request):
    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]
    content = {
        'links_menu': links_menu,
        'title': 'Продукты'
    }
    return render(request, 'products.html', content)


def products_office(request):
    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]
    content = {
        'links_menu': links_menu,
        'title': 'Продукты'
    }
    return render(request, 'products.html', content)


def products_modern(request):
    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]
    content = {
        'links_menu': links_menu,
        'title': 'Продукты'
    }
    return render(request, 'products.html', content)


def products_classic(request):
    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]
    content = {
        'links_menu': links_menu,
        'title': 'Продукты'
    }
    return render(request, 'products.html', content)


# def admin(request):
#     return render(request, 'index.html')
