from rest_framework import status 
from rest_framework import filters
from ..models import UserActivity
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import ActivitySerializer
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination



# Implement Filtering
class ActivityFilterView(generics.ListAPIView):
    queryset = UserActivity.objects.all()
    serializer_class = ActivitySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user_name', 'type', 'duration', 'calories_burned']


# Set the number of items per page  
class setPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page'


# Implement Pagination    
class ActivityPaginationView(ListAPIView):
    queryset = UserActivity.objects.all()
    serializer_class = ActivitySerializer  
    pagination_class = setPagination




class UserActivityView(APIView):

    def get(self, request, pk=None):
        if pk:
            activity = UserActivity.objects.get(id=pk)
            serializer = ActivitySerializer(activity, many = False)
            return Response({'data': serializer.data, 'message': 'Retrieved successfully'}, status=status.HTTP_200_OK)
        else:
            activity = UserActivity.objects.all()
            serializer = ActivitySerializer(activity, many = True)
            return Response({'data':serializer.data, 'msg': "Retrieved successfully"}, status=status.HTTP_200_OK)
               
          
    def post(self, request):
        data = request.data
        serializer = ActivitySerializer(data=data )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def put(self, request, pk):
        data = request.data
        activity = UserActivity.objects.get(id=pk)
        serializer = ActivitySerializer(activity, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk):
        try:
            activity = UserActivity.objects.get(id=pk)
            activity.delete()
            return Response({'msg': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({'msg': 'Activities not found'}, status=status.HTTP_404_NOT_FOUND)


































































