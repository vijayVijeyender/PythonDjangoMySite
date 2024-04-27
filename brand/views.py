from rest_framework.views import APIView, Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from brand.models import *
from brand.serializers import *

@permission_classes([AllowAny])
class BrandView(APIView):

    def get(self, request):
        dept = Brand.objects.all()
        serializer = BrandSerializer(dept, many=True)
        return Response(serializer.data)

    def post(self, request):        
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, id):
        try:
            dept = Brand.objects.get(id=id)
        except Brand.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BrandSerializer(dept, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,{'message : updated successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        try:
            dept = Brand.objects.get(id=id)
        except Brand.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        dept.delete()
        return Response({"message":"deleted successfully"}, status=status.HTTP_204_NO_CONTENT)