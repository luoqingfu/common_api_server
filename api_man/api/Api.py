#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Api.py    
@Contact :   746832476@qq.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/3 上午10:32   luoqingfu   1.0         None
'''

# import lib
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.paginator import Paginator, EmptyPage
from api_man.models import Apimodel
from api_man.serializers import ApiSerializers
from django.core.exceptions import ObjectDoesNotExist


class ApiView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        """
        新增接口
        :param request:
        :return:
        """
        api_serializer = ApiSerializers(data=request.data)
        if api_serializer.is_valid():
            api_serializer.save()
            return Response({
                'code': status.HTTP_200_OK,
                'message': '添加成功',
                'data': api_serializer.data
            })
        else:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'message': '参数错误'
            })

    def get(self, request):
        """
        获取所有的接口
        根据project筛选接口
        :param request:
        :return:
        """
        if request.GET.get('project'):
            project_id = int(request.GET.get('project'))
            page = int(request.GET.get('page', 1))
            page_size = int(request.GET.get('pageSize', 20))
            # 根据pojectid获取对应id下的接口列表
            api_project_obj = Apimodel.objects.filter(project=project_id, status=1)
            paginator = Paginator(api_project_obj, page_size)
            total_page = paginator.num_pages
            total_num = paginator.count
            try:
                curr_page = paginator.page(page)
                api = ApiSerializers(curr_page, many=True)
                return Response({
                    'code': status.HTTP_200_OK,
                    'message': '获取成功',
                    'data': api.data,
                    'page': page,
                    'pageSize': page_size,
                    'totalPage': total_page,
                    'total': total_num
                })
            except EmptyPage:
                return Response({
                    'code': status.HTTP_200_OK,
                    'message': '该页没有数据哦',
                    'page': page,
                    'pageSize': page_size,
                    'totalPage': total_page,
                    'total': total_num

                })

        else:
            api_obj = Apimodel.objects.filter(status=1).order_by('-create_time')
            page = int(request.GET.get('page', 1))
            page_size = int(request.GET.get('pageSize', 20))
            paginator = Paginator(api_obj, page_size)
            total_page = paginator.num_pages
            total_num = paginator.count
            try:
                curr_page = paginator.page(page)
                api = ApiSerializers(curr_page, many=True)
                return Response({
                    'code': status.HTTP_200_OK,
                    'message': '获取成功',
                    'data': api.data,
                    'page': page,
                    'pageSize': page_size,
                    'totalPage': total_page,
                    'total': total_num
                })
            except EmptyPage:
                return Response({
                    'code': status.HTTP_200_OK,
                    'message': '该页没有数据哦',
                    'page': page,
                    'pageSize': page_size,
                    'totalPage': total_page,
                    'total': total_num

                })


class Apiedit(APIView):

    def post(self, request):
        """
        修改对应的接口
        :return:
        """
        pk = request.GET.get('id')
        try:
            api_obj = Apimodel.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({
                'code': status.HTTP_200_OK,
                'message': '该条接口不存在'
            })
        api = ApiSerializers(instance=api_obj, data=request.data, partial=True)  # 允许部分修改
        if api.is_valid():
            api.save()
            return Response({
                'code': status.HTTP_200_OK,
                'message': '修改成功',
                'data': api.data
            })
        else:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'message': '修改失败'
            })


class ApiDel(APIView):

    def post(self, request):
        """
        修改接口的状态，删除状态status= 2
        :param request:
        :return:
        """
        pk = request.data['id']
        try:
            api_obj = Apimodel.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({
                'code': status.HTTP_200_OK,
                'message': '没有该条接口'
            })
        data = {'status': 2}
        api = ApiSerializers(instance=api_obj, data=data, partial=True)  # 状态修改为2
        if api.is_valid():
            api.save()
            return Response({
                'code': status.HTTP_200_OK,
                'message': '删除成功'
            })
        else:
            return Response({
                'code': status.HTTP_200_OK,
                'message': '删除失败'
            })


class SearchApi(APIView):

    def get(self, request):
        """
       根据url 查询接口
       :param request:
       :return:
       """
        try:
            key = request.GET.get('url')
            api_obj = Apimodel.objects.filter(url__contains=key, status=1).order_by('-create_time')
            page = int(request.GET.get('page', 1))
            page_size = int(request.GET.get('pageSize', 20))
            paginator = Paginator(api_obj, page_size)
            total_num = paginator.count
            curr_page = paginator.page(page)
            api = ApiSerializers(curr_page, many=True)
            return Response({
                'code': status.HTTP_200_OK,
                'message': '获取成功',
                'data': api.data,
                'page': page,
                'pageSize': page_size,
                'total': total_num
            })
        except:
            return Response({
                'code': status.HTTP_200_OK,
                'data': [],
                'message': '没有该条接口'
            })
