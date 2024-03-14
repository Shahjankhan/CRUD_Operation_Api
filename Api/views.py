from django.shortcuts import render
from .models import student
from .serializers import Stud_serializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import io
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def student_Api(request):
    if request.method == "GET":
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id', None)
        if id is not None:
           stu= student.objects.get(id=id)
           serial=Stud_serializer(stu)
           json_data=JSONRenderer().render(serial.data)
           return HttpResponse(json_data,content_type='application/json')
        else:
           stu= student.objects.all()
           serial=Stud_serializer(stu,many=True)
           json_data=JSONRenderer().render(serial.data)
           return HttpResponse(json_data,content_type='application/json')

        
       
    if request.method == 'POST':
       json_data=request.body
       stream=io.BytesIO(json_data)
       python_data=JSONParser().parse(stream)
       serial=Stud_serializer(data=python_data)
       if serial.is_valid():
          serial.save()
          res={'msg':'Data successfully created !!'}
          json_data=JSONRenderer().render(res)
          return HttpResponse(json_data,content_type='application/json')
       else:
          json_data=JSONRenderer().render(serial.errors)
          return HttpResponse(json_data,content_type='application/json')
    

    if request.method =='PUT':
       json_data=request.body
       stream=io.BytesIO(json_data)
       python_data=JSONParser().parse(stream)
       id=python_data.get('id')
       stu = student.objects.get(id=id)
       serial= Stud_serializer(stu, data=python_data, partial=True)
       if serial.is_valid():
          serial.save()
          res={'msg':'Data successfully Updated!!'}
          json_data=JSONRenderer().render(res)
          return HttpResponse(json_data,content_type='application/json')
       else:
          json_data=JSONRenderer().render(serial.errors)
          return HttpResponse(json_data,content_type='application/json')
     
    if request.method =='DELETE':
       json_data=request.body
       stream=io.BytesIO(json_data)
       python_data=JSONParser().parse(stream)
       id=python_data.get('id')
       stu=student.objects.get(id=id)
       stu.delete()
       res={'msg':'Data successfully Deleted!!'}
       json_data=JSONRenderer().render(res)
       return HttpResponse(json_data,content_type='application/json')
          
    