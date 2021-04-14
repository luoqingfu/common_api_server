from django.contrib import admin

# Register your models here.
from api_man.models import Projectmodel, Apimodel, BaseUrlModel, ApiTestResultModel, ApiTestSummaryModel

admin.site.register(Projectmodel)
admin.site.register(Apimodel)
admin.site.register(BaseUrlModel)
admin.site.register(ApiTestResultModel)
admin.site.register(ApiTestSummaryModel)
