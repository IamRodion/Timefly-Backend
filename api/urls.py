from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'Worker', views.WorkerViewSet)
router.register(r'TimeEntry', views.TimeEntryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('Worker/employee/<str:employee_id>/', views.WorkerByemployeeID.as_view(), name='get_worker_id_by_employee_id'),
]