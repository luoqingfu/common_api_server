#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   BaseUrl.py
@Contact :   746832476@qq.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/5 下午6:51   luoqingfu   1.0         None
'''

# import lib
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api_man.serializers import BaseUrlSerializers
from api_man.models import BaseUrlModel
from django.core.exceptions import ObjectDoesNotExist


class BaseUrlView(APIView):

    def get(self, request):
        """
        获取所有根域名
        :param request:
        :return:
        """
        base_urls_obj = BaseUrlModel.objects.all()
        if base_urls_obj:
            base_urls = BaseUrlSerializers(base_urls_obj, many=True)
            return Response({
                'code': status.HTTP_200_OK,
                'message': '获取成功',
                'data': base_urls.data
            })
        else:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'message': '获取失败'
            })

    def post(self, request):
        """
        新增根域名
        :param request:
        :return:
        """
        base_url = BaseUrlSerializers(data=request.data)
        if base_url.is_valid():
            base_url.save()
            return Response({
                'code': status.HTTP_200_OK,
                'message': '创建成功',
                'data': base_url.data
            })
        else:
            return Response({
                'code': status.HTTP_200_OK,
                'message': '创建失败'
            })


class BaseUrlDel(APIView):

    def post(self, request):
        """
        删除根域名
        :return:
        """
        pk = request.GET.get('id')
        try:
            base_url = BaseUrlModel.objects.get(pk=pk)
            base_url_del = BaseUrlSerializers(instance=base_url, data={'status': 2}, partial=True)
            if base_url_del.is_valid():
                base_url_del.save()
                return Response({
                    'code': status.HTTP_200_OK,
                    'message': '删除成功'
                })
        except ObjectDoesNotExist:
            return Response({
                'code': status.HTTP_200_OK,
                'message': '该条根域名不存在'
            })


class BaseUrlEdit(APIView):

    def post(self, request):
        """
        修改根域名
        :param request:
        :return:
        """
        pk = request.GET.get('id')
        try:
            base_url_obj = BaseUrlModel.objects.get(pk=pk)
            base_url = BaseUrlSerializers(instance=base_url_obj, data=request.data, partial=True)  # 支持部分修改
            if base_url.is_valid():
                base_url.save()
                return Response({
                    'code': status.HTTP_200_OK,
                    'message': '修改成功',
                    'data': base_url.data
                })
            else:
                return Response({
                    'code': status.HTTP_400_BAD_REQUEST,
                    'message': '修改失败'
                })
        except ObjectDoesNotExist:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'message': '该条根域名不存在'
            })
