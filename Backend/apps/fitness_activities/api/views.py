from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from .serializers import ActivitySerializer
from ..models import UserActivity


# Create your views here.

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


































































