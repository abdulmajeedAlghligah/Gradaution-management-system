from django import forms
from django.forms import fields, widgets
from .models import Doctors, Evaluation, Groups, Projects, Students


class Doc(forms.ModelForm):
    class Meta:
        model= Doctors
        fields=['id_groups_fk']


        widgets ={
            'id_groups_fk':forms.Select(attrs={'class':'form-select'}),
        } 





class Distrbution(forms.ModelForm):
    class Meta:
        model= Evaluation
        fields=['id_doctor_fk', 'id_doctor_fk2', 'id_doctor_fk3']
#

        widgets ={
            'id_doctor_fk':forms.Select(attrs={'class':'form-select'}),
            'id_doctor_fk2':forms.Select(attrs={'class':'form-select'}),
            'id_doctor_fk3':forms.Select(attrs={'class':'form-select'}),
        } 
        



class CRN(forms.ModelForm):
    class Meta:
        model= Groups
        fields=['name_groups']

        widgets ={
            'name_Groups':forms.TextInput(attrs={'class':'form-control'}),
        } 




class Add_Idea(forms.ModelForm):
    class Meta:
        model =Projects
        fields=['name_projects','filled_projects','descriotion_projects','file_project','id_projects','id_Doctors_fk','status','id_department_fk']

        widgets ={
            'id_projects':forms.TextInput(attrs={'class':'form-control'}),
            'name_projects':forms.TextInput(attrs={'class':'form-control'}),
            'filled_projects':forms.TextInput(attrs={'class':'form-control'}),
            'descriotion_projects':forms.TextInput(attrs={'class':'form-control'}),
            'file_project':forms.FileInput(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-select'}),
            'id_department_fk':forms.Select(attrs={'class':'form-select'}),
            'id_Doctors_fk':forms.Select(attrs={'class':'form-select'}),
        } 





class Stu(forms.ModelForm):
    class Meta:
        model= Students
        fields=['id_groups_fk']


        widgets ={
            'id_groups_fk':forms.Select(attrs={'class':'form-select'}),
        } 



class ChoiceIdea(forms.ModelForm):
    class Meta:
        model= Students
        fields=['id_groups_fk']
        widgets ={
            'id_groups_fk':forms.Select(attrs={'class':'form-select'}),
        } 
        

class UploadIdeaForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields=['name_projects','filled_projects','descriotion_projects','file_project','id_projects','id_department_fk','status']

        widgets ={
            'id_projects':forms.TextInput(attrs={'class':'form-control'}),
            'name_projects':forms.TextInput(attrs={'class':'form-control'}),
            'filled_projects':forms.TextInput(attrs={'class':'form-control'}),
            'descriotion_projects':forms.TextInput(attrs={'class':'form-control'}),
            'file_project':forms.FileInput(attrs={'class':'form-control'}),
            'id_department_fk':forms.Select(attrs={'class':'form-select'}),
            'status':forms.Select(attrs={'class':'form-select'}),
        } 
        
################################### my plus code ###############################
class UploadIdeaForm1(forms.ModelForm):
    class Meta:
        model = Projects
        fields=['name_projects','filled_projects','descriotion_projects','file_project','id_projects','id_department_fk','status']

        widgets ={
            'id_projects':forms.TextInput(attrs={'class':'form-control'}),
            'name_projects':forms.TextInput(attrs={'class':'form-control'}),
            'filled_projects':forms.TextInput(attrs={'class':'form-control'}),
            'descriotion_projects':forms.TextInput(attrs={'class':'form-control'}),
            'file_project':forms.FileInput(attrs={'class':'form-control'}),
            'id_department_fk':forms.Select(attrs={'class':'form-select'}),
            'status':forms.Select(attrs={'class':'form-select'}),
        } 
############################################################################################



class updeateForm(forms.ModelForm):
    class Meta:
        model= Students
        fields=['id_groups_fk']


        widgets ={
            'id_groups_fk':forms.Select(attrs={'class':'form-select'}),
        } 

        
class DoctorCreatingGroup(forms.ModelForm):
    class Meta:
        model = Groups
        fields = ['name_groups']

        widgets = {
            #'id_groups':forms.TextInput(attrs={'class':'form-control'}),
            'name_groups':forms.TextInput(attrs={'class':'form-control'}),
            }
class Add_GRP(forms.ModelForm):
    class Meta:
        model = Students
        fields=['id_groups_fk']      
        
        widgets = { 'id_groups_fk':forms.Select(attrs={'class':'form-select'}),}
        


class Choose_group(forms.ModelForm):
    class Meta:
        model= Students
        fields=['id_groups_fk']
        widgets ={
            'id_groups_fk':forms.Select(attrs={'class':'form-select'}),
        } 

class InsertIdea(forms.ModelForm):
    class Meta:
        model = Projects
        fields=['name_projects','filled_projects','descriotion_projects','id_groups_fk']

        widgets ={
            'id_projects':forms.TextInput(attrs={'class':'form-control'}),
            'name_projects':forms.TextInput(attrs={'class':'form-control'}),
            'filled_projects':forms.TextInput(attrs={'class':'form-control'}),
            'descriotion_projects':forms.TextInput(attrs={'class':'form-control'}),
            'id_groups_fk':forms.Select(attrs={'class':'form-select'}),
        } 

class ChooseGroupDoctor(forms.ModelForm):

    class Meta:
        model  = Doctors
        fields = ['id_doctors','id_groups_fk']

        widgets = {
            'id_doctors':forms.Select(attrs={'class':'form-select'}),
            'id_groups_fk':forms.Select(attrs={'class':'form-select'})
            } 


class DoctorEvaluatingGroupForm (forms.ModelForm):
    class Meta:
        model =Evaluation
        fields=['id_evaluation','file_evaluation','file_evaluation_dr2','file_evaluation_dr3']

        widgets ={
            'id_evaluation':forms.Select(attrs={'class':'form-control'}),
            'file_evaluation':forms.FileInput(attrs={'class':'form-control'}),
            'file_evaluation_dr2':forms.FileInput(attrs={'class':'form-control'}),
            'file_evaluation_dr3':forms.FileInput(attrs={'class':'form-control'}),
            
        } 

class DistrbutionCreate(forms.ModelForm):
    class Meta:
        model= Evaluation
        fields=['id_groups_fk','id_doctor_fk', 'id_doctor_fk2', 'id_doctor_fk3','id_department']
#

        widgets ={
            'id_groups_fk':forms.Select(attrs={'class':'form-select'}),
            'id_doctor_fk':forms.Select(attrs={'class':'form-select'}),
            'id_doctor_fk2':forms.Select(attrs={'class':'form-select'}),
            'id_doctor_fk3':forms.Select(attrs={'class':'form-select'}),
            'id_department':forms.Select(attrs={'class':'form-select'}),
        } 
        