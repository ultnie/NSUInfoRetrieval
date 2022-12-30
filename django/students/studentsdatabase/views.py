from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.template.response import TemplateResponse

from . import forms, models


def index(request):
    return TemplateResponse(request, 'index.html')


def university(request, uni_id):
    try:
        curr_uni = models.universities.objects.get(id=uni_id)
        data = {"id": curr_uni.id, "fullName": curr_uni.fullName, "shortName": curr_uni.shortName, "creationDate": curr_uni.creationDate}
        return TemplateResponse(request, "uni.html", data)
    except models.universities.DoesNotExist:
        return HttpResponseNotFound("Университета с таким id не существует")


def create_unversity(request):
    if request.method == "POST":
        fullName = request.POST.get("fullName")
        shortName = request.POST.get("shortName")
        creationDate = request.POST.get("creationDate")
        models.universities.objects.create(fullName=fullName, shortName=shortName, creationDate=creationDate)
        return HttpResponseRedirect(f"/studentsdatabase/university/")
    else:
        data = {"form": forms.UniversityForm()}
        return TemplateResponse(request, "create_uni.html", data)


def delete_university(request, uni_id):
    try:
        uni = models.universities.objects.get(id=uni_id)
        uni.delete()
        return HttpResponseRedirect("/studentsdatabase/university/")
    except models.universities.DoesNotExist:
        return HttpResponseNotFound("Университета с таким id не существует")


def update_university(request, uni_id):
    uni = models.universities.objects.get(id=uni_id)
    if request.method == "POST":
        fName = request.POST.get("fullName")
        sName = request.POST.get("shortName")
        cDate = request.POST.get("creationDate")
        models.universities.objects.update(id=uni_id, fullName=fName, shortName=sName, creationDate=cDate)
        return HttpResponseRedirect(f"/studentsdatabase/university/{uni_id}")
    else:
        data = {"form": forms.UniversityForm(initial={'fullName': uni.fullName, 'shortName': uni.shortName, 'creationDate': uni.creationDate})}
        return TemplateResponse(request, "update_uni.html", data)


def university_list(request):
    all_unis = models.universities.objects.all()
    data = {"universities": all_unis}
    return TemplateResponse(request, "uni_list.html", data)


def student(request, student_id):
    try:
        curr_student = models.students.objects.get(id=student_id)
        data = {"id": curr_student.id, "firstName": curr_student.firstName, "lastName": curr_student.lastName,
                "patronymic": curr_student.patronymic, "birthDate": curr_student.birthDate,
                "university": curr_student.university, "year": curr_student.year}
        return TemplateResponse(request, "student.html", data)
    except models.universities.DoesNotExist:
        return HttpResponseNotFound("Студента с таким id не существует")


def create_student(request):
    if request.method == "POST":
        firstName = request.POST.get("firstName")
        lastName = request.POST.get("lastName")
        patronymic = request.POST.get("patronymic")
        birthDate = request.POST.get("birthDate")
        uni_id = request.POST.get("university")
        uni = models.universities.objects.get(id=uni_id)
        year = request.POST.get("year")
        models.students.objects.create(firstName=firstName, lastName=lastName, patronymic=patronymic, birthDate=birthDate, university=uni, year=year)
        return HttpResponseRedirect(f"/studentsdatabase/student/")
    else:
        data = {"form": forms.StudentForm()}
        return TemplateResponse(request, "create_student.html", data)


def delete_student(request, student_id):
    try:
        student = models.students.objects.get(id=student_id)
        student.delete()
        return HttpResponseRedirect("/studentsdatabase/student/")
    except models.students.DoesNotExist:
        return HttpResponseNotFound("Студента с таким id не существует")


def update_student(request, student_id):
    student = models.students.objects.get(id=student_id)
    if request.method == "POST":
        firstName = request.POST.get("firstName")
        lastName = request.POST.get("lastName")
        patronymic = request.POST.get("patronymic")
        birthDate = request.POST.get("birthDate")
        uni_id = request.POST.get("university")
        uni = models.universities.objects.get(id=uni_id)
        year = request.POST.get("year")
        models.students.objects.update(firstName=firstName, lastName=lastName, patronymic=patronymic,
                                       birthDate=birthDate, university=uni, year=year)
        return HttpResponseRedirect(f"/studentsdatabase/student/")
    else:
        data = {"form": forms.StudentForm(initial={'lastName': student.lastName, 'firstName': student.firstName,
                                                   'patronymic': student.patronymic, 'birthDate': student.birthDate,
                                                   'university': student.university, 'year': student.year})}
        return TemplateResponse(request, "update_uni.html", data)


def student_list(request):
    all_students = models.students.objects.all()
    data = {"students": all_students}
    return TemplateResponse(request, "student_list.html", data)