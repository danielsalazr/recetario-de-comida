from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    # Renders
    path('', views.Recipes.as_view(), name="recetas"),

    path('recipesFormInfo/', views.recipesFormInfo, name="recipesFormInfo")
    # path('impresiontickets/<int:ordenDeCompra>', views.ImpresionTicketsApi.as_view(), name="impresiontickets"),
    # path('impresiontickets/', views.ImpresionTicketsApi.as_view(), name="impresiontickets"),
    # path('impresionTicketsPdf/', views.impresionTicketsPdf, name="impresionTicketsPdf"),
    #  path('EntradaMercancias/', views.EntradaMercancias.as_view(), name="EntradaMercancias"),
    
    # path('manual/', views.manual, name="manual"),
     
]
