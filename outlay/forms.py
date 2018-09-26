from django import forms
from django.contrib.auth import get_user_model
from .models import Item

User = get_user_model()

#Form to add/edit items
class Item_form(forms.ModelForm):
    item_name = forms.CharField(label='Item',
            widget=forms.TextInput(attrs={"class": "form-control form-control-sm","placeholder": "Enter item name"}))
    price = forms.CharField(label='Price:',
        widget=forms.TextInput(attrs={"class": "form-control form-control-sm","placeholder": "Enter price"}))
    image = forms.FileField(label='Image:',
        widget=forms.ClearableFileInput(attrs={"class":"file-input btn-info"}))

    class Meta:
        model = Item
        fields = ('item_name','price','image')

#Form for user registration
class RegisterForm(forms.Form):
    username = forms.CharField(label='Username',
            widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Enter username"}))
    first_name = forms.CharField(label='First Name',
            widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Enter first name"}))
    last_name = forms.CharField(label='Last Name',
            widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Enter last name"}))
    password = forms.CharField(label='Password',
        widget=forms.PasswordInput(attrs={"class": "form-control","placeholder": "Enter Password",}))
    password2 = forms.CharField(label='Password',
        widget=forms.PasswordInput(attrs={"class": "form-control","placeholder": "Confirm your Password",}))
    
    #Checking if entered username is unique or not.
    def clean_username(self):
        username = self.cleaned_data.get('username')
        check_username = User.objects.filter(username=username)
        if check_username.exists():
            raise forms.ValidationError("Username taken!")
        return username
    
    #Checking if passwords match
    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password!=password2:
            raise forms.ValidationError("Passwords must match!")
        return data

#Form for user login
class LoginForm(forms.Form):
    username = forms.CharField(label='Username',
            widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Enter username"}))
    password = forms.CharField(label='Password',
        widget=forms.PasswordInput(attrs={"class": "form-control","placeholder": "Enter Password",}))
    