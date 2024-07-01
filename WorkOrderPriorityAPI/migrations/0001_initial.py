# Generated by Django 4.1.13 on 2024-06-28 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddedWorkOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.IntegerField()),
                ('woNumber', models.IntegerField()),
                ('description', models.TextField()),
                ('requestedBy', models.TextField()),
                ('resourcePriority', models.TextField()),
                ('notes', models.TextField()),
                ('area', models.TextField(choices=[('jyd', 'JYD'), ('sprayDry', 'Spray Dry'), ('tableting', 'Tableting'), ('nonProduction', 'Non-Production')])),
                ('category', models.TextField(choices=[('controls', 'Controls'), ('mes', 'MES'), ('maintenance', 'Maintenance'), ('other', 'Other')])),
                ('status', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('capacity', models.IntegerField()),
                ('category', models.TextField(choices=[('controls', 'Controls'), ('mes', 'MES'), ('maintenance', 'Maintenance'), ('other', 'Other')])),
            ],
        ),
        migrations.CreateModel(
            name='UnaddedWorkOrder',
            fields=[
                ('actual_hours', models.FloatField(blank=True, null=True)),
                ('attachment_count', models.IntegerField()),
                ('category', models.IntegerField()),
                ('closed', models.BooleanField()),
                ('closed_date', models.DateTimeField(blank=True, null=True)),
                ('costcenter', models.IntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(blank=True)),
                ('createdby', models.CharField(blank=True, max_length=150, null=True)),
                ('createdbyuser', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(max_length=50)),
                ('dispatch', models.IntegerField(blank=True, null=True)),
                ('due_date', models.DateTimeField(blank=True, null=True)),
                ('estimated_cost', models.DecimalField(decimal_places=4, max_digits=19, null=True)),
                ('estimated_hours', models.FloatField(blank=True, null=True)),
                ('external_cost', models.DecimalField(decimal_places=4, max_digits=19, null=True)),
                ('externalid', models.CharField(blank=True, max_length=50, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('instructions', models.TextField()),
                ('labor_cost', models.DecimalField(decimal_places=4, max_digits=19, null=True)),
                ('lastupdated', models.DateTimeField(blank=True)),
                ('lastupdatedby', models.CharField(blank=True, max_length=150, null=True)),
                ('lastupdatedbyuser', models.IntegerField(blank=True, null=True)),
                ('launch_date', models.DateTimeField(blank=True, null=True)),
                ('machine', models.IntegerField()),
                ('number', models.CharField(max_length=50)),
                ('owner', models.IntegerField(blank=True, null=True)),
                ('owner_assigned_date', models.DateTimeField(blank=True, null=True)),
                ('parent_dispatch', models.IntegerField(blank=True, null=True)),
                ('parent_fives', models.IntegerField(blank=True, null=True)),
                ('parent_kaizen', models.IntegerField(blank=True, null=True)),
                ('parent_sigevent', models.IntegerField(blank=True, null=True)),
                ('parent_workorder', models.IntegerField(blank=True, null=True)),
                ('priority', models.IntegerField()),
                ('project_workorder', models.BooleanField()),
                ('projectid', models.CharField(blank=True, max_length=50, null=True)),
                ('requested_due_date', models.DateTimeField()),
                ('requestedby', models.CharField(max_length=50)),
                ('requestedby_phone', models.CharField(blank=True, max_length=50, null=True)),
                ('scheduled_date', models.DateTimeField(blank=True, null=True)),
                ('site', models.IntegerField()),
                ('spares_cost', models.DecimalField(decimal_places=4, max_digits=19, null=True)),
                ('spares_estimate', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('status', models.IntegerField()),
                ('status_date', models.DateTimeField(null=True)),
                ('total_cost', models.DecimalField(decimal_places=4, max_digits=19, null=True)),
                ('trade', models.IntegerField()),
            ],
        ),
    ]
