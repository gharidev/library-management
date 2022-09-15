from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated

from core.models import Book, CheckOutHistory, Student
from core.permissions import IsAdminOnly
from core.serializers import BookSerializer, CheckOutSerializer, UserSerializer

class ListStudentView(generics.ListAPIView):
    permission_classes = (IsAdminOnly,)
    serializer_class = UserSerializer
    queryset = Student.objects.all()

class CreateStudentView(generics.CreateAPIView):
    permission_classes = (IsAdminOnly,)
    serializer_class = UserSerializer

class UpdateStudentView(generics.UpdateAPIView):
    permission_classes = (IsAdminOnly,)
    serializer_class = UserSerializer
    queryset = Student.objects.all()

class DeleteUserView(generics.DestroyAPIView):
    permission_classes = (IsAdminOnly,)
    queryset = Student.objects.all()

class CreateBookView(generics.CreateAPIView):
    permission_classes = (IsAdminOnly,)
    serializer_class = BookSerializer

class UpdateBookView(generics.UpdateAPIView):
    permission_classes = (IsAdminOnly,)
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class DeleteBookView(generics.DestroyAPIView):
    permission_classes = (IsAdminOnly,)
    queryset = Book.objects.all()

class ListBookView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class CreateCheckOutView(generics.CreateAPIView):
    permission_classes = (IsAdminOnly,)
    serializer_class = CheckOutSerializer

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data", {}), list):
            kwargs["many"] = True

        return super().get_serializer(*args, **kwargs)

class UpdateCheckOutView(generics.UpdateAPIView):
    permission_classes = (IsAdminOnly,)
    serializer_class = CheckOutSerializer
    queryset = CheckOutHistory.objects.all()

class DeleteCheckOutView(generics.DestroyAPIView):
    permission_classes = (IsAdminOnly,)
    queryset = CheckOutHistory.objects.all()

class ListHistoryCheckOutView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CheckOutSerializer

    def get_queryset(self):
        return CheckOutHistory.objects.filter(student=self.request.user)