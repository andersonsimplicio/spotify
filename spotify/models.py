from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    # Adicione seus campos personalizados aqui.
    # Por exemplo:
    avatar = models.ImageField(
        _("Avatar"),
        upload_to="avatars/",
        blank=True,
        null=True,
        help_text=_("Imagem de perfil do usuário.")
    )
    bio = models.TextField(
        _("Biografia"),
        blank=True,
        help_text=_("Uma breve descrição sobre o usuário.")
    )
    

    class Meta:
        verbose_name = _("Usuário Personalizado")
        verbose_name_plural = _("Usuários Personalizados")

    def __str__(self):
        return self.username
