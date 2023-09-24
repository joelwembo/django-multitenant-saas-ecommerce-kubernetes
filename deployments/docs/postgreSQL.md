# Docker & PostgreSQL

Url : http://localhost:5051/browser/

PGADMIN_DEFAULT_EMAIL: infrastructure.engineering@prodxengine.com
PGADMIN_DEFAULT_PASSWORD: abcde@12345

# Pgadmin Connection Settings Properties

Name : finengine.io

Host name/address :  db
Port : 5432

Maintenance Ddatabse: postgres

Main Databse : fintech_enterpriseDB

Username : joelwembo

Password : abcde@12345


# Docker Compose Settings

db:
    restart: always
    image: postgres
    container_name: fintech_enterpriseDB_postgre
    volumes:
      - ./data/db:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=fintech_enterpriseDB
      - POSTGRES_USER=joelwembo
      - POSTGRES_PASSWORD=abcde@12345
      - POSTGRES_PORT=5432
      - "POSTGRES_HOST_AUTH_METHOD=trust"
    # expose:
      # - "5433"
    # ports:
    #   - "5433:5433" 
  pgadmin:
      restart: always 
      image: dpage/pgadmin4
      container_name: fintech-pgadmin #you can change this
      depends_on:
        - db
      ports:
        - "5051:80"
      environment:
        PGADMIN_DEFAULT_EMAIL: infrastructure.engineering@prodxengine.com
        PGADMIN_DEFAULT_PASSWORD: abcde@12345

# Django Settings.py 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fintech_enterpriseDB',
        'USER': 'joelwembo',
        'PASSWORD': 'abcde@12345',
        'HOST': 'db',
        'PORT': 5432,
    }
}




