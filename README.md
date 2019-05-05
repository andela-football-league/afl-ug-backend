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

Create Application environment variables and save them in .env file
```
APP_SETTINGS=development # Set app environment
DEBUG=True
DB_NAME=development_db # Db for development
DB_USER=postgres # Db user
DB_PASS=password # Db password
DB_PORT=5432
PORT=5000
TEST_DB_NAME=test_db # Db for testing
USER_TOKEN=user-jwt-token # jwt-token for user
```

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

Run tests
```
docker exec -it <app-container-name> pytest -v
```

Tests with converage
```
docker exec -it <app-container-name> coverage run -m pytest -v
docker exec -it <app-container-name> coverage report
docker exec -it <app-container-name> converage html
```