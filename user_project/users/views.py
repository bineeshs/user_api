import csv
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

class UploadCSVAPIView(APIView):
    
    def post(self, request): 
        try:              
            file = request.FILES.get('file')
       
            if not file or not file.name.endswith('.csv'):
               return Response({"error": "Only .csv files are allowed."}, status=status.HTTP_400_BAD_REQUEST)

            decoded_file = file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)

            int_succ_count = 0
            int_err_count = 0
            errors = []
        

            for index, row in enumerate(reader, start=1):
                serializer = UserSerializer(data=row)
                if serializer.is_valid():                
                    if not User.objects.filter(email=serializer.validated_data['email']).exists():
                       serializer.save()
                       int_succ_count += 1
                    else:
                        errors.append({"row": index,"error": {"email": "Duplicate email address."}})
                        int_err_count += 1
                else:
                    errors.append({"row": index,"error": serializer.errors})
                    int_err_count += 1

            return Response({"int_succ_count": int_succ_count,"int_err_count": int_err_count,"error": errors}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
