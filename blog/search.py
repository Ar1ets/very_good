from django.shortcuts import render
from django.http import HttpResponse
from blog import models as bm
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def main(request):
    if request.method == 'GET':
        query = request.GET['search']
        content = bm.getPostsById(bm.getPostsBySubstring(query))
        context = {
            'jumoreski': content
        }
        return render(request, "index_main.html", context)
    else:
        return HttpResponse('500')