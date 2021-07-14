
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .crawl_category import crawler, get_all_categories

@api_view(['GET', 'POST'])
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        all_cat = get_all_categories('https://www.snapdeal.com/page/sitemap')
        # print(list(all_cat.keys()))
        data = {'author':'krisskad', 'email':'krishna.g.kadam98500@gmail.com',
                'example_request': {'category':'category_names'}, "available_categories":list(all_cat.keys())}
        return JsonResponse(data, status=201)

    elif request.method == 'POST':
        req = request.data
        if isinstance(req, dict):

            category = req['category']
            # Crawler function
            json_result = crawler(category)

            return JsonResponse(json_result, status=201)

        else:
            data = {"status": "Error, Please provide json formatted request"}
            return JsonResponse(data, status=201)

