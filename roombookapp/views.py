from django.shortcuts import render,redirect
from django.contrib import messages
from datetime import datetime
from roombookapp.models import *
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required

def logout(request):
    auth.logout(request)
    return render(request,"roombookapp/base.html")
# Create your views here.
def login(request):
    if request.method == 'POST':
        if request.POST.get('uname'):
            chkuname = request.POST.get('uname')
            chkpw = request.POST.get('pwd')
            print(chkuname)
            print(chkpw)
            user = auth.authenticate(request,username=chkuname,password=chkpw)
            if user is not None:
                if user.is_active:
                    request.session.set_expiry(86400) #sets the exp. value of the session 
                    auth.login(request, user) #the user is now logged in
                    messages.success(request,'เข้าสู่ระบบสำเร็จ')
                    #print(request.session['user'])
                return redirect('/login')
            else:
                messages.warning(request,"ไม่ถูกต้อง ลองใหม่")
                return redirect('/login')
    return render(request,"roombookapp/login.html")

def base(request):
    context = {'bookingdata' : bookingdata.objects.all().order_by('-start_date')}
    return render(request,"roombookapp/base.html",context)

@login_required(login_url='/login')
def bookfind(request):
    if request.method == 'POST':
        if request.POST.get('date_search'):
            s_date = request.POST.get('date_search')
            context = {'bookingdata' : bookingdata.objects.filter(start_date=s_date)}
            return render(request,"roombookapp/bookfindform.html",context)
    return render(request,"roombookapp/bookfindform.html")


def manageuser(request):
    context = {'user' : userchk.objects.all()}
    return render(request,"roombookapp/base.html",context)

def bookform(request):
    context = {'roomdata' : roomdata.objects.all()}
    if request.method == 'POST':
        if request.POST.get('book_user'):
            print(request.POST.get('room_name'))
            print(request.POST.get('room_go'))
            print(request.POST.get('start_date'))
            print(request.POST.get('book_detail'))
            print(request.POST.get('book_user'))
            print(request.POST.get('book_tel'))
            start_time = request.POST.get('start_timeh') + ":" + request.POST.get('start_timem')
            end_time = request.POST.get('end_timeh') + ":" + request.POST.get('end_timem')
            start_time_object = datetime.strptime(start_time, '%H:%M').time()
            end_time_object = datetime.strptime(end_time, '%H:%M').time()
            print(start_time_object)
            print(end_time_object)
            table = bookingdata()
            table.room_name = request.POST.get('room_name')
            table.room_go = request.POST.get('room_go')
            table.start_date = request.POST.get('start_date')
            table.start_time = start_time_object
            table.end_time = end_time_object
            table.book_detail = request.POST.get('book_detail')
            table.book_user = request.POST.get('book_user')
            table.book_tel = request.POST.get('book_tel')
            result = 0
            print(range(start_time_object,end_time_object))
            tablechk = bookingdata.objects.all()
            if bookingdata.objects.filter(start_date=table.start_date).exists():
                if bookingdata.objects.filter(start_time=start_time_object).exists() or bookingdata.objects.filter(end_time=end_time_object).exists():
                    messages.warning(request,"วันที่ และ เวลาซ้ำ")
                    return redirect('/bookform',context)
            if userchk.objects.filter(user_phone=table.book_tel).exists():
                table.save()
                messages.success(request,"บันทึกข้อมูลสำเร็จ")
            else:    
                messages.warning(request,"ไม่พบหมายเลขโทรศัพท์ในระบบ")
                return redirect('/bookform',context)
    return render(request,"roombookapp/bookform.html",context)