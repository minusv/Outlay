from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, Item_form
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from .models import Item
User = get_user_model()


@login_required(login_url='/login')
def home(request):
    items=Item.objects.filter(user=request.user.id)
    context={}
    context["items"]=items
    return render(request,'outlay/home.html',context)

@login_required(login_url='/login')
def add_item(request):
    form=Item_form(request.POST,request.FILES)
    context={'form':form,}
    if request.method=='POST':
        if form.is_valid():
            item_name=form.cleaned_data.get("item_name")
            price=form.cleaned_data.get("price")
            image=form.cleaned_data.get("image")
            item=Item(user=request.user,item_name=item_name,price=price,image=image)
            item.save()
            return redirect('/')
    else:
        context['form'] = Item_form()
    return render(request,'outlay/add_item.html',context)

@login_required(login_url='/login')
def edit_item(request,pk):
    itemobj = Item.objects.get(pk=pk)
    if request.method=='POST':
        form=Item_form(instance=itemobj,data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=Item_form(instance=itemobj)
    context={'form':form,}
    return render(request,'outlay/edit_item.html',context)

@login_required(login_url='/login')
def delete_item(request,pk):
    Item.objects.filter(id=pk).delete()
    return redirect('/')

def register_user(request):
    form=RegisterForm(request.POST or None)
    context={
        'form':form,
    }
    if form.is_valid():
        username=form.cleaned_data.get("username")
        first_name=form.cleaned_data.get("first_name")
        last_name=form.cleaned_data.get("last_name")
        password=form.cleaned_data.get("password")
        new_user=User.objects.create_user(username=username,email=None,password=password)
        new_user.first_name=first_name
        new_user.last_name=last_name
        new_user.save()
        return redirect("/login")
    return render(request,'outlay/register.html',context)

def login_user(request):
    form=LoginForm(request.POST or None)
    context={
        'form':form,
    }
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            context['form']=LoginForm()
            context['error']="Invalid credentials."
    return render(request,'outlay/login.html',context)