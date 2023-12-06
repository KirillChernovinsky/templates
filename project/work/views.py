from django.shortcuts import render
from django.http import HttpResponse



contacts = [
    {'id': 1, 'type':'phone', 'contact':'+79027722972'},
    {'id': 2, 'type':'telegramm', 'contact': '@BeLuGa230'},
    {'id': 3, 'type':'address', 'contact': "Yzheselga"},
    {'id': 4, 'type':'vk', 'contact': 'Moi vkontacte'},
]

def index(request):
    learning_place = "Фушка"
    group = '9A'
    specialization = 'pythononshink'
    meWants = 'bussnesman'
    data = {'learning_place': learning_place, 'group': group, "specialization": specialization, 'meWants': meWants}
    return render(request, 'work/index.html', context=data)

def about(request):
    FIO = "Chernovinskii Kirill Alexandrovich"
    height = 175
    weight = 65
    age = 16
    data = {'FIO': FIO, 'height': height, 'weight': weight, "age": age}
    return render(request, 'work/about.html', context=data)


def contactsView(request):

    return render(request, "work/contacts.html", context={'contacts': contacts})


# def login(request):
#     return render(request, 'work/login.html', context=)
# Create your views here.
