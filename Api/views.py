from Api.models import AssetsModel, CheckIn, CheckOut, CheckOutAndReturn, DeviceLog, Company
from Api.serializers import UserSerializer, RegisterSerializer, AssetSerializer, CheckInSerializer, RegisterSerializer, CheckOutSerializer, CheckOutAndReturnSerializer, DeviceLogSerializer, CompanySerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated

##############
from rest_framework import generics
from rest_framework.response import Response
from knox.models import AuthToken

########################
# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })
          

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
    
    