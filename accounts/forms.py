from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser, UserProfile

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email',) + ('first_name',) + ('last_name',) + ('phone',) + ('username',)

class CustomUserChangeForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email',) + ('first_name',) + ('last_name',) + ('phone',) + ('username',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_pic', 'bio', 'mood_board', 'wedding_date', 'location', 'guests', 'bridesmaids', 'groomsmen']
        widgets = {
            'wedding_date': forms.DateInput(attrs={'type': 'date'}),
            'bio': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
            'mood_board': forms.URLInput(attrs={'type': 'url'}),
            'profile_pic': forms.FileInput(attrs={'type': 'file'}),
            'location': forms.TextInput(attrs={'type': 'text'}),
            'guests': forms.NumberInput(attrs={'type': 'number'}),
            'bridesmaids': forms.NumberInput(attrs={'type': 'number'}),
            'groomsmen': forms.NumberInput(attrs={'type': 'number'}),

        }