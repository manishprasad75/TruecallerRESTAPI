from .models import UserProfile
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser
from .utility import isvalid


# Create your views here.

@csrf_exempt
def registration(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        try:
            context = JSONParser().parse(stream)
        except:
            return JsonResponse({'msg': 'Invalid Json'}, status=400)

        (status, msg) = isvalid(context)

        if status:
            user = User.objects.create_user(context.get('phone'), context.get('email'), context.get('password'))
            user.first_name = context['first_name']
            user.last_name = context['last_name']
            user.save()

            profile = UserProfile(user_id=user, phone=context['phone'])
            profile.save()
            return JsonResponse({'msg': 'Successfully Created!!'})
        else:
            return JsonResponse({'msg': msg}, status=400)
    return JsonResponse({'msg': 'Invalid method, Only Post request allowed!!'}, status=400)
