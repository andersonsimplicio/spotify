from django.contrib.auth.forms import AuthenticationForm
from django import forms

# Você pode estender AuthenticationForm se precisar de campos ou validações extras.
# Por enquanto, vamos usá-lo diretamente.
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Nome de Usuário",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu nome de usuário'})
    )
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Sua senha'})
    )