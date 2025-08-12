from django import forms

class CropForm(forms.Form):
    nitrogen = forms.FloatField(
        label='Nitrogen ',
        min_value=0.0,
        widget=forms.NumberInput(attrs={'class':'forms-control','step': '0.1'}))
    
    phosphorus = forms.FloatField(
        label='Phosphorus',
        min_value=0.0,
        widget=forms.NumberInput(attrs={'class':'forms-control','step': '0.1'}))
    
    potassium = forms.FloatField(
        label='Potassium',
        min_value=0.0,
        widget=forms.NumberInput(attrs={'class':'forms-control','step': '0.1'}))
    
    temperature = forms.FloatField(
        label='Temperature',
        min_value=0.0,
        widget=forms.NumberInput(attrs={'class':'forms-control','step': '0.1'}))
    
    humidity = forms.FloatField(
        label='Humidity',
        min_value=0.0,
        widget=forms.NumberInput(attrs={'class':'forms-control','step': '0.1'}))
    
    ph = forms.FloatField(
        label='pH',
        min_value=0.0,
        widget=forms.NumberInput(attrs={'class':'forms-control','step': '0.1'}))
    
    rainfall = forms.FloatField(
        label='Rainfall',
        min_value=0.0,
        widget=forms.NumberInput(attrs={'class':'forms-control','step': '0.1'}))
    
class CropForm(forms.Form):
    nitrogen = forms.FloatField()
    phosphorus = forms.FloatField()
    potassium = forms.FloatField()
    temperature = forms.FloatField()
    humidity = forms.FloatField()
    ph = forms.FloatField()
    rainfall = forms.FloatField()

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)