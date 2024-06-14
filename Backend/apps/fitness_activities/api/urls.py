from django.urls import path
from .views import UserActivityView


urlpatterns = [
    path('activity/', UserActivityView.as_view(), name='activity-list'),
    path('activity/get/<int:pk>/', UserActivityView.as_view(), name='activity-details'),
    path('activity/create/', UserActivityView.as_view(), name='activity-create'),
    path('activity/update/<int:pk>/', UserActivityView.as_view(), name='activity-update'),
    path('activity/delete/<int:pk>/', UserActivityView.as_view(), name='activity-delete')
]