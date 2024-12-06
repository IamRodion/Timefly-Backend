import secrets

def generate_secret_key():
    return ''.join(secrets.choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[]{}|;:,.<>/?') for i in range(50))

# Generar una nueva clave y almacenarla en una variable
secret_key = generate_secret_key()
print(secret_key)