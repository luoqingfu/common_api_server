#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   SendRequest.py    
@Contact :   746832476@qq.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/11 下午4:32   luoqingfu   1.0         None
'''

# import lib
import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api_man.serializers import ApiSendSerializer


class SendRequest(APIView):

    def post(self, request):
        """
        发送http请求
        :param request:
        :return: response
        """

        data = ApiSendSerializer(data=request.data, partial=True)
        if data.is_valid():
            data = data.initial_data
            url = data['url']
            api_method = data['api_method']
            if api_method == 'get':
                res = requests.get(url=url)
                return Response({
                    'code': status.HTTP_200_OK,
                    'message': '请求成功',
                    'data': res.json()
                })
            elif api_method == 'post':
                request_data = eval(data['request_data'])  # 输出原始字符串，不然会有斜杠
                res = requests.post(url=url, data=request_data)
                return Response({
                    'code': status.HTTP_200_OK,
                    'message': '请求成功',
                    'data': res.json()
                })
            else:
                return Response({
                    'code': status.HTTP_400_BAD_REQUEST,
                    'message': '暂时不支持该请求'
                })
