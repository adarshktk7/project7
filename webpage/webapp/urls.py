from django.contrib import admin
from django.urls import path
from webapp import views

urlpatterns = [
    path('dep_add',views.dep_add,name='dep_add'),
    # path('',views.mainhome,name='mainhome'),#
    path('adminhome',views.adminhome,name='adminhome'),
    path('reg_teacher',views.reg_teacher,name='reg_teacher'),
    path('reg_student',views.reg_student,name='reg_student'),
    path('viewstudent',views.viewstudent,name='viewstudent'),
    path('viewteacher',views.viewteacher,name='viewteacher'),

    path('approve/<int:aid>',views.approve,name='approve'),
    path('logins',views.logins,name='logins'),
    path('teacherhome',views.teacherhome,name='teacherhome'),
    path('studenthome',views.studenthome,name='studenthome'),
    path('approved_stview',views.approved_stview,name='approved_stview'),
    path('',views.index,name='index'),
    path('updatest',views.updatest,name='updatest'),
    path('updatestudent/<int:uid>',views.updatestudent,name='updatestudent'),
    path('updateteach',views.updateteach,name='updateteach'),
    path('updateteach/<int:uid>',views.updateteach,name='updateteach'),
    path('lgout',views.lgout,name='lgout'),
    path('deletestud/<int:uid>',views.deletestud,name='deletestud'),
    path('deleteteach/<int:uid>',views.deleteteach,name='deleteteach'),
    path('depbystudent',views.depbystudent,name='depbystudent'),
    path('depbyteacher',views.depbyteacher,name='depbyteacher'),
    
     
]