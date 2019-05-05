from django.shortcuts import render,HttpResponse,redirect,reverse
from django.views import View
from company import models
from company.forms import RoomForm
# Create your views here.



class StudentList(View):
    def get(self,request):
        title = "这是学生页面!"
        all_student = models.Student.objects.all()
        return render(request,'crm/student_list.html',
                      {"all_student":all_student,"title":title})

    def post(self,request):
        pass

def room_add(request):
    form_obj = RoomForm()
    if request.method == 'POST':
        form_obj = RoomForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('student_list'))
    return render(request,'crm/student_list.html',{"form_obj": form_obj})




class RoomList(View):
    def get(self,request):
        title = "这是班级页面!"
        all_room = models.Room.objects.all()
        return render(request, 'crm/room_list.html',
                      {"all_room":all_room,"title":title})

    def post(self,request):
        title = "这是班级添加页面!"
        all_room = models.Room.objects.all()
        return render(request, 'crm/room_list.html',
                      {"all_room": all_room, "title": title})


class CourseList(View):
    def get(self, request):
        title = "这是课程页面!"
        all_course = models.Course.objects.all()
        return render(request, 'crm/course_list.html',
                      {"all_course":all_course,"title":title})

    def post(self, request):
        pass





























