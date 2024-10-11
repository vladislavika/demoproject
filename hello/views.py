from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseBadRequest, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from .forms import UserForm

'''
def index(request):
  return HttpResponse("<h2>Главная</h2>")

#

def index(request):
    return HttpResponse("Hello METANIT.COM", headers={"SecretCode": "21234567"})

#

def index(request):
    return HttpResponse("Произошла ошибка", status=400, reason="Incorrect data")

#
    
def index(request):
    return HttpResponse("<h1>Hello</h1>", content_type="text/plain", charset="utf-8")

#

def about(request, name, age):
    return HttpResponse(f"""
            <h2>О пользователе</h2>
            <p>Имя: {name}</p>
            <p>Возраст: {age}</p>
    """)

#
    
def user(request, name="Undefined", age =0):
    return HttpResponse(f"<h2>Имя: {name} Возраст:{age}</h2>")

#

def index(request):
    host = request.META["HTTP_HOST"] # получаем адрес сервера
    user_agent = request.META["HTTP_USER_AGENT"]    # получаем данные бразера
    path = request.path     # получаем запрошенный путь
    
    return HttpResponse(f"""
        <p>Host: {host}</p>
        <p>Path: {path}</p>
        <p>User-agent: {user_agent}</p>
    """)
'''



'''
def index(request):
    return HttpResponse("Главная страница")
 
def products(request):
    return HttpResponse("Список товаров")
 
def new(request):
    return HttpResponse("Новые товары")
 
def top(request):
    return HttpResponse("Наиболее популярные товары")
'''


'''
def index(request):
    return HttpResponse("Главная страница")
 
def products(request, id):
    return HttpResponse(f"Товар {id}")
 
def comments(request, id):
    return HttpResponse(f"Комментарии о товаре {id}")
 
def questions(request, id):
    return HttpResponse(f"Вопросы о товаре {id}")
'''


'''
def index(request):
    return HttpResponse("<h2>Главная</h2>")
  
def user(request):
    age = request.GET.get("age", 0)
    name = request.GET.get("name", "Undefined")
    return HttpResponse(f"<h2>Имя: {name}  Возраст: {age}</h2>")
'''


'''
def index(request, id):
    people = ["Tom", "Bob", "Sam"]
    # если пользователь найден, возвращаем его
    if id in range(0, len(people)):
        return HttpResponse(people[id])
    # если нет, то возвращаем ошибку 404
    else:
        return HttpResponseNotFound("Not Found")
 
def access(request, age):
    # если возраст НЕ входит в диапазон 1-110, посылаем ошибку 400
    if age not in range(1, 111):
        return HttpResponseBadRequest("Некорректные данные")
    # если возраст больше 17, то доступ разрешен
    if(age > 17):
        return HttpResponse("Доступ разрешен")
    # если нет, то возвращаем ошибку 403
    else:
        return HttpResponseForbidden("Доступ заблокирован: недостаточно лет")
'''

'''
def index(request):
    return JsonResponse({"name": "Tom", "age": 38})
'''

'''
def index(request):
    bob = Person("Bob", 41)
    return JsonResponse(bob, safe=False, encoder=PersonEncoder)
 
class Person:
  
    def __init__(self, name, age):
        self.name = name    # имя человека
        self.age = age        # возраст человека
 
class PersonEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {"name": obj.name, "age": obj.age}
            # return obj.__dict__
        return super().default(obj)
'''

'''
def set(request):
    # получаем из строки запроса имя пользователя
    username = request.GET.get("username", "Undefined")
    # создаем объект ответа
    response = HttpResponse(f"Hello {username}")
    # передаем его в куки
    response.set_cookie("username", username)
    return response

def get(request):
    # получаем куки с ключом username
    username = request.COOKIES["username"]
    return HttpResponse(f"Hello {username}")
'''


'''
def index(request):
    return render(request, "index.html", context = {"person": Person("Tom")})
 
class Person:
  
    def __init__(self, name):
        self.name = name    # имя человека
'''



'''
def index(request):
    header = "Данные пользователя"              # обычная переменная
    langs = ["Python", "Java", "C#"]            # список
    user ={"name" : "Tom", "age" : 23}          # словарь
    address = ("Абрикосовая", 23, 45)           # кортеж
  
    data = {"header": header, "langs": langs, "user": user, "address": address}
    return render(request, "index.html", context=data)
'''

'''
def about(request):
    return render(request, "about.html")
 
def contact(request):
    return render(request, "contact.html")
'''


'''
def index(request):
    return render(request, "index.html", context={"site":"METANIT.COM", "tutorial":"gpuk"})
 
def contacts(request):
    return render(request, "contacts.html")
'''


'''
def index(request):
    return render(request, "index.html")
 
def postuser(request):
    # получаем из строки запроса имя пользователя
    name = request.POST.get("name", "Undefined")
    age = request.POST.get("age", 1)
    langs = request.POST.getlist("languages", ["python"])
     
    return HttpResponse(f"""
                <div>Name: {name}  Age: {age}<div>
                <div>Languages: {langs}</div>
            """)
'''

def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        return HttpResponse(f"<h2>Привет, {name}, твой возраст: {age}</h2>")
    else:
        userform = UserForm()
        return render(request, "index.html", {"form": userform})