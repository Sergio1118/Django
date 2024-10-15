import json
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from users.models import CustomUser
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
@csrf_exempt
def users_list(request):
    if request.method=="GET":
        user=list(CustomUser.objects.all().values("username","password","email","birth_date","biography"))
        return JsonResponse(data={"message": "ok", "users":user})
    return HttpResponse("Method not allowed", status=405)

@csrf_exempt
def user_detail(request, name):
    if request.method=="GET":
        if name:
            user=CustomUser.objects.get(username=name)
            return JsonResponse(data={"message": "ok","mame":user.username,"email":user.email})
        return HttpResponse("Method not allowed", status=405)


@csrf_exempt
def create_user(request):
    if request.method == "POST":
        # Getting data
        decoded_body = request.body.decode('utf-8')
        body = json.loads(decoded_body)

        # Data validation
        errors = []
        if body['username'] == "":
            errors.append({'username': 'username cannot be empty'})

        if body['birth_date'] == "":  # TODO: Validate date format
            errors.append({'birth_date': 'Incorrect date format'})

        if body['email'] == "":  # TODO: Validate email format
            errors.append({'birth_date': 'Incorrect email format'})

        if len(errors) > 0:
            return JsonResponse({'errors': errors}, status=400)

        # Saving data in DB:
        user = CustomUser.objects.create(
            username=body['username'],
            password=body['password'],
            email=body['email'],
            birth_date=body['birth_date'],
            biography=body['biography']
        )
        return JsonResponse(data={'message': 'Created user', 'id': user.id, 'username': user.username})

    return HttpResponse("Method not allowed", status=405)

@csrf_exempt
def update_user(request, name):
    if request.method=="PATCH":
        if name:
            user=CustomUser.objects.get(username=name)
            decoded_body = request.body.decode('utf-8')
            body = json.loads(decoded_body) 
            if body['username'] != "":
                user.username=body["username"]
                return JsonResponse(data={"message": "ok","mame":user.username})
            elif body['username'] != "" and body["password"]!="":
                user.username=body["username"]
                user.password=body["password"]
                return JsonResponse(data={"message": "ok","mame":user.username, "password":user.password})
            elif body['username'] != "" and body["password"]!="" and body["email"]:
                user.username=body["username"]
                user.password=body["password"]
                user.email=body["email"]
                return JsonResponse(data={"message": "ok","mame":user.username, "password":user.password, "email": user.email})
            elif body['username'] != "" and body["password"]!="" and body["email"] and body["birth_date"]!="":
                user.username=body["username"]
                user.password=body["password"]
                user.email=body["email"]
                user.birth_date=body["birth_date"]
                return JsonResponse(data={"message": "ok","mame":user.username, "password":user.password, "email": user.email, "date": user.birth_date})
            elif body['username'] != "" and body["password"]!="" and body["email"] and body["birth_date"]!="" and body["biography"]!="":
                user.username=body["username"]
                user.password=body["password"]
                user.email=body["email"]
                user.birth_date=body["birth_date"]
                user.biography=body["biography"]
                return JsonResponse(data={"message": "ok","mame":user.username, "password":user.password, "email": user.email, "date": user.birth_date, "biography":user.biography})
    return HttpResponse("Method not allowed", status=405)





@csrf_exempt
def delete_user(request, name):
    pass

