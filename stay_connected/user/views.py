from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from user.serializers import UserSerializer, UserLoginSerializer
from drf_spectacular.utils import extend_schema

# Create your views here.
@extend_schema(tags=["Auth"])
class RegisterView(APIView):
    """
    View for users registration
    """

    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def post(self,request,*args,**kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return Response({
                'message': 'Login successful',
                'user': UserSerializer(user).data
            })
        return Response({
            'message': 'Invalid credentials'
        }, status=status.HTTP_401_UNAUTHORIZED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@extend_schema( tags=["Auth"])
class LoginView(TokenObtainPairView):
    serializer_class = TokenObtainPairView.serializer_class


@extend_schema(tags=["Auth"])
class RefreshTokenCustomView(TokenRefreshView):
    serializer_class = TokenRefreshView.serializer_class