#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   serializers.py    
@Contact :   746832476@qq.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/3 上午11:53   luoqingfu   1.0         None
'''

# import lib
from abc import ABC

from rest_framework import serializers

from api_man.models import Projectmodel, Apimodel, BaseUrlModel, ApiTestSummaryModel, ApiTestResultModel


class ProjectSerializers(serializers.ModelSerializer):
    """
    项目信息序列化
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = Projectmodel
        fields = (
            'id',
            'project_name',
            'version',
            'type',
            'status',
            'base_url',
            'description',
            'create_time'
        )


class ApiSerializers(serializers.ModelSerializer):
    """
    接口信息序列化
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = Apimodel
        fields = (
            'id',
            'api_name',
            'url',
            'api_method',
            'flag',
            'request_data',
            'project',
            'status',
            'create_time'
        )


class BaseUrlSerializers(serializers.ModelSerializer):
    """
    跟域名信息序列化
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = BaseUrlModel
        fields = (
            'id',
            'url_name',
            'base_url',
            'status',
            'project',
            'create_time'
        )


class ApiTestSummarySerializer(serializers.ModelSerializer):
    """
    测试概要结果序列化
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = ApiTestSummaryModel
        fields = (
            'id',
            'success_amount',
            'fail_amount',
            'skip_amount',
            'test_start_time',
            'test_spend_time',
            'test_case_amount',
            'project',
            'create_time'
        )


class ApiTestResultSerializer(serializers.ModelSerializer):
    """
    测试详情序列化
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = ApiTestResultModel
        fields = (
            'id',
            'summary',
            'test_path',
            'test_status',
            'test_description',
            'fail_reason',
            'create_time'

        )

class ApiSendSerializer(serializers.ModelSerializer):
    """"
    测试接口序列化
    """
    class Meta:
        model = Apimodel
        fields = (
            'api_name',
            'url',
            'api_method',
            'flag',
            'request_data',
            'project'
        )