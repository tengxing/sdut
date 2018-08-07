# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from django.http import HttpResponse
import json


def get_params(request):
    dict = {}
    if request.method == 'GET':
        print(request.query_params)
        for k in request:
            dict[k] = request.query_params[k]

        return dict

    elif request.method == 'POST':

        for k in request:

            dict[k] = request.data[k]

        return dict


# index
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@csrf_exempt
def hello(request):
    result = {"code": 200, "msg": "ok"}
    if request.method == 'GET':
        result['msg'] = "this is not a GET method !"
    elif request.method == 'POST':
        result['msg'] = "this is not a POST method !"
    else:
        result['code'] = 404
        result['msg'] = "this is not a human method !"
    return HttpResponse(json.dumps(result))
