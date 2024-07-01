from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .models import CustomUser
##
from django.contrib.auth.forms import  UserChangeForm
from .models import CustomUser


from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('phone_number',)

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = UserChangeForm.Meta.fields

##
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')

class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellidos = forms.CharField(max_length=100)     
    email = forms.EmailField()
    telefono = forms.CharField(max_length=15)
    acepto_terminos = forms.BooleanField()

    def save(self, commit=True):
        contacto = super().save(commit=False)
        if commit:
            contacto.save()
        return contacto

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user 


    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user
