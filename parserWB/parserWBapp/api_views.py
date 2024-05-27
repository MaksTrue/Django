from .models import Post, Product, Tag, Category
from .serializers import PostSerializer, ProductSerializer, TagSerializer, CategorySerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from .permission import ReadOnly, IsAuthor


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthor | ReadOnly | IsAdminUser]
    queryset = Post.objects.prefetch_related('tags')
    serializer_class = PostSerializer


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class TagViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
