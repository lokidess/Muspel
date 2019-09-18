from django.urls import path

from Course.views import charge

urlpatterns = [
    path('charge/', charge, name='charge'),
]