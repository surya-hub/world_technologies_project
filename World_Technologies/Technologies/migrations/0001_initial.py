# Generated by Django 3.0 on 2020-06-30 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=100)),
                ('trainer_name', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('start_date', models.DateField()),
                ('content', models.FileField(upload_to='files')),
                ('photo', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='DemoRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('mobile', models.BigIntegerField()),
                ('course', models.CharField(choices=[('Select Course', 'Select Course'), ('PYTHON', 'PYTHON'), ('JAVA', 'JAVA'), ('.NET', '.NET'), ('DJANGO', 'DJANGO'), ('FLASK', 'Flask'), ('REST API', 'REST API'), ('DATA SCIENCE', 'DATA SCIENCE'), ('ML', 'ML'), ('DL', 'DL'), ('AI', 'AI')], default='Select Course', max_length=100)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
    ]
