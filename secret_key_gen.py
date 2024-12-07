import secrets

def generate_secret_key():
    return ''.join(secrets.choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[]{}|;:,.<>/?') for i in range(50))

# Genera una nueva clave y la almacena en una constante
SECRET_KEY = generate_secret_key()
# print(secret_key)
with open('.env', mode='w+') as file:
    file.write("SECRET_KEY = '{}'".format(SECRET_KEY))