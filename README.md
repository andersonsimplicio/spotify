# spotify
Spotify Clone com Django
Este é um projeto prático desenvolvido como parte de um curso ou estudo de Django, focado na criação de um clone simplificado do Spotify. O objetivo principal é aplicar conceitos de desenvolvimento web com Django, incluindo modelos de usuário personalizados, autenticação, gerenciamento de mídias e configuração de ambiente.

🚀 Funcionalidades Implementadas
Modelo de Usuário Personalizado (CustomUser): Extensão do modelo de usuário padrão do Django com campos adicionais como avatar (imagem de perfil) e bio (biografia).

Administração de Usuários: Integração completa do CustomUser no painel de administração do Django, permitindo o cadastro e gerenciamento de usuários, incluindo upload de avatares.

Sistema de Autenticação:

Tela de Login: Página dedicada para autenticação de usuários.

Validação de Usuário: A página inicial (/) é protegida e só pode ser acessada por usuários autenticados.

Logout: Funcionalidade para desconectar o usuário.

Gerenciamento de Arquivos de Mídia: Configuração do Django para servir arquivos de imagem (como avatares) durante o desenvolvimento.

Estrutura Básica de Frontend: Layout inicial inspirado no Spotify com barra lateral, cabeçalho e área de conteúdo, utilizando HTML e CSS.

🛠️ Tecnologias Utilizadas
Backend:

Python

Django (Framework Web)

Pillow (Para manipulação de imagens, necessário para ImageField)

Frontend:

HTML5

CSS3

Font Awesome (Ícones)

Banco de Dados: SQLite (padrão do Django para desenvolvimento)

⚙️ Configuração do Ambiente
Siga os passos abaixo para configurar e rodar o projeto em sua máquina local.

Pré-requisitos
Python 3.x instalado

pip (gerenciador de pacotes do Python)

Passos para Configuração
Clone o Repositório:

git clone <URL_DO_SEU_REPOSITORIO>
cd spotify-clone-django # Ou o nome da pasta do seu projeto

Crie e Ative um Ambiente Virtual:
É uma boa prática isolar as dependências do seu projeto.

python -m venv venv
# No Windows:
.\venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate

Instale as Dependências:
Crie um arquivo requirements.txt na raiz do seu projeto com as seguintes linhas:

Django
Pillow

Então, instale-as:

pip install -r requirements.txt

Configurações do Projeto (settings.py)
Certifique-se de que as seguintes configurações estão presentes no seu settings.py:

INSTALLED_APPS:

INSTALLED_APPS = [
    # ...
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',  # Seu app de usuários
    'spotify', # Seu app principal do Spotify, se for o caso
    # ...
]

AUTH_USER_MODEL:

AUTH_USER_MODEL = 'users.CustomUser'

MEDIA_URL e MEDIA_ROOT:

import os
# ...
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_REDIRECT_URL e LOGIN_URL:

LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'login'

Configurações de URL (urls.py principal)
No seu arquivo urls.py principal (o que está na pasta do seu projeto, não no app users), adicione as URLs do seu app users e a configuração para servir arquivos de mídia em desenvolvimento:

# Seu_Projeto_Principal/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Importe a view 'home' do seu app spotify
from spotify.views import home # Ajuste 'spotify' para o nome do seu app principal

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'), # Sua página inicial
    path('accounts/', include('users.urls')), # Inclui as URLs de login/logout do app users
]

# APENAS EM AMBIENTE DE DESENVOLVIMENTO:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

Execute as Migrações do Banco de Dados:

python manage.py makemigrations users
python manage.py makemigrations spotify # Se você tiver modelos no app spotify
python manage.py migrate

Crie um Superusuário (para acesso ao Admin):

python manage.py createsuperuser

Siga as instruções para criar seu usuário administrador.

🚀 Como Rodar o Projeto
Inicie o Servidor de Desenvolvimento:

python manage.py runserver

O servidor estará disponível em http://127.0.0.1:8000/.

Acesse o Painel de Administração:
Vá para http://127.0.0.1:8000/admin/ e faça login com o superusuário que você criou. Você poderá gerenciar os CustomUsers aqui.

Acesse a Tela de Login:
A tela de login está em http://127.0.0.1:8000/accounts/login/.

Acesse a Página Inicial:
A página inicial está em http://127.0.0.1:8000/. Lembre-se que ela exige que o usuário esteja logado. Se você não estiver logado, será redirecionado para a tela de login.

💡 Próximos Passos (Sugestões de Melhoria)
Implementar a funcionalidade de registro de novos usuários.

Adicionar modelos para Músicas, Artistas, Álbuns e Playlists.

Desenvolver a lógica para reprodução de músicas.

Criar páginas de detalhes para artistas, álbuns e playlists.

Melhorar o design e a responsividade do frontend.

Implementar funcionalidades de busca.