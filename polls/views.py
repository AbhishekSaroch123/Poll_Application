# from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

from django.http import HttpRequest,HttpResponse,JsonResponse

def index(request):
    return HttpResponse("Hello , What Are You Doing")

def detail(request:HttpRequest)-> JsonResponse:
        data={
            "id":1,
            "username":"abhishek"
        }
        return JsonResponse(data)
    

