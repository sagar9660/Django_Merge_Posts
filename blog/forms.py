from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Post, User, Category, Comments
from django.forms import ModelForm, TextInput, EmailInput, Textarea

# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'category', 'tag', 'featured', 'thumbnail')


class UserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("first_name", "last_name", "email", "username", "password1", "password2", "email", "city", "country", "gender",)

	def save(self, commit=True):
		user = super(UserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


# class UserForm(forms.ModelForm):
#     password = forms.CharField(max_length=63, widget=forms.PasswordInput)
#     # confirm_password = forms.CharField(widget=forms.PasswordInput)
    
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email', 'username', 'password', 'city', 'country', 'gender',)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)
    


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'email', 'comment')
        
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px; display: inline;',
                'placeholder': 'Enter Your Name'
                }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px; display: inline;',
                'placeholder': 'Enter Your Email'
                }),
            'comment': Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 300px; max-height: 65px; display: inline;',
                'placeholder': 'Comment Here'
                })
        }