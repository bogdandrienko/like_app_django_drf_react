import time

from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.cache import caches
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework import status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from django_app import models, serializers as django_serializers

# Create your views here.

Cache = caches["default"]


def index(request):
    return render(request, "index.html")


def time_measure(func):
    def wrapper(*args, **kwargs):

        # проверка на логин
        request = args[0]
        if request.user.username is None:
            raise Exception("Login Requried")

        # замер скорости
        # определение токена пользователя
        # кэш
        # логировать
        # ...

        time_start = time.perf_counter()

        try:
            result = func(*args, **kwargs)
        except:
            pass

        time_stop = time.perf_counter()

        print("Elapsed time: ", round(time_stop - time_start, 5))
        return result

    return wrapper


@api_view(http_method_names=["GET"])
# @permission_classes([IsAuthenticated])
@permission_classes([AllowAny])
def get_data(request: Request) -> Response:
    """Данная функция создана для проверки"""
    print(request.user)

    # username = request.data["username"]
    # password = request.data["password"]
    # avatar = request.data["avatar"]

    usr = User.objects.get(id=1)
    usr_json = django_serializers.UserSerializer(instance=usr, many=False).data

    return Response(data=usr_json, status=status.HTTP_200_OK)


class GetData(APIView):
    def get(self, request, *args, **kwargs):
        usr = User.objects.get(id=1)
        usr_json = django_serializers.UserSerializer(instance=usr, many=False).data
        return Response(data=usr_json, status=status.HTTP_200_OK)
        # return HttpResponse("Hello async world!")


@time_measure
def user_all(request: HttpRequest) -> JsonResponse:
    username = ""
    password = ""

    user = authenticate(username=username, password=password)
    if user is not None:
        # пользователь не определён
        # 404, данные не подходят
        pass
    else:
        login(request, user)  # TODO ! MVT authenticate
    # 1) У браузера есть логин и пароль, но каждый раз их "подкидывать" в запрос небезопасно
    # 2) Первый раз он их из формы отправляет на backend
    #  user  |  token                  | time
    #  admin | qqfiluwhnefiuqe143124    | 23.03.2023
    # 3) происходит сопоставление данных (authenticate)
    # 4) происходит сохранение токена в cookies (login)  # TODO ! MVT
    # 4) При каждом запросе ты предъявляешь этот токен

    # request.user

    # pk = 1
    # user = User.objects.get(id=pk).profile.avatar  # models.Profile.objects.get(user=user)
    # print(user)
    # profile = models.Profile.objects.get(user=user)
    # print(profile.avatar)

    # for i in range(500, 550):
    #     User.objects.create(username=f"Bogdan_{i}", password=make_password(f"Bogdan {i}"), first_name=f"Bogdan {i}")

    # Cache.get("user_all")
    # Cache.set("user_all", users, timeout=5)

    # 0.00564 - 1x pep
    # 0.00035 - 1000x pep = 0.00564 + 0.35 = 0.35564
    # 0.00035 - 100000x pep = 0.00564 + 35.0 = 35.564
    # users_json = Cache.get("user_all")
    # if users_json is None:
    #     # todo ДАННЫХ В КЭШЕ НЕТ ИЛИ ОНИ ПРОСРОЧИЛИСЬ, ПОЭТОМУ НУЖНО ИДТИ В МЕДЛЕННУЮ БАЗУ ДАННЫХ
    #     users = User.objects.all()  # QuerySet
    #     users_json = []
    #     for user in users:
    #         users_json.append({"id": user.id, "username": user.username})
    #     Cache.set("user_all", users_json, timeout=10)
    # else:
    #     # todo ДАННЫЕ ЕСТЬ В КЭШЕ, ПОЭТОМУ МОЖНО НЕ ИДТИ В МЕДЛЕННУЮ БАЗУ ДАННЫХ
    #     pass

    # 0.00513   1x pep
    # 0.00513   1000x pep = 5.13 s
    # 0.00513   100000x pep = 500.13 s
    # users = User.objects.all()  # QuerySet
    # users_json = []
    # for user in users:
    #     users_json.append({"id": user.id, "username": user.username})

    return JsonResponse(data={}, safe=False)  # Json
    # return JsonResponse(data=users_json, safe=False)  # Json
