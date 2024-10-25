import json
from django.views.decorators.csrf  import csrf_exempt
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from .models import CustomUser
from  rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from  .serializers import InputSerializer
from  rest_framework.response import Response
from.serializers import OutputSerializer
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.

class SignUp(APIView):
    premisos=[AllowAny]
    def post(self,request):
        serielizar_data=InputSerializer(data=request.data)
        serielizar_data.is_valid(raise_exeption=True)
        if CustomUser.objects.filter(email=serielizar_data.validated_data['email']).exists():
            return Response('email alerey resquistere', status=status.HTTP_400_BAD_REQUEST)
        if CustomUser.objects.filter(username=serielizar_data.validated_data['username']).exists():
            return Response('username alerey resquistere', status=status.HTTP_400_BAD_REQUEST)
        user=CustomUser.objects.create_user( **serielizar_data.validated_data)
        refresh=RefreshToken.for_user(user)
        serielizar_data = OutputSerializer({
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "birth_date": user.birth_date,
            "biography": user.biography,
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
        })
        return Response('user se creo exitosamenet', status= status.HTTP_200_OK)
        
        
        
        
# def users_list(request, pk=None):
#     if request.method == "GET":
#         if pk:
#             try:
#                 user = CustomUser.objects.get(id=pk)
#                 return JsonResponse(data={
#                     "mensaje": "oki",
#                     "id": user.id,
#                     "username": user.username,
#                     "email": user.email,
#                     "birth_date": user.birth_date,
#                     "biography": user.biography
#                 })
#             except CustomUser.DoesNotExist:
#                 return JsonResponse({"mensaje": "Usuario no encontrado"}, status=404)
#         else:
#             users = list(CustomUser.objects.all().values("id", "username", "email", "birth_date", "biography"))
#             return JsonResponse({"mensaje": "el get funciono", "users": users})

#     return HttpResponse("Method not allowed", status=405)

# @csrf_exempt
# def create_user(request):
#     if request.method == "POST":
#         # Getting data
#         decoded_body = request.body.decode('utf-8')
#         body = json.loads(decoded_body)

#         # Data validation
#         errors = []
#         if body['username'] == "":
#             errors.append({'username': 'username cannot be empty'})

#         if body['birth_date'] == "":  # TODO: Validate date format
#             errors.append({'birth_date': 'Incorrect date format'})

#         if body['email'] == "":  # TODO: Validate email format
#             errors.append({'email': 'Incorrect email format'})

#         if len(errors) > 0:
#             return JsonResponse({'errors': errors}, status=400)

#         # Saving data in DB:
#         user = CustomUser.objects.create(
#             username=body['username'],
#             password=body['password'],
#             email=body['email'],
#             birth_date=body['birth_date'],
#             biography=body['biography']
#         )

#         return JsonResponse(data={'message': 'Created user', 'id': user.id, 'username': user.username} , status= 201)

#     return HttpResponse("Method not allowed", status=405)



# import json
# from django.views.decorators.csrf import csrf_exempt
# from django.http import JsonResponse, HttpResponse
# from .models import CustomUser

# @csrf_exempt
# def user_detail(request, pk=None):
#     if request.method == "PATCH":
#         try:
#             user = CustomUser.objects.get(id=pk)
#         except CustomUser.DoesNotExist:
#             return JsonResponse({"mensaje": "Usuario no encontrado"}, status=404)

#         # Obtener y decodificar los datos
#         decoded_body = request.body.decode('utf-8')
#         body = json.loads(decoded_body)

#         # Actualizar solo los campos que están en el cuerpo de la solicitud
#         if 'username' in body:
#             user.username = body['username']
#         if 'password' in body:
#             user.password = body['password']  # Considera hashear la contraseña
#         if 'email' in body:
#             user.email = body['email']
#         if 'birth_date' in body:
#             user.birth_date = body['birth_date']
#         if 'biography' in body:
#             user.biography = body['biography']

#         # Guardar los cambios en la base de datos
#         user.save()

#         return JsonResponse(data={
#             'message': 'usuario actualizado con exito',
#             'id': user.id,
#             'username': user.username,
#             'email': user.email,
#             'birth_date': user.birth_date,
#             'biography': user.biography
#         })

#     return HttpResponse("Method not allowed", status=405)


# @csrf_exempt
# def delete_user(request, pk=None):
#     if request.method=="DELETE": 
#         if pk:
#             CustomUser.objects.filter(id=pk).delete()
#             return JsonResponse(data={"message": "Usuario con el id = " + str(pk) + " ha sido eliminado"})
        
#     return HttpResponse("Method not allowed", status=405)

