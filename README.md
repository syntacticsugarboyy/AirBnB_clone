The Airbnb project by Jareeyah and Great:

0. Write a README.md and AUTHORS file at the root of your repository

1. Write beautiful code that passes the pycodestyle checks

2. All your files, classes, functions must be tested with unit tests

3. Write a class BaseModel that defines all common attributes/methods for other classes

4. Update models/base_model.py

5. Write a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances
- Update models/__init__.py: to create a unique FileStorage instance for your application
- Update models/base_model.py: to link your BaseModel to FileStorage by using the variable storage

6. Write a program called console.py that contains the entry point of the command interpreter

7. Update your command interpreter (console.py) to have these commands

8. Write a class User that inherits from BaseModel

9. Write all those classes that inherit from BaseModel 
