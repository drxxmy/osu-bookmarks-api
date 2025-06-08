# osu!bookmarks API

## Installing dependencies

While in the projects directory, execute the following command to create a virtual environment and install dependencies:

```bash
$ uv sync
```

## Setup your API keys

In case of questions, first refer to [ossapi documentation](https://tybug.github.io/ossapi/index.html).

### Create OAuth client

First, we’ll need to create an OAuth client.

Navigate to your [settings page](https://osu.ppy.sh/home/account/edit#oauth) and click “New OAuth Application”. You can name it anything you like, but choose a callback url on localhost. For example, http://localhost:3914/. Any port greater than 1024 is fine as long as you don’t choose something another application is using.

When you create the application, it will show you a client id and secret. Take note of these two values.

### Edit .env file

Rename `.env.example` file to `.env` and edit accordingly:

```.env
OSU_CLIENT_ID=your_client_id
OSU_CLIENT_SECRET=your_client_secret
```

## Starting a project

```bash
$ fastapi dev app/main.py
```

## Documentation

After running the FastAPI server, you can access documentation either via [Swagger UI](http://127.0.0.1:8000/api/v1/docs) or [ReDoc](http://127.0.0.1:8000/api/v1/redoc)
