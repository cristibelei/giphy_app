
import requests
from django.shortcuts import render
from django.views.decorators.debug import sensitive_variables


@sensitive_variables('url')
def search_results_view(request):
    search_query = request.GET.get("q")
    context = {}
    if search_query is not None:
        url = f"https://api.giphy.com/v1/gifs/search?api_key=xnrTiiLdBYWD2qPjYYUDieQyww7I2QPa&q={search_query}"
        response = requests.get(url)
        response_json = response.json()
        images = response_json['data']

        context = {
            "images": images
        }

    return render(request, 'home.html', context)


