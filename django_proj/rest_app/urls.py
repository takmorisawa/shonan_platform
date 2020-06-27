from rest_framework import routers
from rest_app.views import ProductViewSet,SeriesViewSet,DeviceViewSet,ReportViewSet,SupportViewSet


router=routers.DefaultRouter()
router.register(r'products',ProductViewSet)
router.register(r'serieses',SeriesViewSet)
router.register(r'devices',DeviceViewSet)
router.register(r'rakutensim/reports',ReportViewSet)
router.register(r'supports',SupportViewSet)
