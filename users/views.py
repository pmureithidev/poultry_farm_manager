from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FarmerRegistrationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = FarmerRegistrationForm(request.POST)
        if form.is_valid():
            farmer = form.save()
            login(request, farmer)
            # success message after account creation
            messages.success(request, f"Welcome to Poultry Manager, {farmer.farm_name}!")
            return redirect('home')
        else:
            # add form errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{form.fields[field].label}: {error}")

    else:
        form =FarmerRegistrationForm()
    
    return render(request, 'registration/register.html', {'form': form})

@login_required
def home(request):
    # Access the authenticated user's farm name
    return render(request, 'home.html', {
        'farm_name': request.user.farm_name
    })

