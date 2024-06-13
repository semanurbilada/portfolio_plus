<div align="center">
    <img src="https://img.icons8.com/?size=100&id=FnTmHRua3mU3&format=png&color=000000" alt="icon">
</div>

<h1 align="">Portfolio Plus | Django CV Page</h1>

*  [TO DO](#hash-todo)
*  [Purpose](#hash-purpose)
*  [Preview](#hash-preview)
*  [How To Run?](#hash-how-to-run)
    *  [Docker Scripts](#hash-docker-scripts)
*  [Licence](#hash-licence)


## :hash: TO DO
- [x] Frontend: customizations
- [x] Database models: all datas 
- [x] Set up: docker environment
- [x] Frontend: bootstrap template
- [x] Set up: django project & github repo


# :hash: Purpose
<div align="justify">
Welcome to my Portfolio Website! Here is the Django CV page project for the technical lecture of Advanced Web Programming. Main purpose is the learning and practicing;<br>
- Django in backend applications,<br>
- Docker container and enviroment,<br>
- Bootstrap which is a framework of CSS.<br>
Take a look at my learning journey for Django & Bootstrap & Docker; and feel free to send feedback!
</div>


# :hash: Preview
<div align="center">
   
![Screenshot 2024-05-24 at 2 38 18 AM](https://github.com/semanurbilada/portfolio_plus/assets/96194982/9fbbff0a-2b67-4d64-8021-2ae1a06ce282)
![Screenshot 2024-05-24 at 2 38 26 AM](https://github.com/semanurbilada/portfolio_plus/assets/96194982/cf75919e-3b24-4cb3-bef1-db4bf75e22fd)
![Screenshot 2024-05-24 at 2 38 39 AM](https://github.com/semanurbilada/portfolio_plus/assets/96194982/c019b20a-ec92-411e-86d2-a0da4d5c221f)
![Screenshot 2024-05-24 at 2 38 46 AM](https://github.com/semanurbilada/portfolio_plus/assets/96194982/c7f48401-8ed0-42ef-b804-e01941d63ff9)
![Screenshot 2024-05-24 at 2 38 57 AM](https://github.com/semanurbilada/portfolio_plus/assets/96194982/232b8e0f-5538-4ccb-a8cb-8fb95544eb50)
![Screenshot 2024-05-24 at 2 39 03 AM](https://github.com/semanurbilada/portfolio_plus/assets/96194982/27d1fac1-5b2b-4a19-992f-209a33c06108)

</div>


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
1. ```Build and run the app:```
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

7. Create superuser with docker:
```
docker-compose run app python3 manage.py createsuperuser
```

## :hash: Licence

This project is licensed under the MIT License - see the [LICENSE](https://github.com/semanurbilada/portfolio_plus?tab=MIT-1-ov-file#readme) file for details.