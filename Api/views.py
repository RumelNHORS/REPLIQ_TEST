from Api.models import AssetsModel, CheckIn, CheckOut, CheckOutAndReturn, DeviceLog, Company
from Api.serializers import AssetSerializer, CheckInSerializer, RegisterSerializer, CheckOutSerializer, CheckOutAndReturnSerializer, DeviceLogSerializer, CompanySerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated

#For User Creations
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken


from django.contrib.auth import login



class AssetViewSet(viewsets.ModelViewSet):
    queryset = AssetsModel.objects.all()
    serializer_class = AssetSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
class CheckInViewSet(viewsets.ModelViewSet):
    queryset = CheckIn.objects.all()
    serializer_class = CheckInSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    
    
class CheckOutViewSet(viewsets.ModelViewSet):
    queryset = CheckOut.objects.all()
    serializer_class = CheckOutSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

class CheckOutAndReturnSerializerViewSet(viewsets.ModelViewSet):
    queryset = CheckOutAndReturn.objects.all()
    serializer_class = CheckOutAndReturnSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

class DeviceLogViewSet(viewsets.ModelViewSet):
    queryset = DeviceLog.objects.all()
    serializer_class = DeviceLogSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

class CompanyCViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
#For User Creations
@api_view(['POST'])
def login_api(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    _, token = AuthToken.objects.create(user)
    
    return Response({
        'user_info':{
            'id':user.id,
            'username':user.username,
            'email':user.email
        },
        'token':token
    })

@api_view(['GET'])
def get_user_data(request):
    user = request.user
    
    if user.is_authenticate:
        return Response({
            'user_info':{
                'id':user.id,
                'username':user.username,
                'email':user.email
            }
        })
    return Response({'erroe':'Not Authenticcated'}, status=400)


@api_view(['POST'])
def register_api(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    user = serializer.save()
    _, token = AuthToken.objects.create(user)
    
    return Response({
        'user_info':{
            'id':user.id,
            'username':user.username,
            'email':user.email
        },
        'token':token
    })

