# Installing dependencies

While in the projects directory, execute the following command to create a virtual environment and install dependencies:

```bash
$ uv sync
```

# Starting a project

```bash
$ fastapi dev app/main.py
```

# Documentation

After running the FastAPI server, you can access documentation either via [Swagger UI](http://127.0.0.1:8000/api/v1/docs) or [ReDoc](http://127.0.0.1:8000/api/v1/redoc)
