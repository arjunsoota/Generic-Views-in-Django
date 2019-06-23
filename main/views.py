from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from main import models
from django.views.generic import(
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
    CreateView,
)
# Create your views here.

class Index(View):
    def get(self,request):
        return HttpResponse("Get Request")
    def post(self,request):
        return HttpResponse("Post Request")
    
class collegeDetail(DetailView):
    model = models.college
    template_name = "college_detail.html"

class collegeList(ListView):
    model = models.college
    template_name = "college_list.html"
    context_object_name = 'colleges'

class CollegeCreate(CreateView):
    model = models.college
    template_name = "college_create.html"
    fields = '__all__'
    success_url = '/college'
class StudentCreate(CreateView):
    model = models.student
    template_name= "student_create.html"
    fields = '__all__'
    success_url = '/college'

class CollegeUpdate(UpdateView):
    model = models.college
    template_name = "college_create.html"
    fields = '__all__'
    success_url = '/college'

class DeleteStudent(DeleteView):
    model = models.student
    template_name = "confirm.html"
    success_url = "/college"
    

