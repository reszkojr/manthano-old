<img src="https://github.com/reszkojr/manthano/assets/67809084/695f3150-4798-4d17-a182-8fac8d4f9625" width="500" alt="manthano-light" style="max-width: 100%; padding-bottom: 200px;">

> A virtual environment for learning and sharing resources.

![manthano landing](https://github.com/reszkojr/manthano/assets/67809084/45103725-480e-4f79-af06-6a61e6b3858a)

## What is it?

Manthano is a platform that helps students to study and understand subjects using specific functions designed to share and review study material.


## What are its functions? (in progress)
 - Scan documents and convert them to PDF;
 - Creation of study channels;
 - File share;
 - Integration with Google Forms;
 - Class' timetable;
 - Class' calendar;
 - Jitsi meetings API (Discord-like videocalls);
 - Google Jamboards integration.

# Installation

Programs required to run Manthano:


- Python >= 3
- PostgreSQL >= 9
- NodeJS >= 14.10 (Tailwind)

Settings required to install Manthano in your computer:

```bash
git clone https://github.com/reszkojr/manthano
```

#### Python modules:

```bash
pip install -r requirements.txt
```

#### Database (Docker):

```bash
docker pull redis
docker pull postgres

# Run the containers
docker run --name redis -d redis
docker run --name postgres -d -p 5432:5432 -e POSTGRES_PASSWORD=1030 postgres:alpine
```

# Running

Beforehand, a few setup commands are required in order to run Manthano in your computer:

#### Tailwind:
```bash
# Installing django-tailwind requirements:
python manage.py tailwind install

# Start Tailwind live reload:
python manage.py tailwind start

# Or, just build the CSS file:
python manage.py tailwind build
```

### Migrating Django's migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

#### Running the server

```bash
python manage.py runserver <port>
```


