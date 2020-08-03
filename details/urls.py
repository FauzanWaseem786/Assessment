from . import views
from details.views import PersonView
from django.urls import path
app_name='details'
urlpatterns=[
    path('', views.country_create, name='country_create'),
    path('country_delete/<str:pk>/', views.country_delete, name='country_delete'),
    path('country_update/<str:pk>/', views.country_update, name='country_update'),
    path('country_retrieve/<str:pk>/', views.country_retrieve ,name='country_retrieve'),
    path('state_create/', views.state_create, name='state_create'),
    path('state_delete/<str:pk>/', views.state_delete, name='state_delete'),
    path('state_update/<str:pk>/', views.state_update, name='state_update'),
    path('state_retrieve/<str:pk>/', views.state_retrieve ,name='state_retrieve'),
    path('city_create/', views.city_create, name='city_create'),
    path('city_delete/<str:pk>/', views.city_delete, name='city_delete'),
    path('city_update/<str:pk>/', views.city_update, name='city_update'),
    path('city_retrieve/<str:pk>/', views.city_retrieve ,name='city_retrieve'),
    path('town_create/', views.town_create, name='town_create'),
    path('town_delete/<str:pk>/', views.town_delete, name='town_delete'),
    path('town_update/<str:pk>/', views.town_update, name='town_update'),
    path('town_retrieve/<str:pk>/', views.town_retrieve ,name='town_retrieve'),
    path('person_create/', views.person_create, name='person_create'),
    path('person_delete/<str:pk>/', views.person_delete, name='person_delete'),
    path('person_update/<str:pk>/', views.person_update, name='person_update'),
    path('person_retrieve/<str:pk>/', views.person_retrieve ,name='person_retrieve'),
    path('person_page/', PersonView.as_view(),name='PersonView'),


]
