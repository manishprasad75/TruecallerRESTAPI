from user.models import UserProfile
from mysite.models import UsersContact, UserSpam
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from django.core.serializers import serialize
import io, json
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q


# Create your views here.

def findSpamStatus(phone):
    count = UserSpam.objects.filter(phone=phone).count()
    spam_status = "No"

    if 10 < count < 20:
        spam_status = "Likely"
    if count > 20:
        spam_status = "Most Likely"
    return spam_status


class Search(APIView):
    """
    Search query
    """

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        json_data = request.body
        stream = io.BytesIO(json_data)
        try:
            context = JSONParser().parse(stream)
        except:
            return JsonResponse({'msg': 'Invalid Json'}, status=400)

        query = context.get('query')
        user_id = request.user

        data = UserProfile.objects.filter(phone=query).first()
        if data is not None:
            context = {
                'first_name': data.user_id.first_name,
                'last_name': data.user_id.last_name,
                'phone': data.phone
            }
            context['spam_status'] = findSpamStatus(context.get('phone'))
            tmp = UsersContact.objects.filter(phone=data.phone, synced_from_uid=user_id).first()

            # import pdb
            # pdb.set_trace()

            if tmp is not None:
                context['email'] = data.user_id.email

            return JsonResponse(context)

        queryset = UsersContact.objects.filter(phone=query)
        # import pdb
        # pdb.set_trace()
        if len(queryset) != 0:
            data = serialize('json', list(queryset), fields=('first_name', 'last_name', 'phone', 'synced_from_uid'))
            python_data = json.loads(data)
            context = list()
            for data in python_data:
                if data.get('fields').get('synced_from_uid') == user_id:
                    data['fields']['email'] = user_id.email
                del data['fields']['synced_from_uid']
                data['fields']['spam_status'] = findSpamStatus(data['fields']['phone'])
                context.append(data.get('fields'))
            return JsonResponse(context, safe=False)

        query = query.strip()
        query = query.split(' ')
        start_with_q = UsersContact.objects.filter(Q(first_name__startswith=query[0])).only('first_name', 'last_name', 'phone', 'synced_from_uid')
        contains_q = UsersContact.objects.filter(first_name__icontains=query[0]).exclude(first_name__startswith=query[0]).only('first_name', 'last_name', 'phone', 'synced_from_uid')
        start_with = serialize('json', list(start_with_q), fields=('first_name', 'last_name', 'phone', 'synced_from_uid'))
        contains = serialize('json', list(contains_q), fields=('first_name', 'last_name', 'phone', 'synced_from_uid'))
        python_data = json.loads(start_with)
        context1 = list()
        context2 = list()
        for data in python_data:
            if data.get('fields').get('synced_from_uid') == user_id:
                data['fields']['email'] = user_id.email
            del data['fields']['synced_from_uid']
            data['fields']['spam_status'] = findSpamStatus(data['fields']['phone'])
            context1.append(data.get('fields'))

        python_data = json.loads(contains)

        for data in python_data:
            if data.get('fields').get('synced_from_uid') == user_id:
                data['fields']['email'] = user_id.email
            del data['fields']['synced_from_uid']
            data['fields']['spam_status'] = findSpamStatus(data['fields']['phone'])
            context2.append(data.get('fields'))

        return JsonResponse({"start_with": context1, "contain": context2}, safe=False)
