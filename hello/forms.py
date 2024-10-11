from django import forms
 
class UserForm(forms.Form):
    name = forms.CharField(help_text="Введите свое имя")
    age = forms.IntegerField(help_text="Введите свой возраст")