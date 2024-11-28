# accounts/forms.py
import re
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

# Get the custom user model
CustomUser = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')  # Adjust fields as needed
    
    # Custom password validation
    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        
        # Check for minimum length
        if len(password) < 8:
            raise ValidationError('Password must be at least 8 characters long.')
        
        # Check for uppercase letter
        if not re.search(r'[A-Z]', password):
            raise ValidationError('Password must contain at least one uppercase letter.')
        
        # Check for lowercase letter
        if not re.search(r'[a-z]', password):
            raise ValidationError('Password must contain at least one lowercase letter.')
        
        # Check for digit
        if not re.search(r'[0-9]', password):
            raise ValidationError('Password must contain at least one digit.')
        
        # Check for special character
        if not re.search(r'[\W_]', password):  # \W matches non-alphanumeric characters
            raise ValidationError('Password must contain at least one special character (e.g., @, #, $, etc.).')
        
        return password

    # Custom username validation (optional)
    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        # Check if the username is at least 4 characters long (optional)
        if len(username) < 4:
            raise ValidationError('Username must be at least 4 characters long.')
        
        # Example: Check if the username contains any special characters (optional)
        if not re.match(r'^[\w]+$', username):  # Only letters, numbers, and underscores
            raise ValidationError('Username can only contain letters, numbers, and underscores.')

        return username
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            CustomUser.objects.get(username=username)  # Check if user exists
        except CustomUser.DoesNotExist:
            raise forms.ValidationError("This username does not exist.")
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        # You can add extra password validation if needed
        return password