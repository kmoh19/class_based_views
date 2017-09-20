from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import School,Student
from django.core.urlresolvers import reverse_lazy
#from django.http import HttpResponse


# Create your views here.

# class CBView(View):
#     def get(self,request):
#         return HttpResponse('CLASS BASED VIEWS ARE COOL')
#         


class IndexView(TemplateView):
    template_name='basic_app/index.html'
    
    def get_context_data(self, **kwargs): #first override get_context_data function
        
        context= super().get_context_data(**kwargs) #then create an object of the original prototype function for population...but why...it is the difficult way...there are much easier ways
        context['inject_me']= 'BASIC INJECTION'
        
        return context
    
    
class SchoolListView(ListView):
    context_object_name='schools' # overriding default name which would have been schoo_list
    model=School
    
    
class SchoolDetailView(DetailView):
    context_object_name='school_detail' #overriding default name which would be school
    model = School
    template_name= 'basic_app/school_detail.html'
    
    
    
    
class SchoolCreateView(CreateView):
    model = School # or model.school
    fields=['name','principal']
    
    
class SchoolUpdateView(UpdateView):
    
    fields=['name','principal']
    model=School
                                                      
class SchoolDeleteView(DeleteView):
    model= School
    success_url = reverse_lazy('basic_app:list')
    
    
    
    