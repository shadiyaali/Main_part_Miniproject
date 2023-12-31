from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate
from .models import userdata, image_data
 
from django.db.models import Q


# Create your views here.
def login(request):
    if 'username' in request.session:
        context = {
            'imgdata':image_data.objects.all()
        }
        return render(request, 'home.html',context)

    return render(request, 'login.html')    



def home(request):
    if 'username' in request.session:
        context = {
            'imgdata':image_data.objects.all()
        }
        return render(request, 'home.html',context)

    return render(request, 'login.html') 


def signup(request):
    if 'username' in request.session:
        context = {
            'imgs':image_data.objects.all()
        }
        return render(request, 'home.html',context)

    return render(request, 'signup.html') 

def register(request):
    if request.method == 'POST':
        if userdata.objects.filter(
            email = request.POST['email']
        ).exists():
            messages.error(request, "email or username already exist...!",extra_tags='email_exist')
            return render(request, 'signup.html')
        
        elif request.POST['pass1'] != request.POST['pass2']:
            return render(request, 'signup.html')        
        
        else:
            values = userdata(
                firstname = request.POST['firstname'],
                lastname = request.POST['lastname'],
                username = request.POST['username'],
                email = request.POST['email'],
                password = request.POST['pass1']
            )
            values.save()
            return render(request, 'login.html')

    else:
        return render(request, 'signup.html')


    

def login_form(request):
    if request.method == 'POST':
        user1 = request.POST['username']
        pass1 = request.POST['password']
        user = authenticate(request, username = user1, password = pass1)

        if user is not None:
            request.session['username'] = user1
            context = {
                'users' : userdata.objects.all()
            }
            return render(request, 'admin_panel.html', context)
        else:
            if userdata.objects.filter(
                username = request.POST['username'], password = request.POST['password']
            ).exists():
                request.session['username'] = request.POST['username']
                context = {
                    'imgdata': image_data.objects.all()
                }
                return render(request,'home.html',context)

            else:
                messages.error(request, "username or password is incorrect...!",extra_tags='login_fail')
                
                return render(request, 'signin.html')
    else:
        return render(request, 'login.html')

def admin_panel(request):
    if request.user.is_authenticated:
        context={
            'users': userdata.objects.all()
        }
        return render(request,'admin_panel.html', context)

    elif 'username' in request.session:
        context={
            'users':userdata.objects.all()
        }
    if 'username' in request.session:  
        context = {
            'users':userdata.objects.all()
        }  
        return render(request,'admin_panel.html',context)
    
    return redirect(login)

def add_user(request):
    return render(request,'add_user.html')


def update_user(request,id):
    context={
        'users':userdata.objects.get(id=id)
    }
    return render(request,'update_user.html',context)



def add_user_form(request):
    if request.method == 'POST':
        if userdata.objects.filter(
            email = request.POST['email'], username = request.POST['username']
        ).exists():
            messages.error(request, "email or username already exist...!",extra_tags='email_exist')
            return render(request, 'add_user.html')
       
        elif request.POST['password'] != request.POST['pass1']:
            messages.error(request, "Password 1 and 2 must be same...!")
            return render(request, 'add_user.html')        
       
        else:
            values = userdata(
                firstname = request.POST['firstname'],
                lastname = request.POST['lastname'],
                email = request.POST['email'],
                username = request.POST['username'],
                password = request.POST['password']
            )
            values.save()
            context = {
            'users' : userdata.objects.all()
            }
            return render(request,'admin_panel.html', context)
 
    else:
        return render(request, 'add_user.html')

def add_images(request):
    if request.method == 'POST':
        pname = request.POST['pname']
        pimage = request.FILES['pimage']
        new_data = image_data(pname = pname,pimage = pimage)
        new_data.save()
        return render(request, 'addimgs.html')
    else:
        return HttpResponse("Something Wrong")




def add_imagep(request):
    return render(request,'addimgs.html')  



def update_user_form(request,id):
   
    if request.method == 'POST':
       
        ex1 = userdata.objects.filter(id=id).update(
            firstname = request.POST['firstname'],
            lastname = request.POST['lastname'],
            email = request.POST['email'],
            username = request.POST['username'],
            password = request.POST['password']
        )
        context = {
        'users' : userdata.objects.all()
        }
        return render(request, 'admin_panel.html', context)
    else:
 
        return render(request,'update_user.html')


def delete_user(request,id):
    datas = userdata.objects.get(id=id)
    datas.delete()
    context={
        'users':userdata.objects.all()
    }
    return render(request,'admin_panel.html',context)



def edit_user(request):
    return render(request,'edit_user.html')  

def logout(request):
    if 'username' in request.session:
        request.session.flush()
    return render(request, 'login.html')         

def search_user(request):
    if request.method == "POST":
        searched = request.POST['searched']
 
        multiple_query = Q(Q(username__icontains=searched) | Q(email__icontains=searched))
        users = userdata.objects.filter(multiple_query)
       
        context = {
            'users': users
        }
 
    return render(request, 'admin_panel.html', context)
