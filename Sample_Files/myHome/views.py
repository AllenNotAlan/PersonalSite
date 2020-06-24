from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Project
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ContactForm
from django.conf import settings
from django.views.decorators.http import require_http_methods
from django.contrib import messages

# Create your views here.
def home_view(request):

    context = {
        'projects': Project.objects.all()
    }

    return render(request, 'myHome/home.html', context)

class ProjectListView(ListView):
    model = Project
    template_name = 'myHome/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'projects'
    ordering = ['-date_posted'] # negative sign reverses the loop

class ProjectDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Project

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.author: #if logged in user is the project user
            return True
        return False

#this may be where we need to implement multiple pages per project post!
class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields =['title', 'summary', 'description', 'thumbnail', 'language', 'link']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

#loginrequiredmixin checks if user is logged in to access create new project
#userpassestestmixin checks if correct user is logged in to update their project
class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    fields =['title','summary', 'description' , 'thumbnail', 'language', 'link']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.author: #if logged in user is the project user
            return True
        return False

class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    success_url = '/'

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.author: #if logged in user is the project user
            return True
        return False

def other_view(request):
    return render(request, 'myHome/other.html', {'title': 'Other'})

def contact_view(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            email_signage = "\n\nSent by {}".format(from_email)
            message = form.cleaned_data['message'] + email_signage
            try:
                send_mail(subject, message, from_email, [settings.EMAIL_HOST_USER])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, 'Message Sent!') # user prompt notification
            return redirect('myHome-contact')
    return render(request, 'myHome/contact.html', {'form': form})

def handler404(request, exception=None):
    return render(request, 'myHome/404.html', status=404)

def handler500(request, exception=None):
    return render(request, 'myHome/500.html', status=500)