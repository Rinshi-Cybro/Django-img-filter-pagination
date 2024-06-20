from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path('activity/', UserActivityView.as_view(), name='activity-list'),
    path('activity/get/<int:pk>/', UserActivityView.as_view(), name='activity-details'),
    path('activity/create/', UserActivityView.as_view(), name='activity-create'),
    path('activity/update/<int:pk>/', UserActivityView.as_view(), name='activity-update'),
    path('activity/delete/<int:pk>/', UserActivityView.as_view(), name='activity-delete'),
    # Url set Filter 
    path('activity/filter/', ActivityFilterView.as_view(), name='activity-filter'),
    # url set for Pagenation
    path('activity/pagination/', ActivityPaginationView.as_view(), name='activity-pagination')
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)