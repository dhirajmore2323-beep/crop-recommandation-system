from django.shortcuts import render
from .forms import CropForm
import joblib
import numpy as np
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Login successful!")
            return redirect('predict')
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'login.html')


model = joblib.load('crop_model.pkl')



def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')

def predict_crop(request):
    prediction = None
    if request.method == 'POST':
        form = CropForm(request.POST)
        if form.is_valid():
            data = np.array([[ 
                form.cleaned_data['nitrogen'],
                form.cleaned_data['phosphorus'],
                form.cleaned_data['potassium'],
                form.cleaned_data['temperature'],
                form.cleaned_data['humidity'],
                form.cleaned_data['ph'],
                form.cleaned_data['rainfall']
            ]])

            result = model.predict(data)[0]  # returns crop name like 'rice'
            prediction = result  # Directly use result as prediction
    else:
        form = CropForm()

    return render(request, 'crop.html', {'form': form, 'prediction': prediction})
