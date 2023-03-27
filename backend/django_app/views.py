import time

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.cache import caches
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django_app import models

# Create your views here.

Cache = caches["default"]


def time_measure(func):
    def wrapper(*args, **kwargs):
        time_start = time.perf_counter()

        result = func(*args, **kwargs)

        time_stop = time.perf_counter()

        print("Elapsed time: ", round(time_stop - time_start, 5))
        return result

    return wrapper


@time_measure
def user_all(request: HttpRequest) -> JsonResponse:
    # pk = 1
    # user = User.objects.get(id=pk).profile.avatar  # models.Profile.objects.get(user=user)
    # print(user)
    # profile = models.Profile.objects.get(user=user)
    # print(profile.avatar)

    for i in range(500, 550):
        User.objects.create(
            username=f"Bogdan_{i}",
            password=make_password(f"Bogdan {i}"),
            first_name=f"Bogdan {i}"
        )

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
