from django.urls import path
from . import views

app_name = 'bids'

urlpatterns = [
    path('', views.FilmListView.as_view(), name='all'),
    #path('open', views.openpage, name='openpage'),
    path('bids/<int:pk>/detail', views.FilmDetailView.as_view(), name='bid_detail'),
    path('bids/create/', views.FilmCreateView.as_view(), name='bid_create'),
    path('bids/<int:pk>/update/', views.FilmUpdateView.as_view(), name='bid_update'),
    path('bids/<int:pk>/delete/', views.FilmDeleteView.as_view(), name='bid_delete'),
    path('bids/<int:pk>/delete/', views.FilmDeleteView.as_view(), name='bid_delete'),
    path("index1", views.index1, name="index1")

]
