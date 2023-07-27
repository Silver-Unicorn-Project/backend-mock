from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.


class CustomTokenObtainPairView(TokenObtainPairView):
    # Customize the response data if needed
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        # Add any additional data to the response here
        return response