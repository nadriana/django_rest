from email.iterators import body_line_iterator
import json
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    # request -> HttpRequest -> Django 
    # request es de Django y no es requests de python
    # json from request.body
    print(request.GET) # url query parameters
    body = request.body # byte string of JSON data
    data = {}

    try:
        data = json.loads(body) #string of JSON data to Python dictionary
    except:
        pass

    print(data)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers) # antes request.META
    data['content_type'] = request.content_type
    return JsonResponse(data)