from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from user_app.api.serializers import RegistrationSerializer

# Create your views here.
class RegistrationAPIView(APIView):
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid(raise_exception=True):
            account = serializer.save()
            data["username"] = account.username
            data["email"] = account.email
            data["token"] = Token.objects.get_or_create(user=account)[0].key
            return Response(data)
        else:
            return Response(serializer.errors)
        
    
