from django.shortcuts import render
from rest_framework.views import APIView
from .models import (
    React,
)
from rest_framework.response import Response
from .serializers import (
    ReactSerializer,
)
from rest_framework import status


class ReactView(APIView):
    def get(self, request):
        outputs = [
            {"employee": item.employee, "department": item.department}
            for item in React.objects.all()
        ]
        return Response(outputs)

    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"status": "Employee created successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
