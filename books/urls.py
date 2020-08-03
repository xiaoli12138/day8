from django.urls import path
from rest_framework.routers import DefaultRouter
from books import views

urlpatterns = [
    path('books/book/<name>/', views.BookViewSet.as_view({'get': 'findBookByTitle'})),
    path('books/banner/', views.BannerViewSet.as_view({'get': 'findBanners'})),
    path('books/user/', views.UserViewSet.as_view({'get': 'findUsers'})),

]

router = DefaultRouter()  # 括号不要忘了 ，不然执行不了
router.register(r"books/banner",views.BannerViewSet,basename='banner')
router.register(r"books", views.BookViewSet)
router.register(r"books/user", views.UserViewSet, basename='user')


urlpatterns += router.urls

print(router.urls)
