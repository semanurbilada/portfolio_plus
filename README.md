<div align="center">
<img src="https://cdn-icons-png.flaticon.com/512/8644/8644474.png" width="180" height="180" alt="icon">
</div>

<h1 align="center">Portfolio Plus</h1>

*  [:hash: Purpose](#hash-purpose)
*  [:hash: How To Run?](#hash-how-to-run)
*  [:hash: Database Management System](#hash-database-management-system)

# :hash: Purpose
Welcome to my Portfolio Website (plus)! Here is started with the idea of Django CV page project from the lecture of Advanced Web Programming, then combined with [existing frontend `portfolio-website`](https://github.com/semanurbilada/portfolio-website) project.

Still in progress, and there are lots of aspect to be waiting for developing. Stay Tuned!

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

## Docker Scripts:
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

# :hash: Database Management System
