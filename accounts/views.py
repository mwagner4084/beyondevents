from django.contrib.auth import login
from django.shortcuts import redirect
from .forms import CustomUserCreationForm, UserProfileForm
from .models import UserProfile
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_form'] = UserProfileForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        profile_form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class ProfileView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserProfile
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile.html'
    fields = ['profile_pic', 'bio', 'mood_board', 'wedding_date', 'location', 'phone', 'guests', 'bridesmaids', 'groomsmen']

    def test_func(self):      
        obj = self.get_object()
        return obj.user == self.request.user    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
    
class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserProfile
    success_url = reverse_lazy('home')
    template_name = 'registration/profile.html'
    fields = ['profile_pic', 'bio', 'mood_board', 'wedding_date', 'location', 'phone', 'guests', 'bridesmaids', 'groomsmen']

    def test_func(self):      
        obj = self.get_object()
        return obj.user == self.request.user    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context