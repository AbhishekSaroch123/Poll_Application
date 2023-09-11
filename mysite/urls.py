
from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    # if user navigates to polls then we redirect to polls.urls
    path('polls/',include('polls.urls')),
    path('admin/', admin.site.urls),
]
