import json
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student

@csrf_exempt
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        data = {'students': list(students.values())}
        return JsonResponse(data)
    elif request.method == 'POST':
        data = json.loads(request.body)
        student = Student.objects.create(
            name=data['name'],
            surname=data['surname'],
            year_of_study=data['year_of_study']
        )
        return JsonResponse({'student': student})

@csrf_exempt
def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'GET':
        data = {'student': model_to_dict(student)}
        return JsonResponse(data)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        student.name = data['name']
        student.surname = data['surname']
        student.year_of_study = data['year_of_study']
        student.save()
        return JsonResponse({'student': model_to_dict(student)})
    elif request.method == 'DELETE':
        student.delete()
        return JsonResponse({'deleted': True})

