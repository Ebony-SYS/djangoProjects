from django.contrib import admin
from django.urls import path
from mooc.views import home, contact, courses

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('contato/', contact, name='contato'),
    path('cursos/', courses, name='cursos')
]
