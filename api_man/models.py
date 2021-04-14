import uuid

from django.db import models


# Create your models here.


class Projectmodel(models.Model):
    """
    项目列表
    """
    PROJECT_CHOICES = (
        ('1', 'APP'),
        ('2', 'WEB')
    )
    STATUS_CHOICES = (
        ('1', '项目可用'),
        ('2', '项目不可用')
    )
    id = models.AutoField(primary_key=True)
    project_name = models.CharField(verbose_name='项目名称', max_length=30)
    version = models.CharField(verbose_name='项目版本', max_length=30)
    type = models.CharField(choices=PROJECT_CHOICES, max_length=30)
    description = models.CharField(verbose_name='项目描述', max_length=50, default='这个人很懒，不想写描述')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    status = models.CharField(verbose_name='项目状态', max_length=20, choices=STATUS_CHOICES, default=1)  # 1是正常状态，2是删除状态

    def __unicode__(self):
        return self.project_name

    def __str__(self):
        return self.project_name

    class Meta:
        db_table = 'project'
        verbose_name = '项目'
        verbose_name_plural = verbose_name

    objects = models.Manager()


class Apimodel(models.Model):
    """
    接口列表
    """
    API_CHOICES = {
        ('1', '执行'),
        ('2', '不执行')
    }
    STATUS_CHOICES = {
        ('1', '有效'),
        ('2', '已删除')
    }
    id = models.AutoField(primary_key=True)
    api_name = models.CharField(verbose_name='接口名称', max_length=30)
    url = models.CharField(verbose_name='接口路径', max_length=50)
    api_method = models.CharField(verbose_name='请求方法', max_length=10)
    flag = models.CharField(verbose_name='是否执行该接口', choices=API_CHOICES, max_length=10)  # 1执行，2不执行
    request_data = models.CharField(verbose_name='请求参数', max_length=200, null=True, blank=True)
    # project = models.CharField(verbose_name='所属项目', max_length=10)
    project = models.ForeignKey(Projectmodel, on_delete=models.DO_NOTHING, verbose_name='接口所属于的项目')
    status = models.CharField(verbose_name='接口状态', choices=STATUS_CHOICES, max_length=20, default=1)  # 1有效，2已删除
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __unicode__(self):
        return self.api_name

    def __str__(self):
        return self.api_name

    class Meta:
        db_table = 'api'
        verbose_name = '接口'
        verbose_name_plural = verbose_name

    objects = models.Manager()


class BaseUrlModel(models.Model):
    """
    根域名列表
    """
    STATUS_CHOICES = {
        ('1', '有效'),
        ('2', '已删除')
    }
    id = models.AutoField(primary_key=True)
    url_name = models.CharField(verbose_name='根域名名称', max_length=30)
    base_url = models.CharField(verbose_name='根域名', max_length=30)
    status = models.CharField(verbose_name='是否有效', choices=STATUS_CHOICES, max_length=10)
    project = models.ForeignKey(Projectmodel, verbose_name='属于那个项目', on_delete=models.DO_NOTHING)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    def __unicode__(self):
        return self.url_name

    def __str__(self):
        return self.url_name

    class Meta:
        db_table = 'base_url'
        verbose_name = '根域名'
        verbose_name_plural = verbose_name

    objects = models.Manager()


class ApiTestSummaryModel(models.Model):
    """
    测试结果概要
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=True)
    success_amount = models.IntegerField(verbose_name='成功数量')
    fail_amount = models.IntegerField(verbose_name='错误数量')
    skip_amount = models.IntegerField(verbose_name='跳过数量')
    test_start_time = models.CharField(verbose_name='测试开始的时间', max_length=255)
    test_spend_time = models.CharField(verbose_name='测试花费的时间', max_length=255)
    test_case_amount = models.IntegerField(verbose_name='测试用例数量')
    project = models.ForeignKey(Projectmodel, on_delete=models.DO_NOTHING, verbose_name='所属的项目')
    base_url = models.ForeignKey(BaseUrlModel, on_delete=models.DO_NOTHING, verbose_name='对应的根域名')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        db_table = 'api_test_summary'
        verbose_name = '测试结果概要'
        verbose_name_plural = verbose_name

    objects = models.Manager()


class ApiTestResultModel(models.Model):
    """
    测试详细结果
    """
    TEST_STATUS_CHOICES = {
        ('1', '成功'),
        ('2', '失败'),
        ('3', '跳过')
    }
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=True)
    summary = models.ForeignKey(ApiTestSummaryModel, on_delete=models.DO_NOTHING)
    test_path = models.CharField(verbose_name='测试的路径', max_length=255)
    test_status = models.CharField(verbose_name='测试结果', choices=TEST_STATUS_CHOICES, max_length=255)
    test_description = models.CharField(verbose_name='测试描述', max_length=255)
    fail_reason = models.CharField(verbose_name='错误原因', max_length=1000, null=True, blank=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        db_table = 'api_test_result'
        verbose_name = '详细测试结果'
        verbose_name_plural = verbose_name

    objects = models.Manager()
