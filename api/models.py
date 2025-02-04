from django.db import models

# Create your models here.
class Worker(models.Model):

    DEPARTMENTS = [
        ('Contabilidad', 'Contabilidad'),
        ('Ventas', 'Ventas'),
        ('Sistemas', 'Sistemas'),
        ('Recepción', 'Recepción')
    ]

    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()
    employee_id = models.CharField(max_length=255)
    department = models.CharField(max_length=50, choices=DEPARTMENTS)
    hire_date = models.DateField()
    active = models.BooleanField(default=True)

    def __str__(self):
        # Definiendo la estructura del nombre que mostrará el objeto al ser llamado sin atributos
        return f"{self.firstname}, {self.lastname}"


class TimeEntry(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    #time = models.DateTimeField(auto_now=True)
    time = models.DateTimeField(auto_now_add=True)
    entry_type = models.CharField(max_length=10, choices=[('IN', 'Entrada'), ('OUT', 'Salida')])

    def __str__(self):
        # Definiendo la estructura del nombre que mostrará el objeto al ser llamado sin atributos
        return f"{self.worker} registró su {self.entry_type} el {self.time}"