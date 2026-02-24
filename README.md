# Estrutura
1- Criar pasta hospital-api-drf
2- Criar repositório no GitHub
3- Instalar o Python versão mais recente

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
.\venv\Scripts\activate

# Desativar ambiente virtual
deactivate

# Atualizar o pip (dentro do venv)
python.exe -m pip install --upgrade pip

# Verificar a versão do pip (dentro do venv)
pip -V

# Verificar a versão do Python (dentro do venv)
py -V

# Instalar o Django (dentro do venv)
pip install django

# Atualizar o Django (dentro do venv)
pip install --upgrade django

# Verificar a versão do Django (dentro do venv)
django-admin --version

# Atualizar o pip, setuptools e wheel (dentro do venv)
py -m pip install pip setuptools wheel --upgrade

# Criar o requirements.txt (dentro do venv)
pip freeze > requirements.txt

# Criar o projeto Django (dentro do venv)
django-admin startproject .

# Rodar o servidor de desenvolvimento (dentro do venv)
py manage.py runserver

# Configurações do GIT
git config --global user.name "Leonardo de Andrade Oliveira"
git config --global user.email "leonardo.esportemental@gmail.com"
git config --global init.defaultBranch main
git init
ssh-keygen
git remote add origin git@github.com:LeoAnDev/hospital-api-drf.git