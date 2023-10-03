## Migrations:
`poetry add alembic`
`alembic init alembic` . It will init the alembic inside alembic folder

provide the database connection string in the alembic.ini file 

### Generate Migrations:
Provide the models configuration in the alembic/env.py file.
`target_metadata = Base.metadata`

Run this command to generate the migrations `alembic revision --autogenerate`

Use -m to provide the name of the migration file: `alembic revision --autogenerate -m "Create users table"`

Run migrations: `alembic upgrade head`
To Rollback all the migration: `alembic downgrade base`

We can provide a specific file name of migrations to upgrade or downgrade to that file.



## Database Setup:
`poetry add pymsql`
Provide the configuration in the db setup file like this: 
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:password@localhost/fastapi"

### Drivers for MySQL
1. Sync Driver: pymysql
2. Async Driver: aiomysql