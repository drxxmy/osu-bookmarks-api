# osu!bookmarks API 📌

![Python Version](https://img.shields.io/badge/python-3.13%2B-blue)
![UV](https://img.shields.io/badge/package_installer-uv-FFD43B?logo=python)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen)

A modern Python project with FastAPI, SQLAlchemy, and osu! API integration.

### Built With 💙

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?logo=fastapi)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1E4C62?logo=sqlalchemy)

## Table of Contents 📖

- [Install dependencies](#dependencies)
- [Setup API keys](#api-keys)
- [Usage](#usage)
- [Documentation](#documentation)

## Dependencies 🛠️

While in the projects directory, execute the following command to create a virtual environment and install dependencies:

```bash
$ uv sync
```

## API keys 🔒

In case of questions, first refer to [ossapi documentation](https://tybug.github.io/ossapi/index.html).

### 1. Create OAuth client

First, we’ll need to create an OAuth client.

Navigate to your [settings page](https://osu.ppy.sh/home/account/edit#oauth) and click “New OAuth Application”. You can name it anything you like, but choose a callback url on localhost. For example, http://localhost:3914/. Any port greater than 1024 is fine as long as you don’t choose something another application is using.

When you create the application, it will show you a client id and secret. Take note of these two values.

### 2. Edit .env file

Rename `.env.example` file to `.env` and edit accordingly:

```.env
OSU_CLIENT_ID=your_client_id
OSU_CLIENT_SECRET=your_client_secret
```

## Usage 🖥️

Start API server by executing:

```bash
$ fastapi dev app/main.py
```

## Documentation 📄

After running the FastAPI server, you can access documentation either via [Swagger UI](http://127.0.0.1:8000/api/v1/docs) or [ReDoc](http://127.0.0.1:8000/api/v1/redoc)
