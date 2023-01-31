from django.urls import path
from . import views1

urlpatterns=[
    path('api/course', views1.course_list),
    path('api/course/<id>', views1.course_detail),
    path('api/course/published', views1.course_list_published)
]