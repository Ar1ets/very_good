from django.http import HttpResponse
from blog import models as bm
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def main(request):
    if request.method == "POST":
        myjson = request.POST
        arr = str(list(myjson.dict().keys())[0]).split()
        try:
            r = bm.update_rating(int(arr[0]), int(arr[1]))
        except ValueError:
            r = 0
        return HttpResponse(r)
    else:
        return HttpResponse("nil")
