#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ApiTest.py
@Contact :   746832476@qq.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/7 下午5:43   luoqingfu   1.0         None
'''

# import lib
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api_man.models import ApiTestResultModel, ApiTestSummaryModel
from django.core.paginator import Paginator, EmptyPage
from api_man.serializers import ApiTestResultSerializer, ApiTestSummarySerializer
from django.core.exceptions import ObjectDoesNotExist


class ApiTestSummary(APIView):

    def get(self, request):
        """
        获取所有测试概要
        :param request:
        :return:
        """
        project_id = request.GET.get('projectId')
        page = int(request.GET.get('page', 1))
        page_size = int(request.GET.get('pageSize', 20))
        # 判断是否有projectId
        if project_id:
            api_test_summarys = ApiTestSummaryModel.objects.filter(project=project_id)
        else:
            api_test_summarys = ApiTestSummaryModel.objects.all()
        paginator = Paginator(api_test_summarys, page_size)
        total_page = paginator.num_pages
        total_num = paginator.count
        try:
            curr_page = paginator.page(page)
            api_test_summary = ApiTestSummarySerializer(curr_page, many=True)
            return Response({
                'code': status.HTTP_200_OK,
                'message': '查询成功',
                'data': api_test_summary.data,
                'page': page,
                'pageSize': page_size,
                'totalPage': total_page,
                'total': total_num

            })
        except EmptyPage:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'message': '该页没有数据哦',
                'page': page,
                'pageSize': page_size,
                'totalPage': total_page,
                'total': total_num
            })

    def post(self, request):
        """
        新增测试结果概要
        :param request:
        :return:
        """
        api_test_summary = ApiTestSummarySerializer(data=request.data, partial=True)
        if api_test_summary.is_valid():
            api_test_summary.save()
            return Response({
                'code': status.HTTP_200_OK,
                'message': '新增成功',
                'data': api_test_summary.data
            })
        else:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'message': '新增失败',
            })


class ApiTestResult(APIView):

    def get(self, request):
        """
        获取对应测试概要下的测试结果
        :param request:
        :return:
        """
        page = int(request.GET.get('page', 1))
        page_size = int(request.GET.get('pageSize', 20))
        summary_id = request.GET.get('summaryId')
        try:
            api_test_result = ApiTestResultModel.objects.filter(summary=summary_id)
            paginator = Paginator(api_test_result, page_size)
            total_page = paginator.num_pages
            curr_page = paginator.page(page)
            total_num = paginator.count
            api_test_results = ApiTestResultSerializer(curr_page, many=True)
            return Response({
                'code': status.HTTP_200_OK,
                'message': '获取成功',
                'data': api_test_results.data,
                'page': page,
                'pageSize': page_size,
                'totalSize': total_page,
                'total': total_num
            })
        except ObjectDoesNotExist:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'message': '对应的summaryId没有结果'
            })

    def post(self, request):
        """
        新建测试结果详情
        :param request:
        :return:
        """
        data = request.data.copy()  # 新建一个副本，reque.data不能修改
        if isinstance(data['test_status'], str):
            if data['test_status'] == 'passed':
                data['test_status'] = 1
            elif data['test_status'] == 'failed':
                data['test_status'] = 2
            else:
                data['test_status'] = 3
        else:
            pass
        api_test_result = ApiTestResultSerializer(data=data, partial=True)
        if api_test_result.is_valid():
            api_test_result.save()
            return Response({
                'code': status.HTTP_200_OK,
                'message': '创建成功',
                'data': api_test_result.data
            })
        else:
            return Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'message': '创建失败'
            })