

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommitteesCharis',
            fields=[
                ('id_committees_charis', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_committees_charis', models.CharField(blank=True, default='nothing', max_length=45, null=True)),
                ('passwords', models.CharField(blank=True, max_length=45, null=True)),
                ('bu_id', models.IntegerField()),
            ],
            options={
                'db_table': 'committees_charis',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id_department', models.AutoField(primary_key=True, serialize=False)),
                ('name_department', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'department',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id_doctors', models.AutoField(db_column='id_Doctors', primary_key=True, serialize=False)),
                ('name_doctors', models.CharField(blank=True, db_column='name_Doctors', max_length=45, null=True)),
                ('passwords', models.CharField(blank=True, max_length=45, null=True)),
                ('id_bu', models.IntegerField()),
            ],
            options={
                'db_table': 'doctors',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id_evaluation', models.AutoField(db_column='id_Evaluation', primary_key=True, serialize=False)),
                ('file_evaluation', models.FileField(db_column='file_evaluation_dr1', upload_to='doucment')),
                ('file_evaluation_dr2', models.FileField(db_column='file_evaluation_dr2', upload_to='doucment')),
                ('file_evaluation_dr3', models.FileField(db_column='file_evaluation_dr3', upload_to='doucment')),
            ],
            options={
                'db_table': 'evaluation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Examiners',
            fields=[
                ('id_examiners', models.AutoField(db_column='id_Examiners', primary_key=True, serialize=False)),
                ('name_examiners', models.CharField(blank=True, db_column='name_Examiners', max_length=45, null=True)),
            ],
            options={
                'db_table': 'examiners',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id_groups', models.AutoField(db_column='id_groups', primary_key=True, serialize=False)),
                ('name_groups', models.CharField(blank=True, db_column='name_Groups', max_length=45, null=True)),
            ],
            options={
                'db_table': '_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id_projects', models.AutoField(db_column='id_Projects', primary_key=True, serialize=False)),
                ('name_projects', models.CharField(blank=True, db_column='title_projects', max_length=45, null=True)),
                ('filled_projects', models.CharField(blank=True, max_length=45, null=True)),
                ('descriotion_projects', models.CharField(blank=True, max_length=45, null=True)),
                ('file_project', models.FileField(db_column='File_Project', upload_to='doucment')),
                ('status', models.CharField(choices=[('avilable', 'avilable'), ('anvilable', 'anvilable')], max_length=50)),
            ],
            options={
                'db_table': 'projects',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id_students', models.AutoField(db_column='id_Students', primary_key=True, serialize=False)),
                ('name_Students', models.CharField(blank=True, max_length=45, null=True)),
                ('passwords', models.CharField(blank=True, max_length=45, null=True)),
                ('bu_id', models.IntegerField()),
            ],
            options={
                'db_table': 'students',
                'managed': False,
            },
        ),
    ]
