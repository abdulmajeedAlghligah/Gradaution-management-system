from asyncio import Condition
import os
import re
from django.http.response import HttpResponse
from typing import ContextManager
from django.shortcuts import render 
from django.db.models import Q
from django.conf import settings
from django.templatetags.static import static
from .models import Department, Evaluation, Projects, Students
from .forms import Add_Idea, CRN, ChoiceIdea, Doc, Stu, Distrbution ,UploadIdeaForm,UploadIdeaForm1,  Add_GRP, ChoiceIdea , Choose_group, InsertIdea, ChooseGroupDoctor, DoctorCreatingGroup, DoctorEvaluatingGroupForm , DistrbutionCreate
from django import forms
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
from .models import Doctors,CommitteesCharis,Students,Groups 
from django.shortcuts import redirect
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session

#####################################################################################
#################################### Login Pages  auth_permission uploud####################################
#####################################################################################


## messages for login page
message_welcome = 'Welcome Mr.'
message_error_sorry = "Sorry Mr."
message_error_reason = " the username or password are invalid - please try again"

def index(request):
   return render(request,'themes/login.html')


def loginCommittee(request):
    if request.method=="POST":
        try:
            check_committee = CommitteesCharis.objects.get(
                bu_id = request.POST.get('bu_id'), 
                passwords = request.POST.get('password')
                )
            messages.success(request, message_welcome + request.POST.get('bu_id'))

            ## get session of the doctor name
            committee_name = CommitteesCharis.objects.filter(bu_id = request.POST.get('bu_id')).values('name_committees_charis')
            toStr = str(committee_name)
            format1 = re.findall('[a-zA-Z]+', toStr)
            request.session['committee_name'] = format1[4]
            print(format1[4])
            # end the session of the doctor name 

            # get doctor id in the system
            committee_id_system = CommitteesCharis.objects.filter(bu_id = request.POST.get('bu_id')).values('id_committees_charis')
            tostring = str(committee_id_system)
            format1 = re.findall('[0-9]+', tostring)
            returnToIntId = int(format1[0])
            print(returnToIntId)
            request.session['committee_id'] = returnToIntId
            global committee_id
            def committee_id():
                return returnToIntId
            # end the doctor id in the system

            # get the doctor bu id 
            committee_BU_ID = request.POST.get('bu_id')
            print(committee_BU_ID)
            request.session['committee_id_bu'] = committee_BU_ID
            global doctor_bu_id
            def doctor_bu_id():
                return committee_BU_ID
            # end the doctor bu id 

            # get the department classifications 
            committeeDepartmentID = CommitteesCharis.objects.filter(bu_id = committee_BU_ID).values('id_department_fk')
            formating_to_string = str(committeeDepartmentID)
            regular_get_number = re.findall('[0-9]+', formating_to_string)
            return_to_int = int(regular_get_number[0])
            get_name_department = Department.objects.filter(id_department = return_to_int).values('name_department')
            formating_to_string2 = str(get_name_department)
            regular_get_str = re.findall('[a-zA-Z]+', formating_to_string2)
            request.session['committee_dep_id'] = return_to_int
            print(return_to_int)
            request.session['committee_dep_name'] = regular_get_str[3]
            print(regular_get_str[3])
            global committee_department_id
            def committee_department_id():
                return return_to_int
            # end the department classifications 

            return render(request, 'themes/pages_Committee/home.html')
        except CommitteesCharis.DoesNotExist as committeeNull:
            messages.error(request, message_error_sorry + request.POST.get('bu_id') + message_error_reason)
            print(str(committeeNull) + ' id => ' + str(request.POST.get('bu_id') + ' pass => ' + str(request.POST.get('password'))))
    return render(request, "themes/pages_login/loginCommittee.html")


def loginDoctors(request):
    if request.method=="POST":
        try:
            check_doctor = Doctors.objects.get(
                id_bu = request.POST.get('id'), 
                passwords = request.POST.get('password')
                )
            messages.success(request, message_welcome + request.POST.get('id'))

            ## get session of the doctor name
            doctorName = Doctors.objects.filter(id_bu = request.POST.get('id')).values('name_doctors')
            toStr = str(doctorName)
            format1 = re.findall('[a-zA-Z]+', toStr)
            request.session['doctor_name'] = format1[3]
            # end the session of the doctor name 

            # get doctor id in the system
            doctorIdSystem = Doctors.objects.filter(id_bu = request.POST.get('id')).values('id_doctors')
            tostring = str(doctorIdSystem)
            format1 = re.findall('[0-9]+', tostring)
            returnToIntId = int(format1[0])
            request.session['doctor_id'] = returnToIntId
            global doctorID
            def doctorID():
                return returnToIntId
            # end the doctor id in the system

            #get the doctor group id 
            doctorBU_ID = request.POST.get('id')
            doctorGroupID = Doctors.objects.filter(id_bu = doctorBU_ID).values('id_groups_fk')
            tostr = str(doctorGroupID)
            format1 = re.findall('[0-9]+', tostr)
            format2 = format1[0]
            format3 = int(format2)
            request.session['doctor_group_id'] = format3
            global doctor_group_id
            def doctor_group_id():
                return format3
            # end the doctor group id 

            # get the doctor bu id 
            request.session['doctor_id_bu'] = doctorBU_ID
            global doctor_bu_id
            def doctor_bu_id():
                return doctorBU_ID
            # end the doctor bu id 

            # get the department classifications 
            doctorDepartmentID = Doctors.objects.filter(id_bu = doctorBU_ID).values('id_department_fk')
            formating_to_string = str(doctorDepartmentID)
            regular_get_number = re.findall('[0-9]+', formating_to_string)
            return_to_int = int(regular_get_number[0])
            get_name_department = Department.objects.filter(id_department = return_to_int).values('name_department')
            formating_to_string2 = str(get_name_department)
            regular_get_str = re.findall('[a-zA-Z]+', formating_to_string2)
            print(regular_get_str)
            request.session['doctor_dep_id'] = return_to_int
            request.session['doctor_dep_name'] = regular_get_str[3]
            global doctor_department_id
            def doctor_department_id():
                return return_to_int
            # end the department classifications 

            return render(request, 'themes/pages_Doctors/home.html')
        except Doctors.DoesNotExist as doctorNull:
            messages.error(request, message_error_sorry + request.POST.get('id') + message_error_reason)
            print(str(doctorNull) + ' id => ' + str(request.POST.get('id') + ' pass => ' + str(request.POST.get('password'))))
    return render(request, "themes/pages_login/loginDoctors.html")


def loginStudents(request):
    if request.method=="POST":
        try:
            check_student = Students.objects.get(
                bu_id = request.POST.get('bu_id'), 
                passwords = request.POST.get('password')
                )
            messages.success(request, message_welcome + request.POST.get('bu_id'))

            ## get session of the student name
            student_name = Students.objects.filter(bu_id = request.POST.get('bu_id')).values('name_Students')
            toStr = str(student_name)
            format1 = re.findall('[a-zA-Z]+', toStr)
            request.session['student_name'] = format1[3]
            print(format1[3])
            # end the session of the student name 

            # get student id in the system
            studentIdSystem = Students.objects.filter(bu_id = request.POST.get('bu_id')).values('id_students')
            tostring = str(studentIdSystem)
            format1 = re.findall('[0-9]+', tostring)
            returnToIntId = int(format1[0])
            request.session['student_id'] = returnToIntId
            print(returnToIntId)
            global student_id
            def student_id():
                return returnToIntId
            # end the student id in the system
            
            #get the student group id 
            studentBU_ID = request.POST.get('bu_id')
            studentGroupID = Students.objects.filter(bu_id = studentBU_ID).values('id_groups_fk')
            tostr = str(studentGroupID)
            format1 = re.findall('[0-9]+', tostr)
            format2 = format1[0]
            format3 = int(format2)
            request.session['student_group_id'] = format3
            print(format3)
            global student_group_id
            def student_group_id():
                return format3
            # end the student group id 

            # get the student bu id 
            request.session['student_id_bu'] = studentBU_ID
            global student_bu_id
            def student_bu_id():
                return studentBU_ID
            # end the student bu id 

            # get the department classifications 
            studentDepartmentID = Students.objects.filter(bu_id = studentBU_ID).values('id_department_fk')
            formating_to_string = str(studentDepartmentID)
            regular_get_number = re.findall('[0-9]+', formating_to_string)
            return_to_int = int(regular_get_number[0])
            get_name_department = Department.objects.filter(id_department = return_to_int).values('name_department')
            formating_to_string2 = str(get_name_department)
            regular_get_str = re.findall('[a-zA-Z]+', formating_to_string2)
            request.session['student_dep_name'] = regular_get_str[3]
            request.session['student_dep_id'] = return_to_int
            global student_department_id
            def student_department_id():
                return return_to_int
            # end the department classifications 

            request.session['name'] = request.POST.get('bu_id')
            return render(request, 'themes/pages_Students/student_home.html')
        except Students.DoesNotExist as studentNull:
            messages.error(request, message_error_sorry + request.POST.get('bu_id') + message_error_reason)
            print(str(studentNull) + ' id => ' + str(request.POST.get('bu_id') + ' pass => ' + str(request.POST.get('password'))))
    return render(request, "themes/pages_login/loginStudents.html")

################################################################################################
#################################### committee chairs views ####################################
################################################################################################

def committee_home(request):
    return render(request, 'themes/pages_Committee/home.html')

def committee_add_idea(request):
    
    if request.method =='POST':
        Idea = Add_Idea(request.POST, request.FILES)
        if Idea.is_valid():
            Idea.save()
            return redirect('show_suggested_idea')

    context={
        'from':Add_Idea(),
        
    }
    return render(request, 'themes/pages_Committee/add_idea.html',context)

def show_suggested_idea(request):
    context={
            'project':Projects.objects.all().filter(id_department_fk = committee_department_id(), status = 'avilable'),
    }
    return render(request, 'themes/pages_Committee/show_suggested_idea.html',context)

def committee_show_idea(request):    
    context={
            'project':Projects.objects.all().filter(id_department_fk = committee_department_id(), status = 'anvilable'),       
    }
    return render(request, 'themes/pages_Committee/show_idea.html',context)

def modifying_groups(request):
    if request.method =='POST':
        stu = Stu(request.POST)
        doc = Doc(request.POST)
        if stu.is_valid() and doc.is_valid():
            stu.save()
            doc.save()

    context = {
        'std_forms':Stu(),
        'student':Students.objects.all().filter(id_department_fk = committee_department_id()),
        'group_forms':Doc(),
        'doctors':Doctors.objects.all().filter(id_department_fk = committee_department_id()),
    }
    return render(request,'themes/pages_Committee/modifying_groups.html', context)

def Student_update(request,id):
    id_Stu = Students.objects.get(id_students=id)
    if request.method =='POST':
        stu_save = Stu(request.POST,instance= id_Stu)
        if stu_save.is_valid():
            stu_save.save()
            return redirect('/modifying_groups')
    else:
        stu_save = Stu(instance=id_Stu)    
    context={
        'std_forms':stu_save
    }
    return render(request,'themes/pages_Committee/Student_update.html', context)

def Doctor_update(request,id):
    id_GRO = Doctors.objects.get(id_doctors=id)
    if request.method =='POST':
        do_save = Doc(request.POST,instance= id_GRO)
        if do_save.is_valid():
            do_save.save()
            return redirect('/modifying_groups')

    else:
        do_save = Doc(instance=id_GRO)
        
    context={
        'group_forms':do_save

    }
    return render(request,'themes/pages_Committee/Doctor_update.html', context)

def Add_CRN(request):
    if request.method =='POST':
        cr = CRN(request.POST)
        if cr.is_valid():
            cr.save()

    context={
        'froms':CRN(),
        'groub':Groups.objects.all(),
    }
    return render(request, 'themes/pages_Committee/Add_CRN.html',context)

#CRNهنا سويت فنكشن عشان اقدر اسوي تعديل ل 
def CRN_update(request,id):
    groub_id = Groups.objects.get(id_groups=id)
    if request.method =='POST':
        group_save = CRN(request.POST,instance=groub_id)
        if group_save.is_valid():
            print('this is not found')
            group_save.save()
            return redirect('/Add_CRN')

    else:
        group_save = CRN(instance=groub_id)
        
    context={
        'form':group_save

    }
    return render(request,'themes/pages_Committee/CRN_update.html', context)

def show_evaluation(request):
    evaluate = {'evaluation' : Evaluation.objects.all().filter(id_department = committee_department_id())}
    return render(request, 'themes/pages_Committee/show_evaluation.html', evaluate)

def distrbution_doctors_to_groups(request):
    if request.method =='POST':
        Idea = DistrbutionCreate(request.POST, request.FILES)
        if Idea.is_valid():
            Idea.save()
            

    distrbution_doctors = {
        'create' : DistrbutionCreate(),
        'evaluator' : Evaluation.objects.filter( Q(id_doctor_fk = None) | Q(id_doctor_fk2 = None) | Q(id_doctor_fk3 = None) ).exclude(id_groups_fk = None).filter(id_department = committee_department_id()),
        }
    return render(request, 'themes/pages_Committee/distrbution_doctors_to_groups.html', distrbution_doctors)

redirect_distrbution_page = '/distrbution_doctors_to_groups'
path_distrbution_update = 'themes/pages_Committee/distrbution_update.html'

def distrbution_update(request,id):
    evaluators = Evaluation.objects.get(id_evaluation = id)
    if request.method == "POST":
        evaluator_save = Distrbution(request.POST, instance = evaluators)
        if evaluator_save.is_valid():
            evaluator_save.save()
            return redirect(redirect_distrbution_page) 
    else:
        evaluator_save = Distrbution(instance = evaluators)

    context={
        'evaluator_from':evaluator_save,
    }
    return render(request, 'themes/pages_Committee/distrbution_update.html', context)

#######################################################################################
#################################### create group C ####################################
#######################################################################################

def Committee_create_group(request):
    if request.method =='POST':
        global upload 
        upload = Groups.objects.create(name_groups = request.POST.get('create'))
        upload.save()
        return redirect('/Committee_message_creating_group')
    global groupsID
    def groupsID():
        return upload
        

    context = {
        'students':Students.objects.all().filter(id_groups_fk = None, id_department_fk = doctor_department_id()),
        'create': DoctorCreatingGroup(),
        'hi':Add_GRP(),
    }
    return render(request, 'themes/pages_Committee/Committee_create_group.html', context)

def Committee_message_creating_group(request):
    msg = {'msg':"Success You have been added group ID " + str(groupsID())}
    return render(request, 'themes/pages_Committee/Committee_message_creating_group.html', msg)

def Committee_creating_group(request, id):
    Group = Students.objects.get(id_students=id)
    if request.method =='POST':
        Choose_save = Add_GRP(request.POST,instance=Group)
        if Choose_save.is_valid():
            Choose_save.save()
            return redirect('/Committee_create_group')
    else:
        Choose_save = Add_GRP(instance=Group)
    context={
        'from':Choose_save
    }
    return render(request,'themes/pages_Committee/Committee_creating_group.html', context)


#######################################################################################
#################################### doctors views ####################################
#######################################################################################

def doctors_home(request):
    return render(request, 'themes/pages_Doctors/home.html')


def doctor_show_idea(request):

    context = {
    
        'show':Groups.objects.all(),
        'projects':Projects.objects.all().exclude(id_groups_fk = None).filter(id_department_fk = doctor_department_id(), status = 'avilable'),
        'doctors':Doctors.objects.filter(id_bu = doctor_bu_id()),
        'doctorForm':ChooseGroupDoctor()
    }
    return render(request, 'themes/pages_Doctors/doctor_show_idea.html', context)

def doctor_choose_idea(request,id):
    chooseID = Doctors.objects.get(id_doctors=id)
    if request.method =='POST':
        Choose_save = ChooseGroupDoctor(request.POST,instance=chooseID)
        if Choose_save.is_valid():
            Choose_save.save()
            return redirect('/doctor_show_idea')
    else:
        Choose_save = ChooseGroupDoctor(instance=chooseID)

    context={'from':Choose_save}
    return render(request, 'themes/pages_Doctors/doctor_choose_idea.html', context)

def doctor_create_group(request):
    if request.method =='POST':
        global upload 
        upload = Groups.objects.create(name_groups = request.POST.get('create'))
        upload.save()
        return redirect('/doctor_message_creating_group')
    global groupsID
    def groupsID():
        return upload
        

    context = {
        'students':Students.objects.all().filter(id_groups_fk = None, id_department_fk = doctor_department_id()),
        'create': DoctorCreatingGroup(),
        'hi':Add_GRP(),
    }
    return render(request, 'themes/pages_Doctors/doctor_create_group.html', context)

def doctor_message_creating_group(request):
    msg = {'msg':"Success You have been added group ID " + str(groupsID())}
    return render(request, 'themes/pages_Doctors/doctor_message_creating_group.html', msg)

def doctor_creating_group(request, id):
    Group = Students.objects.get(id_students=id)
    if request.method =='POST':
        Choose_save = Add_GRP(request.POST,instance=Group)
        if Choose_save.is_valid():
            Choose_save.save()
            return redirect('/doctor_create_group')
    else:
        Choose_save = Add_GRP(instance=Group)
    context={
        'from':Choose_save
    }
    return render(request,'themes/pages_Doctors/doctor_creating_group.html', context)


def doctor_show_my_group(request):
    student = Students.objects.all().filter(id_groups_fk = doctor_group_id()).values('name_Students')
    for n in student:
        x = n
    tostr = str(student)
    format1 = re.findall('[a-zA-Z]+', tostr)
    context = {
        'groupid':Groups.objects.all().filter(id_groups = doctor_group_id()),
        'hisStudents':Students.objects.all().filter(id_groups_fk = doctor_group_id()),
        'mygroup':doctor_group_id()
    }
    return render(request, 'themes/pages_Doctors/doctor_show_my_group.html',context)

def doctor_evaluating_groups(request):

    context ={
        'evaluations': Evaluation.objects.filter(Q(id_doctor_fk = doctorID()) | Q(id_doctor_fk2 = doctorID() ) | Q(id_doctor_fk3 = doctorID())),
    }
    return render(request, 'themes/pages_Doctors/doctor_evaluating_groups.html' ,context)


def doctor_upload_file(request,id):
    Eval = Evaluation.objects.get(id_evaluation=id)
    if request.method =='POST':
        Chose_save = DoctorEvaluatingGroupForm(request.POST,instance=Eval)
        if Chose_save.is_valid():
            Chose_save.save()
            return redirect('/doctor_evaluating_groups')
    else:
        Chose_save = DoctorEvaluatingGroupForm(instance=Eval)
    context={
        'from':Chose_save
    }
    return render(request,'themes/pages_Doctors/doctor_upload_file.html', context)


def doctor_show_my_group_evaluation(request):
    context = {
        'doctor_evaluating':Evaluation.objects.filter(id_groups_fk = doctor_group_id()),
    }
    return render(request, 'themes/pages_Doctors/doctor_show_my_group_evaluation.html',context)

########################################################################################
#################################### students views ####################################
########################################################################################

def student_home(request):
    return render(request, 'themes/pages_Students/student_home.html')

def student_show_the_department_idea(request):
    if request.method =='POST':
        ge = ChoiceIdea(request.POST)
        if ge.is_valid():
            ge.save()
    context={
        'froms':ChoiceIdea(),
        'project':Projects.objects.exclude(id_groups_fk = None).exclude(id_Doctors_fk = None).filter(id_department_fk = student_department_id(), status = 'avilable'),
        'choiceidea':Students.objects.filter(id_students = student_id()),   
    }
    return render(request, 'themes/pages_Students/student_show_the_department_idea.html',context)

def Chose_Enter(request,id):
    Group = Students.objects.get(id_students=id)
    if request.method =='POST':
        Chose_save = ChoiceIdea(request.POST,instance=Group)
        if Chose_save.is_valid():
            Chose_save.save()
            return redirect('/student_show_the_department_idea')
    else:
        Chose_save = ChoiceIdea(instance=Group)
    context={
        'from':Chose_save
    }
    return render(request,'themes/pages_Students/Chose_Enter.html', context)

def student_show_archived_idea(request):
    context = {
        'archiveed': Projects.objects.all().filter(status = 'anvilable').exclude(name_projects = None).exclude(filled_projects = None).exclude(descriotion_projects = None).exclude(id_Doctors_fk = None).exclude(id_groups_fk = None),
    }
    return render(request, 'themes/pages_Students/student_show_archived_idea.html' ,context)

def student_upload_project(request):
    if request.method =='POST':
        upload = UploadIdeaForm(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('student_show_archived_idea')

    context ={
        'Upload_form': UploadIdeaForm(),
    }
    return render(request, 'themes/pages_Students/student_upload_project.html' ,context)

########################################################################################
#################################### student_upload_proposal  ####################################
########################################################################################
def student_upload_proposal(request):
    if request.method =='POST':
        upload = UploadIdeaForm1(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('student_show_archived_idea')

    context ={
        'Upload_form': UploadIdeaForm(),
    }
    return render(request, 'themes/pages_Students/student_upload_proposal.html' ,context)

############################################################################

def student_choose_groups(request):
    if request.method =='POST':
        upload = InsertIdea(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('message_create_group')
    context ={
        'students': Students.objects.filter(id_students = student_id()),
        'from': InsertIdea(),
        'projects': Projects.objects.all()
    }
    return render(request, 'themes/pages_Students/student_choose_groups.html' ,context)

def choose_group(request,id):
    choose_group = Students.objects.get(id_students=id)
    if request.method =='POST':
        save_group = Choose_group(request.POST,instance=choose_group)
        if save_group.is_valid():
            save_group.save()
            return redirect('/student_choose_groups')
    else:
        save_group = Choose_group(instance=choose_group)
    context={
        'from':save_group
    }
    return render(request,'themes/pages_Students/choose_group.html', context)

def student_show_my_group(request):
    context = {
        'grops': Students.objects.all().filter(id_groups_fk = student_group_id()),
    }
    return render(request, 'themes/pages_Students/student_show_my_group.html' ,context)

