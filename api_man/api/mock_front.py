#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   mock_front.py    
@Contact :   746832476@qq.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/4/3 下午9:44   luoqingfu   1.0         None
'''

# import lib
from rest_framework.views import APIView
from rest_framework.response import Response

class Chart(APIView):

    def get(self, request):
        list_chart = [20, 40, 78, 10, 30, 48]
        return Response({
            'code': 200,
            'data': list_chart
        })
