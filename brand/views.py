from rest_framework.views import APIView, Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from brand.models import *
from brand.serializers import *

@permission_classes([AllowAny])
class BrandView(APIView):

    def get(self, request):
        brandList = Brand.objects.all()
        brandDetails = BrandSerializer(brandList, many=True)
        return Response(brandDetails.data)

    def post(self, request):        
        newBrandDetails = BrandSerializer(data=request.data)
        if newBrandDetails.is_valid():
            newBrandDetails.save()
            return Response(newBrandDetails.data, status=status.HTTP_201_CREATED)
        else:
            return Response(newBrandDetails.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, id):
        try:
            brand = Brand.objects.get(id=id)
        except Brand.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        updatedBrandDetails = BrandSerializer(brand, data=request.data, partial=True)
        if updatedBrandDetails.is_valid():
            updatedBrandDetails.save()
            return Response(updatedBrandDetails.data,{'message : updated successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(updatedBrandDetails.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        try:
            brand = Brand.objects.get(id=id)
        except Brand.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        brand.delete()
        return Response({"message":"deleted successfully"}, status=status.HTTP_204_NO_CONTENT)