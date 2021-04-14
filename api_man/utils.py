#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   utils.py    
@Contact :   746832476@qq.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/2 下午9:04   luoqingfu   1.0         None
'''

# import lib
from rest_framework import status


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'code': status.HTTP_200_OK,
        'message': 'success',
        'data': {
            'uid': user.id,
            'username': user.username,
            'token': token
        }

    }

def jwt_response_payload_error_handler(serializer, request = None):
    return {
        'code': status.HTTP_400_BAD_REQUEST,
        'message': '用户名或者密码错误',
        'data': serializer.errors

    }
