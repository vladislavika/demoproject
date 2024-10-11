"""
URL configuration for demoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path, include
from hello import views
from django.views.generic import TemplateView

'''
urlpatterns = [
    path('', views.index),
    path('about', views.about, kwargs={"name":"Tom", "age": 38}),
    path("user", views.user),
    path("user/<name>", views.user),
    path("user/<name>/<int:age>", views.user),
    #re_path(r"^user/(?P<name>\D+)/(?P<age>\d+)", views.user),
]
'''


'''
product_patterns = [
    path("", views.products),
    path("new", views.new),
    path("top", views.top),
]
 
urlpatterns = [
    path("", views.index),
    path("products/", include(product_patterns)),
]
'''


'''
product_patterns = [
    path("", views.products),
    path("comments", views.comments),
    path("questions", views.questions),
]
 
urlpatterns = [
    path("", views.index),
    path("products/<int:id>/", include(product_patterns)),
]
'''

'''
urlpatterns = [
    path("", views.index),
    path("user/", views.user)
]
'''

'''
urlpatterns = [
    path("", views.index),
    path("about/", views.about),
    path("contact/", views.contact),
    path("details/", views.details),
]
'''

'''
urlpatterns = [
    path("index/<int:id>", views.index),
    path("access/<int:age>", views.access),
]
'''

'''
urlpatterns = [
    path("set", views.set),
    path("get", views.get),
]
'''

'''
urlpatterns = [
    path("", views.index),
    path("about/", views.about),
    path("contact/", views.contact),
]
'''

'''
urlpatterns = [
    path("", views.index),
    path("contacts/", views.contacts),
    path("about/", TemplateView.as_view(template_name="about.html", 
        extra_context={"header": "О сайте"})),
    path("contact/", TemplateView.as_view(template_name="contact.html")),
]
'''

'''
urlpatterns = [
    path("", views.index),
    path("postuser/", views.postuser),
]
'''

urlpatterns = [
    path("", views.index),
]