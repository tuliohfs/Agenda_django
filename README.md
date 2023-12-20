Django Event Agenda
Este projeto Django é uma aplicação simples para gerenciar eventos, permitindo que os usuários autenticados possam criar, visualizar, editar e excluir eventos em uma agenda. A aplicação possui uma interface amigável e funcionalidades básicas para manusear eventos.

Funcionalidades
Lista de Eventos: Visualize uma lista de eventos futuros, filtrados com base na data atual e no usuário logado.
Detalhes do Evento: Visualize detalhes de um evento específico.
Criação e Edição: Adicione novos eventos ou edite eventos existentes, incluindo título, data e descrição.
Exclusão: Remova eventos que não são mais necessários.
Requisitos de Configuração
Antes de executar a aplicação, certifique-se de ter o ambiente configurado corretamente:

Python
Django
Banco de dados configurado no arquivo settings.py
Dependências do projeto instaladas (consulte o arquivo requirements.txt)
Instalação e Execução
Clone este repositório:

bash
Copy code
git clone https://github.com/tuliohfs/agenda_django.git
Navegue até o diretório do projeto:

bash
Copy code
cd agenda_django
Execute as migrações para configurar o banco de dados:

bash
Copy code
python manage.py migrate
Inicie o servidor de desenvolvimento:

bash
Copy code
python manage.py runserver
Acesse a aplicação em http://localhost:8000/Agenda/

Rotas Principais
/Agenda/: Lista de eventos futuros.
/Agenda/evento/: Detalhes de um evento específico.
/Agenda/evento/submit: Página para criar ou editar um evento.
/Agenda/eventos/delete/<int:id_evento>/: Exclui um evento.
/login/: Página de login.
/logout/: Encerra a sessão do usuário.
