# Generated by Django 3.1.7 on 2021-03-27 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=50)),
                ('admin_first_name', models.CharField(max_length=50)),
                ('admin_last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ScenarioChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source1', models.CharField(max_length=50)),
                ('source2', models.CharField(max_length=50)),
                ('target1', models.CharField(max_length=50)),
                ('value', models.DecimalField(decimal_places=2, max_digits=5)),
                ('target2', models.CharField(max_length=50)),
                ('unit', models.CharField(default='what up!', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SupplyChainSelection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supply_chain', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
                ('primary', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('organization', models.CharField(max_length=50)),
            ],
        ),
    ]
