from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from .serializers import UserSerializer , UserProgressSerializer,DormitorysSerializer
from .models import UserProgress ,Dormitory


class  UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny, ]

class  UserProgressViewSet(viewsets.ModelViewSet):
    queryset = UserProgress.objects.all()
    serializer_class = UserProgressSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]


    def get_queryset(self, *args, **kwargs):
        
        user = self.request.user.id
        print ('User',user)
        qs = UserProgress.objects.filter(user=user)

        return qs

    
class  DormitorysViewSet(viewsets.ModelViewSet):
    queryset = Dormitory.objects.all()
    serializer_class = DormitorysSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]


    def get_queryset(self, *args, **kwargs):
            
        user = self.request.user.id
 
        print ('User',user)
   
        qs = Dormitory.objects.filter(user=user)
        return qs