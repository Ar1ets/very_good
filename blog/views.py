from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def index(request):
    global resp
    hasCookie = False

    if "color" in request.COOKIES:
        resp = f"Your favorite color is {request.COOKIES['color'].split()[-1]}"
    else:
        resp = "black"
        hasCookie = True
    context = {"resp": resp}
    response = render(request, "index_blog.html", context)
    if not hasCookie:
        response.set_cookie("color", resp, path="blog")
    return response