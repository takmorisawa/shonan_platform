from rest_framework import routers
from rest_app.views import SpotViewSet,PostViewSet,ReportViewSet

router=routers.DefaultRouter()
router.register(r'spots',SpotViewSet)
router.register(r'posts',PostViewSet)
router.register(r'simreports/rakuten',ReportViewSet)
