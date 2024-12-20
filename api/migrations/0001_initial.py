# Generated by Django 4.0.6 on 2024-12-06 02:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('employe_id', models.CharField(max_length=255)),
                ('department', models.CharField(choices=[('Contabilidad', 'Contabilidad'), ('Ventas', 'Ventas'), ('Sistemas', 'Sistemas'), ('Recepción', 'Recepción')], max_length=50)),
                ('hire_date', models.DateField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TimeEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('entry_type', models.CharField(choices=[('IN', 'Entrada'), ('OUT', 'Salida')], max_length=10)),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.worker')),
            ],
        ),
    ]
