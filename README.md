<h1 align="">Portfolio Plus | Django CV Page</h1>

<div align="center">
<img src="https://cdn-icons-png.flaticon.com/512/8644/8644474.png" width="180" height="180" alt="icon">
</div>

*  [TO DO](#hash-todo)
*  [Purpose](#hash-purpose)
*  [Preview](#hash-preview)
*  [How To Run?](#hash-how-to-run)
    *  [Docker Scripts](#hash-docker-scripts)
*  [Database Management System](#hash-database-management-system)

## :hash: TO DO
- [ ] Frontend: customizations -> WIP
- [ ] Database models: all datas -> WIP
- [ ] Contact app: frontend last 2 videos
- [x] Set up: project & github repo
- [x] Frontend: bootstrap template

# :hash: Purpose
<div align="justify">
Welcome to my Portfolio Website! Here is the Django CV page project for the technical lecture of Advanced Web Programming. Main purpose is the learning and practicing;<br>
- Django in backend applications,<br>
- Bootstrap which is a framework of CSS,<br>
- Docker.<br>
Still in progress, and there are lots of aspect to be waiting for developing. Stay Tuned!
</div>


# :hash: Preview


# :hash: How To Run?
1. Virtual environment setup:
```
python3 -m venv environment_name
```

2. To activate the virtual environment (Windows):
```
environment_name/Scripts/activate
```

3. To activate the virtual environment (Linux / MacOS):
```
source environment_name/bin/activate
```

4. Install dependencies:
```
pip install -r requirements.txt
```
or
```
pip3 install -r requirements.txt
```

5. Run:
```
python manage.py runserver
```
or
```
python3 manage.py runserver
```

- Note: For deactivating python enviroment:
```
deactivate
```
or in MacOS / Linux:
```
source deactivate
```

## :hash: Docker Scripts:
1. Build and run the app:
```
docker-compose up --build
```
or 
```
docker compose up --build
```

2. Build and run the app in the background:
```
docker-compose up --build -d
```

3. See current runs with container IDs:
```
docker ps
```

4. Stop the run:
```
docker stop <container_id>
```

5. Stop and remove the run:
```
docker-compose stop <container_id>
```

6. About migrations:
- Create a new migration from models;
```
docker-compose run app python3 manage.py makemigrations 
```

- Apply migrations to database;
```
docker-compose run app python3 manage.py migrate
```

6. Create superuser with docker:
```
docker-compose run app python3 manage.py createsuperuser
```


# :hash: Database Management System
