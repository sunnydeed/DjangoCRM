from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignupForm(UserCreationForm):
    email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))
    first_name = forms.CharField(max_length=100,label = "",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(max_length=100,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    
    class Meta:
        model = User
        fields = ['email','username','first_name','last_name','password1','password2']
        
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ''
        self.fields['username'].help_text = ''
        
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class = "form-text text-muted small"><li>Minimum 8 characters</li><li>At least one uppercase letter</li><li>At least one lowercase letter</li><li>At least one number</li><li>At least one special character</li></ul>'
        
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<ul class = "form-text text-muted small"><li>Enter the same password as before, for verification</li></ul>'



class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100,required=True,label = "",widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(max_length=100,label="",required=True,widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    email = forms.EmailField(label="",required=True,widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))
    phone = forms.CharField(max_length=15,label="",required=True,widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'phone'}))
    address = forms.CharField(max_length=100,label="",required=True,widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'Address'}))
    street = forms.CharField(max_length=100,label="",required=True,widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'Street'}))
    city = forms.CharField(max_length=100,label="",required=True,widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'City'}))
    state = forms.CharField(max_length=100,label="",required=True,widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'State'}))
    postcode = forms.CharField(max_length=10,label="",required=True,widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'Postcode'}))
    company = forms.CharField(max_length=100,label="",required=True,widget=forms.widgets.TextInput(attrs={'class':'form-control','placeholder':'Company'}))
    
    class Meta:
        model = Record
        exclude = ('User',)