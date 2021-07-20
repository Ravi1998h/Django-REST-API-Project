from django.shortcuts import render
from django.views.generic import View
import io
from rest_framework.parsers import JSONParser
from myapp.models import Employee
from rest_framework.renderers import JSONRenderer
from myapp.serializer import EmployeeSerializer
from django.http import HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
@method_decorator(csrf_exempt,name='dispatch')
class EmployeeCRUDCBV(View):
    def get(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        py_data=JSONParser().parse(stream)
        id=py_data.get('id',None)
        if id is not None:
            record=Employee.objects.get(id=id)
            esirialize=EmployeeSerializer(record)
            json_data=JSONRenderer().render(esirialize.data)
            return HttpResponse(json_data,content_type='application/json')
        qs=Employee.objects.all()
        esirialize=EmployeeSerializer(qs,many=True)
        json_data=JSONRenderer().render(esirialize.data)
        return HttpResponse(json_data,content_type='application/json')

    def post(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        py_data=JSONParser().parse(stream)
        esirialize=EmployeeSerializer(data=py_data)
        if esirialize.is_valid():
            esirialize.save()
            mes={'msg':'data is created'}
            json_data=JSONRenderer().render(mes)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(eserializer.errors)
        return HttpResponse(json_data,content_type='application/json')

    def put(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        py_data=JSONParser().parse(stream)
        id=py_data.get('id')
        record=Employee.objects.get(id=id)
        eserialize=EmployeeSerializer(record,data=py_data)
        if eserialize.is_valid():
            eserialize.save()
            msg={'msg':'data is updated'}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(eserialize.errors)

    def delete(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        py_data=JSONParser().parse(stream)
        id=py_data.get('id')
        record=Employee.objects.get(id=id)
        record.delete()
        msg={'msg':'data is deleted'}
        json_data=JSONRenderer().render(msg)
        return HttpResponse(json_data,content_type='application/json')



# Create your views here.
