from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Урок по Django DJ01</h1>")

def data(request):
    return HttpResponse("<h1>Скоро здесь появятся Данные</h1>")

def test(request):
    return HttpResponse("<h1>Скоро здесь будет страница сайта</h1>")