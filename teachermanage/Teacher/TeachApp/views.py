from django.shortcuts import render, redirect
from TeachApp.models import *
from TeachApp.forms import code, Register, login, fpass, photo
from TeachApp.models import master


# Create your views here.
# def login(request):
# return render(request,'TeachApp/login.html')

def code1(request):
    form = code
    alwin = Cobra.objects.all()
    minor = master.objects.all()
    if request.method == "POST":  # form=code(request.POST or None)
        form = code(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin')
    return render(request, 'TeachApp/admin.html', {'form': form,'alwin':alwin,'minor':minor})


def retrieve(request):
    victor = signup.objects.all()
    return render(request, 'TeachApp/admin.html', {"victor": victor})


def register(request):
    alwin = Register  # for store the data
    if request.method == "POST":
        form = Register(request.POST)
        value = form['Code'].value()  # get data from the form
        pass1 = form['Password'].value()
        # print(pass1)
        pass2 = form['Confirm_Password'].value()
        # print(pass2)
        decide = Cobra.objects.all()  # get all data from database
        for i in decide:
            print(i.code)
            if i.code == value:
                if pass1 == pass2:
                    if form.is_valid():
                        form.save()
                        return redirect('/')

        else:
            print("Error")
    return render(request, 'TeachApp/Register.html', {'alwin': alwin})


def signin(request):
    victor = signup.objects.all()
    fin = login
    # print(fin)
    if request.method == "POST":
        form = login(request.POST)
        value1 = form['username'].value()
        # print(value1)
        value2 = form['password'].value()
        # print(value2)
        for i in victor:
            if i.UserName == value1 and i.Password == value2:
                
                    id = value1
                    return redirect('upload',id)
                

    return render(request, 'TeachApp/login.html', {'fin': fin})


def matter(request,id):
    mama = master.objects.get(uname=id)
    return render(request, 'TeachApp/main2.html',{'mama':mama})


def forget(request):
    hoo = fpass

    if request.method == "POST":

        bumi = fpass(request.POST)
        name1 = request.POST['user']  # get data from html tag
        vendor = signup.objects.get(UserName=name1)  # get specified data from database
        print(name1)
        codition1 = bumi['Code'].value()
        codition2 = vendor.Code
        if codition1==codition2:
            pass1 = bumi['New_password'].value()
            pass2 = bumi['Confirm_password'].value()
            if pass1 == pass2:
                name2 = vendor.UserName
                print(name2)
                if name2 == name1:
                    vendor.Password = pass1
                    vendor.Confirm_Password = pass1
                    vendor.save()
                    return redirect('/')
    return render(request, 'TeachApp/pass.html', {"hoo": hoo})


def upload(request,id):
    hlo =master()
    bunny = signup.objects.get(UserName=id)
    if request.method == "POST":
        hlo = master()
        hlo.uname = bunny.UserName
        hlo.code = bunny.Code
        hlo.name = request.POST.get("name")
        hlo.dob = request.POST.get("dob")
        hlo.qualification = request.POST.get("qualification")
        hlo.phone = request.POST.get("phno")
        hlo.email = request.POST.get("mail")
        hlo.address = request.POST.get("address")
        hlo.UG = request.POST.get("ug")
        hlo.PG = request.POST.get("pg")
        hlo.Mphil = request.POST.get("phil")
        hlo.Phd = request.POST.get("phd")
        hlo.ex = request.POST.get("ex")
        hlo.research_paper = request.POST.get("paper")
        hlo.net = request.POST.get("net")
        hlo.set = request.POST.get("set")
        hlo.jrf = request.POST.get("jrfapp")
        hlo.jrfdate = request.POST.get("jrfdate")
        hlo.award = request.POST.get("award")

        if len(request.FILES)!=0:
            hlo.photo = request.FILES["photo"]
            hlo.ugfile = request.FILES["ugfile"]
            hlo.pgfile = request.FILES["pgfile"]
            hlo.mphilgfile = request.FILES["mphilfile"]
            hlo.phdfile = request.FILES["phdfile"]
            hlo.exfile = request.FILES["exfile"]
            hlo.netfile = request.FILES["netup"]
            hlo.setfile = request.FILES["setup"]
            hlo.jrffile = request.FILES["jrf"]
            hlo.awardfile = request.FILES["amdup"]
            hlo.save()
            id = hlo.uname
            return redirect('master',id)
    return render(request, 'TeachApp/main.html',{'bunny':bunny})

def cal(request):
    alwin = Cobra.objects.all()
    minor = master.objects.all()
    safe = score.objects.all()

    
    api_score=0

    if request.method == "POST":
        name1=request.POST.get('name')
        safe2 = score()
        safe2.name = name1
        safe2.api = 0
        safe2.save()
        cus = master.objects.get(name=name1)
        safe1 = score.objects.get(name=name1)
        
        m1=cus.UG
        m2=cus.PG
        api_score = 0
        print(m1)
        a1 = request.POST.get("gen") # get data from radiobutton 
        print(name1)
        print(a1)
        if a1 == 'verified':
            if m1>=80:
                api_score+=21
            elif m1>=60:
                api_score+=19
            elif m1>=55:
                api_score+=16

        a2 = request.POST.get("pg")
        
        if a2 =='verified':
            if m2>=80:
                api_score+=33
            elif m2>=60:
                api_score+=30
            elif m2>=55:
                api_score+=25
        print(api_score)
        a3 = request.POST.get('phil')
        a4 = request.POST.get('phd')
        m3 = cus.Mphil
        if a4 =='verified':
            api_score+=20

        elif a3 == 'verified':
            if m3>=60:
                api_score+=7
            elif m3>=55:
                api_score+=5

        a7 = request.POST.get('ex')    
        m7 = int(cus.ex)
        if a7=='verified':
            xtra_score =m7 *2
            if xtra_score >= 10:
                api_score+=10
            else:
                api_score+=xtra_score

        a6= request.POST.get('jrf')
        a5= request.POST.get('net')
        if a6=='verified':
            api_score+=10
        elif a5 =='verified':
            api_score+=8

        res1 = request.POST.get('paper1')
        res2 = request.POST.get('paper2')
        res3 = request.POST.get('paper3')
        if res1 =='verified':
            api_score+=2
        if res2=='verified':
            api_score+=2
        if res3 == 'verified':
            api_score+=2

        print(api_score)
        safe1.api = api_score
        safe1.save()
        return render(request,'TeachApp/admin.html',{'alwin':alwin,'minor':minor,'safe':safe})
    
    return render(request,'TeachApp/admin.html',{'alwin':alwin,'minor':minor,'safe':safe})

        
def board(request):
    bun = score.objects.all()
    mon = master.objects.all()
    a=[]

    # for i in bun:
        #   mon = master.objects.get(name=i.name)
        #  print(mon)

    for i in bun:
        a.append(i.api)
    a.sort(reverse=True)
    print(a)
    f=[]
    for i in a:
        sen = score.objects.get(api = i)
        f.append(sen)
        print(f)


    return render(request,'TeachApp/leaderboard.html',{'f':f,'mon':mon})
        
        
def gen(request):
    form = code
    alwin = Cobra.objects.all()
    minor = master.objects.all()
    if request.method == "POST":  # form=code(request.POST or None)
        form = code(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin/generatecode')
    return render(request,'TeachApp/Code.html',{'form':form,'alwin':alwin})

            

