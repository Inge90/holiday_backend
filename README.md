# holiday backend with fastapi

Here is video code exaple , we'll walk you through the process of building a holiday API using FastAPI.
https://youtu.be/FtC8HfR-lRw 
 

Install packages with pip:

```
pip3 install passlib[bcrypt] SQLAlchemy fastapi[all] pyjwt
```

or

```
pip3 install -r requirements.txt
```

Back end code you can run, under this rule

```
  uvicorn main:app --reload
```

Can view api doc in a local browser:
http://localhost:8000/docs

The recommendation is to set up a virtual virtual environment.

Creation of virtualenv:

```Language
virtualenv -p python3 <desired-path>
```

Activate the virtualenv:

```Language
source <desired-path>/bin/activate

source venv/bin/activate

```

Deactivate the virtualenv:

```Language
deactivate
```
