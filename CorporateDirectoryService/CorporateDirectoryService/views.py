from django.http import HttpResponse,JsonResponse

def home_page(request):
    friend = [
        "Saurabh", "Krishna", "Avinash", "Amit"
    ]
    return JsonResponse(friend, safe=False)