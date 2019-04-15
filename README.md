# Andela Football League ug

## Technology Stack
- Python 3
- Flask
- PostgreSQL
- Docker: For local development

## Installation

clone the project
```
git clone https://github.com/andela-football-league/afl-ug-backend.git
cd afl-ug-backend
```

Make sure that you have docker installed on your machine


Build project with docker-compose
```
docker-compose build
```

Start development server
```
docker-compose up
```

Run migrations
```
docker-compose build
docker-compose up -d
docker exec -it <app-container-name> python manage.py db init
docker exec -it <app-container-name> python manage.py db migrate
docker exec -it <app-container-name> python manage.py db upgrade
```

Access database via the shell
```
docker exec -it <db-container-name> psql -U postgres
```