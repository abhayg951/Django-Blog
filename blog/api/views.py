from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "pk"

    def list(self, request, *args, **kwargs):
        print(request.user.pk)
        queryset = self.get_queryset().filter(pk=request.user.pk).get()
        serializer = UserSerializer(queryset, context={'request': request})
        return Response(serializer.data)

#     def list(self, request):
#         # Note the use of `get_queryset()` instead of `self.queryset`
#         print(request.user.pk)
#         queryset = self.get_queryset().filter(pk=request.user.pk)
#         serializer = UserSerializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data)

# class EditUserView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [ permissions.IsAuthenticated]
#     lookup_field = "pk"