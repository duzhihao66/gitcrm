
from django.conf.urls import url,include
from company.views import StudentList,RoomList,CourseList
from company import views

urlpatterns = [
    # url(r'^home/', Home.as_view()),
    url(r'^student_list/$', StudentList.as_view(),name='my_student'),
    url(r'^room_list/$', RoomList.as_view(),name='my_room'),
    url(r'^room_add/$',views.room_add,name='room_add'),
    url(r'^course_list/$', CourseList.as_view(),name='my_course'),
]
