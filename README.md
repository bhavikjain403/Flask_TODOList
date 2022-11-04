TO-DO List developed using Flask

Steps to run : 
1. Install virtual environment : pip install virtualenv
2. Create virtual environment : virtualenv env
3. Activate virtual environment : env/Scripts/activate
4. Install flask and flask_sqlalchemy : pip install flask flask_sqlalchemy
5. To setup database : flask shell
                   >>> db.create_all()
6. The setup is complete. To run : python app.py