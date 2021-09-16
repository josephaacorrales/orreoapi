from rest_framework import viewsets
from api.models import Gw2Key
from api.serializers import Gw2KeySerializer

class UserGw2KeysViewSet(viewsets.ModelViewSet):
    """
    A ViewSet that allows a user to perform CRUD operations on their GW2 API Keys
    """
    queryset = Gw2Key.objects.all()
    serializer_class = Gw2KeySerializer

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)

    serializer = Gw2KeySerializer(queryset, many=True)