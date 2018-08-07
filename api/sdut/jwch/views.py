# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from django.http import HttpResponse
from django.http import StreamingHttpResponse

import json
from . import jwcScore
from . import excel


@csrf_exempt
def info(request):
    data = {"post_xuehao":""}
    result = {"code": 200, "msg": "ok"}
    if request.method == 'GET':
        data['post_xuehao'] = request.GET.get("std_id")
    elif request.method == 'POST':
        data['post_xuehao'] = json.loads(str(request.body,"utf-8")).get("std_id")
        #data['post_xuehao'] = request.body.get("std_id")
    else:
        print("")
    result = jwcScore.get_std_info(data)
    jwcScore.write_file("data/"+data["post_xuehao"], result)
    return HttpResponse(result,content_type='application/json; charset=utf-8')


@csrf_exempt
def download(request):
    id = ''
    if request.method == 'GET':
        id = request.GET.get("std_id")
    elif request.method == 'POST':
        id = json.loads(str(request.body,"utf-8")).get("std_id")
    else:
        print("")

    excel.shengcheng(id)

    the_file_name = 'data/' + id + '.xlsx'

    def file_iterator(file_name, chunk_size=512):
        with open(file_name, 'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(id + ".xlsx")
    print(response.status_code)
    return response