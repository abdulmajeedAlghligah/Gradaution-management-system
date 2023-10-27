from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [


    path('', views.index, name='login'),

    # committees paths auth_permission

    path('loginCommittee',                   views.loginCommittee,                    name='loginCommittee'),
    path('committee_home',                   views.committee_home,                    name='committee_home'),
    path('committee_add_idea',               views.committee_add_idea,                name='committee_add_idea'),
    path('committee_show_idea',              views.committee_show_idea,               name='committee_show_idea'),
    path('show_suggested_idea',              views.show_suggested_idea,               name='show_suggested_idea'),
    path('modifying_groups',                 views.modifying_groups,                  name='modifying_groups'),
    path('show_evaluation',                  views.show_evaluation,                   name='show_evaluation'),
    path('distrbution_doctors_to_groups',    views.distrbution_doctors_to_groups,     name='modifying_groups'),
    path('Add_CRN',                          views.Add_CRN,                           name='Add_CRN'),
    path('<int:id>/CRN_update/',             views.CRN_update,                        name='CRN_update'),#Url for page update
    path('<int:id>/Doctor_update/',          views.Doctor_update,                     name='Doctor_update'),
    path('<int:id>/Student_update',          views.Student_update,                    name='Student_update'),
    path('Committee_create_group',           views.Committee_create_group,              name='Committee_create_group'),
    path('Committee_message_creating_group',  views.Committee_message_creating_group ,  name='Committee_message_creating_group'),
    path('Committee_creating_group/<int:id>',  views.Committee_creating_group ,               name='Committee_creating_group'),
    path('distrbution_update/<int:id>',      views.distrbution_update,                name='distrbution_update'),

    # doctors paths   

    path('loginDoctors',                     views.loginDoctors,                      name='loginDoctors'),
    path('doctors_home',                     views.doctors_home,                      name='doctors_home'),
    path('doctor_show_idea',                 views.doctor_show_idea,                  name='doctor_show_idea'),
    path('doctor_create_group',              views.doctor_create_group ,              name='doctor_create_group'),
    path('doctor_show_my_group',    views.doctor_show_my_group ,    name='doctor_show_my_group'),
    path('doctor_evaluating_groups',         views.doctor_evaluating_groups ,         name='doctor_evaluating_groups'),
    path('doctor_show_my_group_evaluation',  views.doctor_show_my_group_evaluation ,  name='doctor_show_my_group_evaluation'),
    path('doctor_message_creating_group',  views.doctor_message_creating_group ,  name='doctor_message_creating_group'),
    path('doctor_choose_idea/<int:id>',      views.doctor_choose_idea ,               name='doctor_choose_idea'),
    path('doctor_creating_group/<int:id>',      views.doctor_creating_group ,               name='doctor_creating_group'),
    path('doctor_upload_file/<int:id>',      views.doctor_upload_file ,               name='doctor_upload_file'),
    
    
    # students paths  

    path('loginStudents',                    views.loginStudents,                     name='loginStudents'),
    path('student_home' ,                    views.student_home,                      name='student_home'),
    path('student_show_the_department_idea', views.student_show_the_department_idea , name='student_show_the_department_idea'),
    path('student_show_archived_idea',       views.student_show_archived_idea ,       name='student_show_archived_idea'),
    path('student_upload_project',           views.student_upload_project ,           name='student_upload_project'),
    path('student_upload_proposal',           views.student_upload_proposal ,           name='student_upload_proposal'),
    path('student_choose_groups',            views.student_choose_groups ,            name='student_choose_groups'),
    path('student_show_my_group',              views.student_show_my_group ,              name='student_show_my_group'),
    path('Chose_Enter/<int:id>',             views.Chose_Enter,                       name='Chose_Enter'),
    path('choose_group/<int:id>',            views.choose_group,                      name='choose_group'),
    
    



    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  

urlpatterns += staticfiles_urlpatterns()
