from django.shortcuts import render,redirect
from webapp.models import department,user,Teacher,Student
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout



def dep_add(request):
    if request.method=="POST":
        d=request.POST["dep"]
        x=department.objects.create(dep_name=d)
        x.save()
        return HttpResponse('success')
    else:
        return render(request,'dep_add.html')


def index(request):
    return render(request,'index.html')


def adminhome(request):
    return render(request,'adminhome.html') 

def mainhome(request):
    return render(request,'mainhome.html')


def reg_teacher(request):
    if request.method=="POST":
        d=request.POST['dep']
        f=request.POST['fname']
        l=request.POST['lname']
        e=request.POST['email']
        u=request.POST['uname']
        p=request.POST['password']
        a=request.POST['age']
        ad=request.POST['address']
        q=request.POST['qual']
        x=user.objects.create_user(first_name=f,last_name=l,email=e,username=u,password=p,usertype="teacher")
        x.save()
        y=Teacher.objects.create(tid=x,depid_id=d,age=a,address=ad,qualification=q)
        y.save()
        return HttpResponse("success")
    else:
        x=department.objects.all()

        return render(request,'reg_teacher.html',{'x1':x})
    
def reg_student(request):
    if request.method=="POST":
        d=request.POST['dep']
        f=request.POST['fname']
        l=request.POST['lname']
        e=request.POST['email']
        u=request.POST['uname']
        p=request.POST['password']
        a=request.POST['age']
        ad=request.POST['address']
        x=user.objects.create_user(first_name=f,last_name=l,email=e,username=u,password=p,usertype="student",is_active=False)
        x.save()
        y=Student.objects.create(sid=x,depid_id=d,age=a,address=ad)
        y.save()
        return HttpResponse("student registered")
    else:
        x=department.objects.all()
        return render(request,'reg_student.html',{'x1':x})
    
def viewstudent(request):
    x=Student.objects.all()
    return render(request,'viewstudent.html',{'x1':x})

def viewteacher(request):
    x=Teacher.objects.all()
    return render(request,'viewteacher.html',{'x1':x})

def approve(request,aid):
    st=Student.objects.get(id=aid)
    st.sid.is_active=True
    st.sid.save()
    
    return redirect(viewstudent)

def teacherhome(request):
    return render(request,'teacherhome.html') 

def studenthome(request):
    return render(request,'studenthome.html') 

def logins(request):
    if request.method=="POST":
        u=request.POST['username']
        p=request.POST['password']
        user=authenticate(request,username=u,password=p)
        if user is not None and user.is_superuser==1:
            return redirect(adminhome)
        elif user is not None and user.usertype=="teacher":
            login(request,user)
            request.session['teach_id']=user.id
            return redirect(teacherhome)
        elif user is not None and user.usertype=="student" and user.is_active==1:
            login(request,user)
            request.session['stu_id']=user.id
            return redirect(studenthome)
        else:
            return HttpResponse("not valid")
    else:
        return render(request,'logins.html')

def approved_stview(request):
    x=user.objects.filter(is_active=1,usertype="student")
    return render(request,'approved_stview.html',{'x':x})

def updatest(request):
    stud=request.session.get('stu_id')
    student=Student.objects.get(sid_id=stud)
    User=user.objects.get(id=stud)
    return render(request,'updatest.html',{'view':student,'data':User})


def updatestudent(request,uid):
    if request.method=="POST":
        stud=Student.objects.get(id=uid)
        sid=stud.sid_id
        User=user.objects.get(id=sid)
        User.first_name=request.POST['fname']
        User.last_name=request.POST['lname']
        User.email=request.POST['email']
        User.username=request.POST['uname']
        User.save()
        stud.age=request.POST['age']
        stud.address=request.POST['address']
        stud.save()
        return HttpResponse('success')
    
def updateteach(request):
    teach=request.session.get('teach_id')
    teacher=Teacher.objects.get(tid_id=teach)
    User=user.objects.get(id=teach)
    return render(request,'updateteach.html',{'view':teacher,'data':User})


def updateteacher(request,uid):
    if request.method=="POST":
        teach=Teacher.objects.get(id=uid)
        tid=teach.tid_id
        User=user.objects.get(id=tid)
        User.first_name=request.POST['fname']
        User.last_name=request.POST['lname']
        User.email=request.POST['email']
        User.username=request.POST['uname']
        User.save()
        teach.age=request.POST['age']
        teach.address=request.POST['address']
        teach.save()
        return HttpResponse('success')
    

def lgout(request):
    logout(request)
    return redirect(logins)

def deletestud(request,uid):
    x=user.objects.get(id=uid)
    x.delete()
    return redirect(viewstudent)

def deleteteach(request,uid):
    x=user.objects.get(id=uid)
    x.delete()
    return redirect(viewteacher)

def depbystudent(request):
    teacher=Teacher.objects.get(tid=request.user)
    department_students=Student.objects.filter(depid=teacher.depid)
    return render(request,'department_student.html',{'x1':department_students})

def depbyteacher(request):
    student=Student.objects.get(sid=request.user)
    department_teacher=Teacher.objects.filter(depid=student.depid)
    return render(request,'department_teacher.html',{'x1':department_teacher})



