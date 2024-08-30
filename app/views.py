from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from app.forms import *
# Create your views here.
class senddata_bytv(TemplateView):
    template_name='senddata_bytv.html'
    def get_context_data(self,**kwargs):
        ecdo=super().get_context_data(**kwargs)
        ecdo['name']='likki'
        ecdo['age']=22
        ecdo['eso']=StudentForm()
        return ecdo
    def post(self,request):
        sdo=StudentForm(request.POST)
        if sdo.is_valid():
            sdo.save()
            return HttpResponse('data is inserted')
        else:
            return HttpResponse('invalid data')
    
