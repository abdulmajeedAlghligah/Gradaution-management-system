from django.db import models

# Create your models here.

from django.db import models

# Create your models here .

class Department(models.Model):
    id_department = models.AutoField(primary_key=True)
    name_department = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return str(self.name_department)

    class Meta:
        managed = False
        db_table = 'department'






class CommitteesCharis(models.Model):
    id_committees_charis = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name_committees_charis = models.CharField(max_length=45, blank=True, null=True,default="nothing")
    passwords = models.CharField(max_length=45, blank=True, null=True)
    id_department_fk = models.ForeignKey(Department, models.DO_NOTHING, db_column='id_department_fk', blank=True, null=True)
    bu_id = models.IntegerField(blank=False, null=False)
    def __str__(self):
        return str(self.id_committees_charis)

    class Meta:
        managed = False
        db_table = 'committees_charis'


class Groups(models.Model):
    id_groups = models.AutoField(db_column='id_groups',primary_key=True)
    name_groups = models.CharField(db_column='name_Groups', max_length=45, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.id_groups)
    # def __str__(self):
    #     return (self.name_groups)



    class Meta:
        managed = False
        db_table = '_groups'


class Doctors(models.Model):
    id_doctors = models.AutoField(db_column='id_Doctors', primary_key=True)  # Field name made lowercase.
    name_doctors = models.CharField(db_column='name_Doctors', max_length=100, blank=True, null=True)  # Field name made lowercase.
    passwords = models.CharField(max_length=100, blank=True, null=True)
    id_department_fk = models.ForeignKey(Department, models.DO_NOTHING, db_column='id_department_fk', blank=True, null=True)
    id_groups_fk = models.ForeignKey(Groups, models.DO_NOTHING, db_column='id_Groups_fk', blank=True, null=True,default=0)  # Field name made lowercase.
    id_bu = models.IntegerField(blank=False, null=False)
    def __str__(self):
        return str(self.name_doctors)

    class Meta:
        managed = False
        db_table = 'doctors'


class Projects(models.Model):
    status_project=[
        ('avilable','avilable'),
        ('anvilable','anvilable'),
    ]
    id_projects = models.AutoField(db_column='id_Projects', primary_key=True)  # Field name made lowercase.
    name_projects = models.CharField(db_column='title_projects',max_length=100, blank=True, null=True)
    filled_projects = models.CharField(max_length=1000, blank=True, null=True)
    descriotion_projects = models.CharField(max_length=1000, blank=True, null=True)
    id_groups_fk = models.ForeignKey(Groups, models.DO_NOTHING, db_column='id_Groups_fk', blank=True, null=True)  # Field name made lowercase.
    id_Doctors_fk=models.ForeignKey(Doctors,models.DO_NOTHING,db_column='id_Doctors_fk',blank=True,null=True)
    file_project = models.FileField(upload_to='doucment',db_column='File_Project') # Field name made lowercase.
    status=models.CharField(max_length=50,choices=status_project,blank=False, null=False)
    id_department_fk = models.ForeignKey(Department, models.DO_NOTHING, db_column='id_department_fk', blank=False, null=False)

    def __str__(self):
        return str(self.id_projects)
    class Meta:
        managed = False
        db_table = 'projects'


class Evaluation(models.Model):
    id_evaluation = models.AutoField(db_column='id_Evaluation', primary_key=True)  # Field name made lowercase.
    file_evaluation = models.FileField(upload_to='doucment',db_column='file_evaluation_dr1',blank=True, null=True)
    id_groups_fk = models.ForeignKey(Groups, models.DO_NOTHING, db_column='id_Groups_fk', blank=True, null=True)  # Field name made lowercase.
    id_doctor_fk = models.ForeignKey(Doctors, models.DO_NOTHING, db_column='id_doctor_fk', blank=True, null=True   ,related_name='Eval1')
    id_doctor_fk2 = models.ForeignKey(Doctors, models.DO_NOTHING, db_column='id_doctor_fk2', blank=True, null=True ,related_name='Eval2')
    id_doctor_fk3 = models.ForeignKey(Doctors, models.DO_NOTHING, db_column='id_doctor_fk3', blank=True, null=True ,related_name='Eval3')  # Field name made lowercase.
    file_evaluation_dr2 = models.FileField(upload_to='doucment',db_column='file_evaluation_dr2',blank=True , null=True)
    file_evaluation_dr3 = models.FileField(upload_to='doucment',db_column='file_evaluation_dr3',blank=True, null=True)
    id_department = models.ForeignKey(Department, models.DO_NOTHING, db_column='id_department', blank=False, null=False)
    def __str__(self):
        return str(self.id_evaluation)


    class Meta:
        managed = False
        db_table = 'evaluation'








class Examiners(models.Model):
    id_examiners = models.AutoField(db_column='id_Examiners', primary_key=True)  # Field name made lowercase.
    name_examiners = models.CharField(db_column='name_Examiners', max_length=100, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return str(self.id_examiners)
    class Meta:
        managed = False
        db_table = 'examiners'






class Students(models.Model):
    id_students = models.AutoField(db_column='id_Students', primary_key=True)
    name_Students = models.CharField(max_length=1000, blank=True, null=True)  # Field name made lowercase.
    passwords = models.CharField(max_length=1000, blank=True, null=True)
    id_groups_fk = models.ForeignKey(Groups, models.DO_NOTHING, db_column='id_Groups_fk', blank=True, null=True)  # Field name made lowercase.
    id_department_fk = models.ForeignKey(Department, models.DO_NOTHING, db_column='id_department_fk', blank=True, null=True)
    bu_id = models.IntegerField(blank=False, null=False)
    def __str__(self):
        return str(self.name_Students)

    class Meta:
        managed = False
        db_table = 'students'
