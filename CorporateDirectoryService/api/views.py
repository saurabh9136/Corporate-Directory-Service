
from rest_framework import viewsets
from rest_framework.decorators import action
from api.models import Company,Employee
from api.serializers import CompanySerializer,EmployeeSerializer
from rest_framework.response import Response
# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=True, methods=['get']) #details will check if pk is passed or not meehtods define the http methods
    def employees(self, request, pk=None):

        try:
            company = Company.objects.get(pk=pk)
            emp_data = Employee.objects.filter(company =  company)
            # now we have a data which we need to return but before that serialize it 
            emp_serialize_dat = EmployeeSerializer(emp_data, many=True, context={'request':request})

            return Response(emp_serialize_dat.data)
        except:
            return Response(
                {'message' : 'Company not found'}
            )


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

   
