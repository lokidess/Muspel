from django.contrib import admin
from django.urls import path, include
from Course.views import CourseDetailView, LectureDetalView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('payments.urls')),
    path('coursedital/<int:pk>/', CourseDetailView.as_view(), name='coursedital'),
    path('lecture/<int:pk>/', LectureDetalView.as_view(), name='lecture_detail'),

]
