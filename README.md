<h3 align="center">Nork-Town Cars</h3>

---

<p align="center"> A small test for Python API development
</p>
<p>
Nork-Town is a weird place. Crows cawk the misty morning while old men squint. It’s a small town, so the mayor had a bright idea to limit the number of cars a person may possess. One person may have up to 3 vehicles. The vehicle, registered to a person, may have one color, ‘yellow’, ‘blue’ or ‘gray’. And one of three models, ‘hatch’, ‘sedan’ or ‘convertible’. Carford car shop want a system where they can add car owners and cars. Car owners may not have cars yet, they need to be marked as a sale opportunity. Cars cannot exist in the system without owners.

Requirements

● Setup the dev environment with docker

○ Using docker-compose with as many volumes as it takes

● Use Python’s Flask framework and any other library

● Use any SQL database

● Secure routes

● Write tests
</p>


##  Running the project

### Prerequisites

What things you need to install the software and how to install them.

```
Python 3.10+
Python 3.6+ (Not Tested)
```

### Installing

A step by step series of examples that tell you how to get a development env running.


1. Get this project

```
git clone https://github.com/raphael-d-cordeiro/advicehealth.git
cd advicehealth
```
##### Without Docker

2. Installing the dependences (virtualenv recommended)

```
pip install -r requirements.txt
```
3. Configure env file

```
cp .env.example .env

# fill .env variables
```

4. Run the server API

```
python server.py
```

5. Check if it is running with curl request

```
curl http://127.0.0.1:5000/hello-world

# Hello World! The API is Running!
```
##### With Docker

2. building the container

```
docker-compose build
```

3. running the container

```
docker-compose up
```

##### With Docker Compose (recommended)

2. build & run

```
docker-compose up -d
```

## Running the tests

To run the Unit Tests with PyTest after installation run in the project folder

```
pytest -v
```

## Usage

Load the Insomnia Collection file "Insomnia_requests_nork_town_cars" and make requests.

## Built Using 

- [Flask](https://flask.palletsprojects.com/) - Web Framework
- [Sqlalchemy](https://www.sqlalchemy.org/) - Database ORM
- [PyTest](https://pytest.org/) - Test Tools
