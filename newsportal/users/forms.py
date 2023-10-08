from allauth.account.forms import SignupForm

from django.contrib.auth.models import Group
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


from .models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={
        'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите имя пользователя'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите имя'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите фамилию'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите emalil'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        common_users = Group.objects.get(name="common users")
        user.groups.add(common_users)
        return user
