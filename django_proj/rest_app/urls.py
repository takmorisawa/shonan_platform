from rest_framework import routers
from rest_app.views import SpotViewSet,PostViewSet

router=routers.DefaultRouter()
router.register(r'spots',SpotViewSet)
router.register(r'posts',PostViewSet)
