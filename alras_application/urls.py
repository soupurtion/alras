from django.urls import path
from . import views


urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
path('', views.index, name='index'),
path('labroom/', views.LabRoomListView.as_view(), name= 'labroom'),
path('labroom/<int:pk>', views.LabRoomDetailView.as_view(), name='labroom-detail'),
path('labroom/<int:pk>/reserve_slot/', views.reserveSlot, name='reserve_slot'),
path('labroom/<int:pk>/cancel_slot/', views.cancelSlot, name='cancel_slot'),
path('labroom/<int:pk>/update_slot/', views.updateSlot, name='update_slot'),
#path('labroom/reserve_slot/', views.reserveAnySlot, name='reserve_any_slot'),
#path('labroom/cancel_slot/', views.cancelAnySlot, name='cancel_any_slot'),
#path('labroom/update_slot/', views.updateAnySlot, name='update_any_slot'),
]
