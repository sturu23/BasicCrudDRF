from rest_framework import generics
from .models import Item, Location
from .serializers import ItemSerializer, LocationSerializer


class ItemList(generics.ListCreateAPIView):

    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        location = self.request.query_params.get('location', None)
        if location is not None:
            queryset = queryset.filter(item_location__location_name=location)
        return queryset
    

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    
        queryset = Item.objects.all()
        serializer_class = ItemSerializer


class LocationList(generics.ListCreateAPIView):
         
        serializer_class = LocationSerializer
        queryset = Location.objects.all()
    
class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    
        queryset = Location.objects.all()
        serializer_class = LocationSerializer