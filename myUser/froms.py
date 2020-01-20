from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser
from django.contrib.auth import authenticate

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=100, required=True , label="آدرس ایمیل" , help_text="آدرس ایمیل خود را وارد نمایید" )

    class Meta:
        model = MyUser
        fields = ('email','username','password1','password2')



class LoginForm (forms.ModelForm):
    password = forms.CharField(label="گذر واژه",widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email','password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email,password=password):
                raise forms.ValidationError('invalid login')


class UpdateForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ("email",'username')
    
    def setEmail(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                user = MyUser.objects.exclude(pk = self.instance.pk).get(email = email)
            except user.DoesNotExist:
                return email
            raise forms.ValidationError("email does not exists")
    
    def setUsername(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                user = MyUser.objects.exclude(pk = self.instance.pk).get(username = username)
            except user.DoesNotExist:
                return username
            raise forms.ValidationError("username does not exists")

