from django.urls import path
from api import views
# from api.views import SearchGifsView

urlpatterns = [
    path('', views.search_results_view, name='home')
    # path('', SearchGifsView.as_view(), name='search_results')
]