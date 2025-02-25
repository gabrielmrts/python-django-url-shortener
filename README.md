# Encurtador de URL com Django REST Framework

## Sobre o Projeto
Este projeto é uma API de encurtamento de URLs desenvolvida com **Django REST Framework**. Ele permite que os usuários enviem uma URL longa e obtenham uma versão encurtada, além de redirecionar os acessos para a URL original e contar o número de acessos.

## Tecnologias Utilizadas
- Python 3.13
- Django 3.13
- Django REST Framework
- SQLite (padrão, mas pode ser alterado para PostgreSQL ou MySQL)

## Como Rodar o Projeto
### 1. Clonar o Repositório
```sh
git clone https://github.com/gabrielmrts/python-django-url-shortener.git
cd python-django-url-shortener
```

### 2. Criar um Ambiente Virtual e Ativá-lo
```sh
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```

### 3. Instalar as Dependências
```sh
pip install -r requirements.txt
```

### 4. Criar o Banco de Dados
```sh
python manage.py migrate
```

### 5. Rodar o Servidor
```sh
python manage.py runserver
```

## Endpoints da API

### 1. Encurtar uma URL
**Endpoint:** `POST /api/urls/`

**Corpo da Requisição (JSON):**
```json
{
  "original_url": "https://www.exemplo.com"
}
```

**Resposta de Sucesso (JSON):**
```json
{
  "short_code": "abc123",
  "original_url": "https://www.exemplo.com",
  "created_at": "2025-02-25T12:00:00Z",
  "access_count": 0
}
```

---

### 2. Redirecionar para a URL Original
**Endpoint:** `GET /api/urls/{short_code}/`

**Exemplo:**
```sh
GET http://127.0.0.1:8000/api/urls/abc123/
```

**Resposta de Sucesso:**
```json
{
  "redirect_to": "https://www.exemplo.com"
}
```

**Erro se o código não existir:**
```json
{
  "error": "URL not found."
}
```

## Estrutura do Projeto
```
shortener/
│── shortener/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── services.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│── app/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│── manage.py
│── README.md
│── requirements.txt
```

## Melhorias Futuras
- Adicionar suporte a usuários e autenticação
- Criar um painel de administração para visualizar estatísticas
- Implementar tempo de expiração para links encurtados
- Suporte para customização de códigos curtos

## Licença
Este projeto está licenciado sob a **MIT License**.

