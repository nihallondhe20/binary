from django.shortcuts import render, redirect,get_object_or_404
from .forms import ServiceForm,UserForm
from .models import Service,User


def insert_record(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('record_list')  # Redirect to a list of support requests
    else:
        form = ServiceForm()
    
    return render(request, 'add.html', {'form': form})

def record_list(request):
    support_requests = Service.objects.all()
    return render(request, 'home.html', {'support_requests': support_requests})


def insert_user_record(request):
    if request.method == 'POST':
        complainform = UserForm(request.POST, request.FILES)
       
        if complainform.is_valid():
            
            complainform.save()
            return redirect('/list')  # Redirect to a list of support requests
    else:
        
        complainform = UserForm()
    
    return render(request, 'add.html', {'complainform': complainform})

def user_record_list(request):
    user_list = User.objects.all()
    return render(request, 'home.html', {'user_list': user_list})



def search_user(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        if user_id:
            user = get_object_or_404(User, idss=user_id)
            return redirect('user_profile', user_id=user.idss)
    
    return render(request, 'search.html')

def user_profile(request, user_id):
    user = get_object_or_404(User, idss=user_id)
    return render(request, 'profile.html', {'user': user})


def user_edit(request, pk):
    instance = get_object_or_404(User, pk=pk)
    
    if request.method == 'POST':
        form = UserForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to a success page after editing
    else:
        form = UserForm(instance=instance)
    
    return render(request, 'customer_service.html', {'form': form})