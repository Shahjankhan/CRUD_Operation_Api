
from django.contrib import admin
from django.urls import path
from Api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_Api/', views.student_Api),
]
    
