from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appointments.views import AppointmentViewSet
from patients.views import PatientViewSet
from doctors.views import DoctorViewSet
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth import views as auth_views
from users.views import CustomLoginView

router = DefaultRouter()
router.register(r'appointments', AppointmentViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'doctors', DoctorViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    path('', include('appointments.urls')),  # Frontend clásico de appointments
    path('', include('doctors.urls')),  # Frontend clásico de doctors
    path('', include('patients.urls')),  # Frontend clásico de patients
    path('accounts/', include('django.contrib.auth.urls')),  # login/logout
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]