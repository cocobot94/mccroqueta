from rest_framework.routers import DefaultRouter
from apps.api.views.user_view import UserViewSet
from apps.api.views.product_views import (
    ProductViewSet,
    CategoryProductViewSet,
    IndicatorViewSet,
    OrderViewSet,
    OrderDetailViewSet,
)
from apps.api.views.profile_view import ProfileView
from apps.api.views.blog_views import PostViewSet, CommentsViewSet, CategoryPostViewSet
from apps.api.views.link_views import LinkViewSet
from apps.api.views.news_views import NewsViewSet


router = DefaultRouter()
router.register(r"users", viewset=UserViewSet, basename="users")
router.register(r"products", viewset=ProductViewSet, basename="products")
router.register(
    r"category_product", viewset=CategoryProductViewSet, basename="category_product"
)
router.register(r"indicator", viewset=IndicatorViewSet, basename="indicator")
router.register(r"order", viewset=OrderViewSet, basename="order")
router.register(r"order_detail", viewset=OrderDetailViewSet, basename="order_detail")
router.register(r"profile", viewset=ProfileView, basename="profile")
router.register(r"posts", viewset=PostViewSet, basename="posts")
router.register(r"comments", viewset=CommentsViewSet, basename="comments")
router.register(r"category_post", viewset=CategoryPostViewSet, basename="category_post")
router.register(r"links", viewset=LinkViewSet, basename="links")
router.register(r"news", viewset=NewsViewSet, basename="news")

urlpatterns = router.urls
