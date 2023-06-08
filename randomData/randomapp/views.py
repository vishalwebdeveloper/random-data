
from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from rest_framework import viewsets,status
from .serializer import *
from .models import *
from random import randint

# class modelViewset(viewsets.ModelViewSet):
#     queryset = Model.objects.all()
#     serializer_class = ModelSerializer

#     def create(self, request, *args, **kwargs):
#         data = self.generate_random_data()  # Function that generates random data
#         serializer = self.get_serializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         # headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     def generate_random_data(self):
#         # Generate random data based on your requirements
#         random_name = "Random Name " + str(random.randint(1, 100))
#         # Generate other random data fields
#         return {'name': random_name}
    

# class StudentViewset(viewsets.ModelViewSet):
#     queryset = student.objects.all()
#     serializer_class = studentSerializer

#     def list(self, request, *args, **kwargs):
#         n= request.POST.get('record')
#         i=1
#         while i<=n:
#             random_number = randint(1, 14)  # Generate a random number
#             print(random_number)
#             filter_queryset = self.filter_queryset(self.get_queryset().filter(roll=random_number))
#             # for data in filter_queryset:
#             #     another = record.objects.create(roll=data.roll,name=data.name,city=data.city)
#             #     another.save()
#             serializer = self.get_serializer(filter_queryset, many=True)
#             i+=1
#         return Response(serializer.data)
        


class StudentViewset(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = studentSerializer

    def list(self, request, *args, **kwargs):
        n= request.POST.get('record')
        i=1
        while i<=n:
            random_number = randint(1, 14)  # Generate a random number
            print(random_number)
            filter_queryset = self.filter_queryset(self.get_queryset().filter(roll=random_number))
            # for data in filter_queryset:
            #     another = record.objects.create(roll=data.roll,name=data.name,city=data.city)
            #     another.save()
            serializer = self.get_serializer(filter_queryset, many=True)
            i+=1
        return Response(serializer.data)