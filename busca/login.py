import os
def login_data():

    login = {
        'username' : os.getenv('USER'),
        'password' : os.getenv('PASSWORD')
    }

    return login