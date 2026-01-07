from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serilizers

# Create your views here.
class Register(APIView):
    def post(self, request):
        serilizer = serilizers.RegisterSer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(data={"message": "successfuly registerd"}, status=status.HTTP_201_CREATED)
        return Response(data={"message": "not registerd", "errors": serilizer.errors}, status=status.HTTP_400_BAD_REQUEST)