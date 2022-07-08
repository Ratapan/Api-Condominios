from django.urls import path
from .views import CondominiumView,ResidentView,HouseView,ResidenceView, CondominosManage

urlpatterns = [
    #lista
    path('condominos/', CondominosManage.as_view(), name='manage_cond'),

    #condominios
    path('condominiums/', CondominiumView.as_view(), name='condominium_list'),
    path('condominiums/<int:id>', CondominiumView.as_view(), name='condominium_list'),
    
    #residentes
    path('residents/', ResidentView.as_view(), name='resident_list'),
    path('residents/<int:id>', ResidentView.as_view(), name='resident_list'),
    
    #casas
    path('houses/', HouseView.as_view(), name='house_list'),
    
    #recidencias
    path('residences/', ResidenceView.as_view(), name='residence_list'),
]