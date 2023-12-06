from django.shortcuts import render


products = [
    {'id':1, "title": 'Skirt', "size": 'L', 'price': 2000},
    {'id':2, "title": 'Shorts', "size": 'Xl', 'price': 2500},
    {'id':3, "title": 'T-shirt', "size": 'XXl', 'price': 5000},
    {'id':4, "title": 'Dress', "size": 'S', 'price': 1200},
    {'id':5, "title": 'Cap', "size": 'M', 'price': 1300},
]


def productsView(request):
    return render(request, 'shop/products.html', context={'products': products})

def product(request, id):
    product = products[id - 1]
    return render(request, "shop/product.html", context={'product': product})
# from django.http import HttpResponse
# # Create your views here.
#
# def index(request):
#     text = "main page"
#     return HttpResponse(text)

def index(request):
    header = "данные пользователя"
    langs = ['C', 'C++', "python"]
    user = {'name': "Vasilii", 'surname': "Pupkin"}
    address = ('Mira', 12, 147)
    text = '<h4> My text </h4>'

    data = {'header': header, 'langs': langs, 'user': user, 'address': address, 'text': text}
    return render(request, 'shop/index.html', context=data)

def about(request):
    data = {'name': 'Ann', 'interests': 'programming'}
    return render(request, 'shop/about.html', context=data)

def contacts(request):
    return render(request, 'shop/contacts.html')

