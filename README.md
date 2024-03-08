# What is this?

This is a ready-to-production application made with Python and Postgres.
It can do:
- User IAM (Identity and Access Management): 
    - User Creation
    - User Delete
    - User Data Update
    - User Login
- Raw Data Operations in a Postgres Database:
    - Data Creation
    - Data Grabbing
    - Data Delete

Data are considered as "per user" so each user can access only Its data.<br/>
All operation can be done only once an user has authenticated.<br/>
There are 2 level of users:
- administrator: have access to all the data
- non administrator: have access to their data
<br/>

All data are saved as is in a postgres table and can be in JSON format (and json serializable) without limitation of lenght.
<br/>
All user information are saved as is except for sensitive information (like passwords) that are **encrypted** first and then saved into database.
<br/><br/>
***No sensitive data is stored or printed. Only after encrypting, they are saved into Postgres database. Password matching is made with encrypted password to limitate password encrypt-decrypt***
<br/>

## There's more
This code is ready for production (except for environment variables that must be defined in production server) and comes with:
- Robust Endpoint with input and output data validaiton using Pydantic Schemas
- Oauth2 with Bearer toker
- Database versioning with Alembic
- Gunicorn service setting definition
- NGINX reverse proxy setting definition
- Dokerfile and docker-compose.yml


## Future Developing

To make a more robust production environment and enhance the application capabilities:
- Data saving frequency and lenght limitation based on user role (licensing)
- Add more specific database tables (even if a single data table is the aim of this simple and raw data saving project)
- create a robust production logging system, potentially using an external centralized logging server
- Add Google (and others) Sign up and Sign in methods integrated 