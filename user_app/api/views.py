from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

from django.core.exceptions import ObjectDoesNotExist

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
        

class LogoutAPIView(APIView):

    def post(self, request):
        return self.logout(request)

    def logout(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass

        # logout(request)

        return Response({"success": "Successfully logged out."},
                        status=status.HTTP_200_OK)



