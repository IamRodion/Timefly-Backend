import secrets, os
from dotenv import load_dotenv

def generate_secret_key():
    return ''.join(secrets.choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[]{}|;:,.<>/?') for i in range(50))

def write_file(ALLOWED_HOSTS, DEBUG, CORS_ORIGIN_ALLOW_ALL, CORS_ORIGIN_WHITELIST):
    TEXT = f"""SECRET_KEY = '{generate_secret_key()}'
ALLOWED_HOSTS = {ALLOWED_HOSTS}
DEBUG = {DEBUG}
CORS_ORIGIN_ALLOW_ALL = {CORS_ORIGIN_ALLOW_ALL}
CORS_ORIGIN_WHITELIST = '{CORS_ORIGIN_WHITELIST}'"""
    with open('.env', mode='w+') as file:
        file.write(TEXT)
    # return TEXT

load_dotenv()

enviroment = input("Elige el ambiente para desplegar:\nS para servidor\nP para prueba\n>")

if enviroment.lower() == 'p':
    ALLOWED_HOSTS = "['*']"
    DEBUG = True
    CORS_ORIGIN_ALLOW_ALL = True
    CORS_ORIGIN_WHITELIST = "http://localhost, https://localhost"
    write_file(ALLOWED_HOSTS=ALLOWED_HOSTS, DEBUG=DEBUG, CORS_ORIGIN_ALLOW_ALL=CORS_ORIGIN_ALLOW_ALL, CORS_ORIGIN_WHITELIST=CORS_ORIGIN_WHITELIST)
else:
    ALLOWED_HOSTS = "['iamrodion.pythonanywhere.com']"
    DEBUG = False
    CORS_ORIGIN_ALLOW_ALL = False
    CORS_ORIGIN_WHITELIST = "https://iamrodion.pythonanywhere.com, "
    write_file(ALLOWED_HOSTS=ALLOWED_HOSTS, DEBUG=DEBUG, CORS_ORIGIN_ALLOW_ALL=CORS_ORIGIN_ALLOW_ALL, CORS_ORIGIN_WHITELIST=CORS_ORIGIN_WHITELIST)



# variables = [ os.getenv('SECRET_KEY'), os.getenv('ALLOWED_HOSTS'), bool(os.getenv('DEBUG')), bool(os.getenv('CORS_ORIGIN_ALLOW_ALL')), os.getenv('CORS_ORIGIN_WHITELIST').split(',')]

# for data in variables:
#     print(data)
#     print(type(data))