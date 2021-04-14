#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   urls.py    
@Contact :   746832476@qq.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/3 上午10:41   luoqingfu   1.0         None
'''

# import lib
from django.urls import path

from api_man.api.Project import ProjectView, Projectdel, Projectedit, ProjectSearch
from api_man.api.Api import ApiView, Apiedit, ApiDel, SearchApi
from api_man.api.BaseUrl import BaseUrlView, BaseUrlDel, BaseUrlEdit
from api_man.api.ApiTest import ApiTestSummary, ApiTestResult
from api_man.api.SendRequest import SendRequest
from api_man.api.mock_front import Chart

urlpatterns = [
    path('project', ProjectView.as_view()),
    path('project/del', Projectdel.as_view()),
    path('project/edit', Projectedit.as_view()),
    path('project/search', ProjectSearch.as_view()),
    path('api', ApiView.as_view()),
    path('api/edit', Apiedit.as_view()),
    path('api/del', ApiDel.as_view()),
    path('baseurl', BaseUrlView.as_view()),
    path('baseurl/del', BaseUrlDel.as_view()),
    path('baseurl/edit', BaseUrlEdit.as_view()),
    path('apitest/summary', ApiTestSummary.as_view()),
    path('apitest/result', ApiTestResult.as_view()),
    path('api/sendRequest', SendRequest.as_view()),
    path('api/dashboard/chart', Chart.as_view()),
    path('api/search', SearchApi.as_view())


]
