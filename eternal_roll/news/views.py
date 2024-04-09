from django.shortcuts import render
from rest_framework import generics, viewsets
from django.forms import model_to_dict
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated

from rest_framework.views import APIView
from rest_framework.response import Response

from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly

from .models import  *
from .serializers import *

# Create your views here.
# class NewsViewSet(viewsets.ModelViewSet):
#     #queryset = News.objects.all()
#     serializer_class = NewsSerializer

#     def get_queryset(self):
#         pk = self.kwargs.get("pk")
#         if not pk:
#             return News.objects.all()[:2]
#         return News.objects.filter(pk=pk)
    
#     @action(methods=['get'], detail=True)
#     def category(self, request, pk=None):
#         cats = Category.objects.get(pk=pk)
#         return Response({'cats': cats.name})


class NewsAPIList( generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class NewsAPIUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsOwnerOrReadOnly, )

class NewsAPIDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset=News.objects.all()
    serializer_class = NewsSerializer
    permission_classes =(IsAdminOrReadOnly,)

class NewsAPIdetailView(generics.UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class CharListAPI(generics.ListCreateAPIView):
    queryset = CharList.objects.all()
    serializer_class = CharListSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
         user= self.request.user
         serializer.save(owner=user)
        #  user_instance = User.objects.get(id=user_id)

class CharListAPIUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = CharList.objects.all()
    serializer_class = CharListSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly, )


class StatBlockAPI(generics.ListCreateAPIView):
    queryset = StatBlock.objects.all()
    serializer_class = StatBlockSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly, )

class StatBlockAPIUpdate(generics.RetrieveUpdateDestroyAPIView):
        queryset = StatBlock.objects.all()
        serializer_class = StatBlockSerializer
        # permission_classes = (IsOwnerOrReadOnly, )


'''    
class NewsAPIView(APIView):

    def get(self, request):
        w = News.objects.all()
        return Response({'posts':NewsSerializer(w, many=True).data})

    def post(slef, request):
        serializer = NewsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return  Response({'post':serializer.data})
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = News.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = NewsSerializer(data=request.data, instance=instance) # инстанс тот обьект(запись) которую мы будем менять
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})

        try: 
            post= News.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})
        
        post.delete()

        return Response({"post": "delete post " + str(pk)})
    '''