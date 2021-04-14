#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Project.py    
@Contact :   746832476@qq.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/3 上午10:47   luoqingfu   1.0         None
'''

# import lib
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api_man.models import Projectmodel
from api_man.serializers import ProjectSerializers


class ProjectView(APIView):

    def post(self, request):
        """
        创建一个新的项目
        :param request:
        :return:
        """
        project_serializers = ProjectSerializers(data=request.data)
        if project_serializers.is_valid():
            project_serializers.save()
            return Response({
                'code': status.HTTP_200_OK,
                'message': '添加成功',
                'data': project_serializers.data
            })
        else:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'message': '请求参数错误'
            })

    def get(self, request):
        """
        获取项目列表
        :param request:
        :return:
        """
        try:
            page = int(request.GET.get('page', 1))
            page_size = int(request.GET.get('page_seze', 20))
        except(TypeError, ValueError):
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'message': 'page和pagesize只能是整数'
            })
        project_status = request.GET.get('status', 1)
        projects = Projectmodel.objects.filter(status__contains=project_status)
        paginator = Paginator(projects, page_size)
        total_num = paginator.count
        total = paginator.num_pages
        try:
            curr_page = paginator.page(page)
        except EmptyPage:
            return Response({
                'code': status.HTTP_200_OK,
                'message': '该页没有数据哦',
                'page': page,
                'pageSize': page_size,
                'totalPage': total,
                'total': total_num

            })
        projects = ProjectSerializers(curr_page, many=True)
        return Response({
            'code': status.HTTP_200_OK,
            'message': '获取项目列表成功',
            'data': projects.data,
            'page': page,
            'pageSize': page_size,
            'totalPage': total,
            'total': total_num
        })


class Projectdel(APIView):

    def post(self, request):
        """
        根据项目id删除对应的接口
        :param request:
        :return:
        """
        try:
            pk = request.GET.get('id')
            project = Projectmodel.objects.filter(pk=pk).first()
        except ObjectDoesNotExist:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'message': '此项目不存在'
            })
        if pk:
            data = {'status': 2}
            project_obj = ProjectSerializers(instance=project, data=data, partial=True)
            if project_obj.is_valid():
                project_obj.save()
                return Response({
                    'code': status.HTTP_200_OK,
                    'message': '删除成功'
                })
            else:
                return Response({
                    'code': status.HTTP_400_BAD_REQUEST,
                    'message': '修改失败'
                })
        else:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'message': '请输入项目id'
            })


class Projectedit(APIView):

    def post(self, request):
        """
        修改项目信息
        :param request:
        :return:
        """
        pk = request.GET.get('id')
        try:
            project = Projectmodel.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'message': '该项目不存在'
            })
        project_obj = ProjectSerializers(instance=project, data=request.data, partial=True)  # 可以局部修改
        if project_obj.is_valid():
            project_obj.save()
            return Response({
                'code': status.HTTP_200_OK,
                'message': '修改成功',
                'data': project_obj.data
            })
        else:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'message': '修改失败'
            })


class ProjectSearch(APIView):

    def get(self, request):
        """
        按照 project_name过滤项目
        :param request:
        :return:
        """
        page = int(request.GET.get('page', 1))
        pageSize = int(request.GET.get('pageSize', 20))
        project_name = request.GET.get('projectName')
        try:
            project = Projectmodel.objects.filter(project_name__icontains=project_name, status=1).order_by('id')  # 不区分大小写
            paginator = Paginator(project, pageSize)
            total = paginator.num_pages
            curr_page = paginator.page(page)
            total_num = paginator.count
            project = ProjectSerializers(curr_page, many=True)
            return Response({
                'code': status.HTTP_200_OK,
                'message': '查询成功',
                'data': project.data,
                'page': page,
                'pageSize': pageSize,
                'totalPage': total,
                'total': total_num
            })
        except:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'message': '查询失败'
            })
