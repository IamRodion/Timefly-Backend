import secrets, os
from dotenv import load_dotenv, set_key

ENV_PATH = '.env'
load_dotenv()

def generate_secret_key()-> str:
    """Genera un string largo aleatoriamente"""
    return ''.join(secrets.choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[]{}|;:,.<>/?') for i in range(50))

set_key(ENV_PATH, 'SECRET_KEY', generate_secret_key())

ENVIRONMENT = input("Elige el ambiente para desplegar:\n[1] Producción\n[2] Desarrollo\n>")

if ENVIRONMENT == '1':
    ALLOWED_HOSTS = input("Indique los host permitidos (* para permitir todos):\n>")
    CORS_ORIGIN_WHITELIST = input("Indique los orígenes permitidos (Use 'http://localhost' para permitir el mismo servidor):\n>")

    set_key(ENV_PATH, 'ENVIRONMENT', 'production')
    set_key(ENV_PATH, 'ALLOWED_HOSTS', ALLOWED_HOSTS)
    set_key(ENV_PATH, 'CORS_ORIGIN_WHITELIST', CORS_ORIGIN_WHITELIST)
    
    print("[!] Se configuró el ambiente para producción")
elif ENVIRONMENT == '2':
    set_key(ENV_PATH, 'ENVIRONMENT', 'dev')
    print("[!] Se configuró el ambiente para desarrollo")
else:
    print("[!] La opción indicada es incorrecta, no se desplegó ni configuró el ambiente.")