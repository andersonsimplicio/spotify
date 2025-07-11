from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from spotify.models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'avatar_thumbnail')

    # Define a ordem e os campos que aparecem no formulário de edição de usuário
    # Adicionamos um novo fieldset para 'Campos Personalizados'
    fieldsets = UserAdmin.fieldsets + (
        (('Campos Personalizados'), {'fields': ('avatar', 'bio',)}),
    )

    # Define a ordem e os campos que aparecem no formulário de criação de novo usuário
    # Adicionamos um novo fieldset para 'Campos Personalizados'
    add_fieldsets = UserAdmin.add_fieldsets + (
        (('Campos Personalizados'), {'fields': ('avatar', 'bio',)}),
    )

    # Função para exibir uma miniatura do avatar no list_display
    def avatar_thumbnail(self, obj):
        if obj.avatar:
            # Use safe para evitar problemas com caracteres HTML
            return f'<img src="{obj.avatar.url}" width="50" height="50" style="border-radius: 50%;" />'
        return "Sem Avatar"
    avatar_thumbnail.short_description = 'Avatar'
    avatar_thumbnail.allow_tags = True # Permite que o HTML seja renderizado
