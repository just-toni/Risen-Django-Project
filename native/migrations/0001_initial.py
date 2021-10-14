# Generated by Django 3.2.7 on 2021-09-28 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cohort', '0002_alter_cohort_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Native',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('scvn', models.CharField(max_length=10, null=True)),
                ('image', models.ImageField(upload_to='image/')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('cohort', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cohort.cohort')),
            ],
        ),
    ]