# Framework
from django.shortcuts import redirect, HttpResponse, render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q, Max, QuerySet
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.core import serializers
from django.db import models, connections, transaction
from django.forms.models import model_to_dict

# import django_excel as excel

# Views
# from MySQL.views import (
#     deleteBoxComplete,
#     deleteReference,
#     getAllBoxInPicking,
#     getBoxWeight,
#     getReferencesInBoxMonitor,
#     TestMysqlConnection,
# )


# from SAP.views import (
#     getInfoReferenceSAPCodebarsArray,
#     getInfoReferenceSAPitemCode,
#     getItemsSaleOrder,
#     getItemsSaleQuotation,
#     getListInvoicesOfSaleOrder,
#     getTitleSaleOrder,
#     getTitleSaleQuotation,
#     # getSaleOrderCollection,
#     getSaleOrderCollectionId,
#     getSaleOrderCollectionIdByName,
#     getCollectionIDByName,
#     getSaleOrderOrQuotationInformation,
# )

# # Models
# from picking.models import Company
# from login.models import Permisos
from django.contrib.auth.models import User
# from picking.models import (
#     Box,
#     BoxItem,
#     CollectionIndicator,
#     Dimension,
#     Picking,
#     Status,
#     WarehouseCustomer,
#     StatusHistory,
#     DuplicatedPicking,
# )

# from picking.packinglist.filterCharacters import filterCharacters
# # Crud
# from picking.consume.crud import (
#     addBox,
#     addItemBox,
#     addPicking,
# )

# # Middleware
# from picking.consume.middelware import (
#     getBalancesItemsBySaleOrder,
#     getFormulaIndicatorPickingCollection,
#     getFormulaIndicatorPickingSaleOrder,
#     getPorcDespachado,
#     getPorcDespachadoByCollection,
# )

# Django Rest Framework
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import FileUploadParser

# Validators
# from picking.consume.validations import existInOrder, supMontoInOrder

from .models import (
    Recipe,
    Category,
    CombinedRecipes,
    ImageRecipe,
)

# Python
from datetime import datetime
from time import gmtime, strftime
import json
import time
# import pytz
from rich.console import Console
console = Console()

# Utils
# from utils.datetimeConversionTimezone import colombiaTimezone

@api_view(('GET', 'POST',))
def recipesFormInfo(request):

    categories = Category.objects.all().values()

    context = {
        "categories":categories,
    }

    return Response(context)


class Recipes(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """

        # usernames = [user.username for user in User.objects.all()]

        if 'recipe' in request.query_params:

            recipes = Recipe.objects.get(id=request.query_params['recipe'])
            images = ImageRecipe.objects.filter(recipe=recipes).values()
            recipe_dict = Recipe.objects.filter(id=request.query_params['recipe']).values().first()
            categorias = recipes.categories.all().values()
            relacionados = recipes.categories.all().values()

            context = { 
                "recipe": recipe_dict, 
                "images": images, 
                "categorias": categorias
            }

            return Response(context)

            
        recipes = Recipe.objects.all()
        recipes_dict =  Recipe.objects.all().values() #get(id=2)
        # images = ImageRecipe.objects.filter(recipe=recipes).values()
        # recipe_dict = Recipe.objects.filter(id=1).values()
        # categorias = recipes.categories.all().values()
        # relacionados = recipes.categories.all().values()


        context = []
        for i, data in enumerate(recipes):
            json = {}
            json['recipe'] = recipes_dict[i]#model_to_dict(data)
            json['images'] = ImageRecipe.objects.filter(recipe=data).values().first() #.values()
            json['categorias'] = data.categories.all().values()
            json['recipe']['author'] = f"{data.author.first_name} {data.author.last_name}"
            context.append(json)




        
        console.log(context)

        # queryValidateExistCopy = f"""
        #     SELECT 
        #         idDestino_id,
        #         idOrigen_id,
        #         T1.company_id as companyOrigen,
        #         T2.company_id as companyDestino
        #     FROM picking_duplicatedpicking T0
        #     INNER JOIN picking_picking T1 ON T1.idPicking = T0.idOrigen_id 
        #     INNER JOIN picking_picking T2 ON T2.idPicking = T0.idDestino_id
        #     where (T0.idOrigen_id = {picking.idPicking} or T0.idDestino_id =  {picking.idPicking})  and T1.company_id = {request.data['originDatabaseSelected']} and T2.company_id = {request.data['destinationDatabaseSelected']};
        # """
            
        # with connections['default'].cursor() as cursor:
        #     cursor.execute(queryValidateExistCopy)
        #     columns = [col[0] for col in cursor.description]
        #     result = [dict(zip(columns, row)) for row in cursor.fetchall()]
            # result = list(cursor.fetchall())

        # queryset = QuerySet(model=passTable, using='default')
        # queryset._result_cache = list(result)

        # return Response({"info": "Reinfo"})
        return Response(context)

    def post(self, request, *args, **kwargs):
        pass
        
        console.log(request.data)

        imagenes = request.FILES.getlist('imagen')
        console.log(imagenes)

        receta = Recipe(
            name = request.data.get('name'),
            ingredients = request.data.get('ingredients'),
            description = request.data.get('description'),
            author = User.objects.get(id=1)
            # categories = request.data.get('name
        )
        receta.save()

        for i in request.data.getlist('categories'):
            # console.log(i)
            receta.categories.add(Category.objects.get(name=i))

        for i in imagenes:
            ImageRecipe.objects.create(image=i, recipe=receta)

        return Response({"res" : "Si mi papa"})

# class passTable(models.Model):
#     pass

# # from rich.console import Console
# # console = Console()

# @login_required
# def picking(request):

#     database = request.session['databaseSAP']
#     # console.log(database)
#     company = Company.objects.get(name=database)

#     # user = 
#     if database != "":
#         saldos = ""
#         saleOrder = ""
#         getItems_OrderPV = ""
#         picking = None
#         infoCompleteItem = []
#         dimension = Dimension.objects.all()
#         warehouses = ""
#         # Consultando información de Ordenes de Venta
        
#         orderPVtemp = request.GET.get("OrderPV")
#         """ Verficar si la consulta es a pedido u orden de venta"""
#         orderOrQuotation = request.GET.get("selection")

#         saleOrderCollections = [
#                 'SS22'
#                 'VACATION 2021',
#                 'null',
#                 'GOOP',
#                 'CELIA',
#                 'BARÚ LATAM',
#                 'AURELIANA',
#                 'SOLEDAD',
#                 'PREFALL 2022 SWIM',
#                 'MATCHES',
#                 'PREFALL 2022 RTW',
#                 'PEDIDOS ESPECIALES',
#                 'HOLIDAY HOME ENTERTAINING',
#                 'FALL WINTER 2021 RTW',
#                 'FALL WINTER 2022',
#                 'RESORT SWIM 2023',
#         ]

#         saleOrderCollectionsId = [
#             '009',
#             '014',
#             'null',
#             '006',
#             '003',
#             '002',
#             '012',
#             '004',
#             '020',
#             '021',
#             '019',
#             '011',
#             '021',
#             '020',
#             '005',
#             '001',
#             '024',
#             '025',
#         ]

#         if orderPVtemp != None:
            
#             """Verificar si existe la colexion en Orden de venta"""
#             # collection = getSaleOrderCollection(database, orderPVtemp, orderOrQuotation)
#             # collectionID = getSaleOrderCollectionId(database, orderPVtemp, orderOrQuotation)

#             # console.log(getSaleOrderCollectionId)

#             # # console.log(collection)
#             # console.log(collectionID)


#             """ Se aniade el siguiente condicional debido a que python no posee valor null, 
#                 con esto convertimos None un null para las busquedas sin colecciones
#             """
#             # if collection == None or collectionID == None:
#             # if collectionID == None:
#             #     collection = 'null'

#             # verify = any(collection == v for v in saleOrderCollections)
#             # verifyId = any(collectionID == v for v in saleOrderCollectionsId)
#             # console.log(verifyId)
#             #print(verify)
#             #if verify == True:

#             """ Obtenemos la informacion del pedido verificando si es orden u oferta de venta """
#             saleOrder = getTitleSaleOrder(orderPVtemp, database, orderOrQuotation)

#             # Esta es la nueva modificacion para obtener el picking por coleccion
#             collectionID = saleOrder[0]['collectionId']
            
#             if collectionID == None:
#                 collection = 'null'
            
#             verifyId = any(collectionID == v for v in saleOrderCollectionsId)
#             console.log(verifyId)

#             if orderOrQuotation == "order":     
#                 getItems_OrderPV = getItemsSaleOrder(orderPVtemp, database)
#             else: # "Quotation"
#                 getItems_OrderPV = getItemsSaleQuotation(orderPVtemp, database)

#             #print(saleOrder)
#             #getItems_OrderPV = getItemsSaleOrder(orderPVtemp, database)
#             warehouses = WarehouseCustomer.objects.filter(customer=saleOrder[0]['CardCode'])
            
#             for item in getItems_OrderPV:
#                 barcode = getInfoReferenceSAPitemCode(
#                     item['ItemCode'], database, orderPVtemp, orderOrQuotation
#                 )
#                 infoCompleteItem.append({
#                     'ItemCode': item['ItemCode'],
#                     'Description': item['Description'],
#                     'Quantity': item['Quantity'],
#                     'CodeBars': barcode['barcode']
#                 })
#         try:
#             picking = Picking.objects.filter(
#                 Q(
#                     saleOrder=orderPVtemp,
#                     company=company,
#                     # collection = collection
#                     collectionId = collectionID
#                 )
#             ).order_by('-idPicking')
#             #print(picking)
#         except:
#             picking = ""


#         #print(orderPVtemp)
#         """ porcDespachado = [
#             {'porcentaje': int(getPorcDespachadoByCollection('009', 'SS22', database)), 'indicator':str(getFormulaIndicatorPickingCollection('009', 'SS22', database))+' - SS22'},
#             {'porcentaje': int(getPorcDespachadoByCollection('020', 'PREFALL 2022 SWIM', database)), 'indicator':str(getFormulaIndicatorPickingCollection('020', 'PREFALL 2022 SWIM', database))+' - PREFALL 2022 SWIM'},
#             {'porcentaje': int(getPorcDespachadoByCollection('019', 'PREFALL 2022 RTW', database)), 'indicator':str(getFormulaIndicatorPickingCollection('019', 'PREFALL 2022 RTW', database))+' - PREFALL 2022 RTW'},
#             {'porcentaje': int(getPorcDespachado(orderPVtemp, database)), 'indicator': getFormulaIndicatorPickingSaleOrder(orderPVtemp, database)}
#         ] """

#         # Aqui se toma la cantida de elementos despachados
#         if orderPVtemp != None:
#             porcDespachado = [{'porcentaje': str(int(getPorcDespachado(orderPVtemp, database))) + "% Despacho PV # " + orderPVtemp, 'indicator': getFormulaIndicatorPickingSaleOrder(orderPVtemp, database)}]
#         else:
#             porcDespachado = [{'porcentaje': str(int(getPorcDespachado(orderPVtemp, database))) + "% Despacho PV # ", 'indicator': getFormulaIndicatorPickingSaleOrder(orderPVtemp, database)}]

#         collections = CollectionIndicator.objects.all().order_by('-date_created')
        
#         # console.log(collections.values())
        
#         for indicator in collections:
#             porcDespachado.append(
#                 {'porcentaje': str(int(getPorcDespachadoByCollection(indicator.code, indicator.name, database))) + "% Despachado", 'indicator':str(getFormulaIndicatorPickingCollection(indicator.code, indicator.name, database))+' - '+indicator.name}
#             )

#         infoUser = {'user': request.user.first_name + " " +
#                     request.user.last_name, 'email': request.user.email}

#         companies = Company.objects.all()


#         context = {
#             'pickings': picking,
#             'dateOrders': saleOrder,
#             'dimensions': dimension,
#             'warehouses': warehouses,
#             'itemsSaleOrder': saldos,
#             'infoUsers': infoUser,
#             'porcDespachado': porcDespachado,
#             'company': company.name,
#             'orderOrQuotation': orderOrQuotation,
#             'credenciales': {
#                 'permisos': request.session['permisos'],
#                 'area': request.session['area'],
#             },
#             "database" : database,
#             "companies": companies,
#         }

#         console.log(context['dateOrders'])

#         #print(context)

#         return render(request, 'picking.html', context)
#     else:
#         return redirect('/logout/')


# def manual(request):
#     database = request.session['databaseSAP']
#     company = Company.objects.get(name=database)
#     infoUser = {'user': request.user.first_name + " " +
#                 request.user.last_name, 'email': request.user.email}
#     context = {
#         'infoUsers': infoUser,
#         'company': company.name
#     }
#     return render(request, 'manual.html', context)


# """ SALEORDER """

# # API que permite listar la informacion del pedido de venta (cabecera)


# @login_required
# def saleOrderInfoList(request, id, orderOrQuotation):
#     database = request.session['databaseSAP']
#     saleOrder = getTitleSaleOrder(id, database, orderOrQuotation)
#     response = list(saleOrder)

#     return JsonResponse({'InfoOrdenDeVenta': response})


# # @login_required
# def invoicesOfSaleOrder(request, docNumSaleOrder):
#     database = request.session['databaseSAP']
#     # database = "SBOJOZFLLC"

#     company = Company.objects.get(name=database)

#     orderOrQuotation = request.GET.get('orderOrQuotation')
#     # console.log(request.GET.get('orderOrQuotation'))

#     # console.log(company.id)
    
#     listInvoices = getListInvoicesOfSaleOrder(docNumSaleOrder, int(company.id), orderOrQuotation, database)
#     if listInvoices != None:
#         response = list(listInvoices)
#     else:
#         response = []

#     # console.log(listInvoices)

#     response.append('STICKER 15x10')
#     return JsonResponse({'Invoices': response})


# """ PICKING """


# @login_required
# def createPicking(request):
#     database = request.session['databaseSAP']
#     company = Company.objects.get(name=database)
#     if database != "":

#         console.log(request.POST)

#         # now = colombiaTimezone(datetime.now())
#         now = timezone.now()
#         saleOrder = request.POST.get("pk-OrdenPV")
#         customerCode = request.POST.get("customerCode")
#         customerName = request.POST.get("customerName")
#         collection = request.POST.get("collection")
#         collectionId = request.POST.get("collectionId")
#         pickingStatus = request.POST.get('pickingStatus')
#         console.log(pickingStatus)
#         pickingComment = request.POST.get('pickingComment')
#         orderOrQuotation = request.POST.get('orderOrQuotation')
#         userCreated = request.user.first_name + " " + request.user.last_name
#         userModified = request.user.first_name + " " + request.user.last_name

#         console.log(collectionId)

#         newPicking = {
#             'saleOrder': saleOrder,
#             'customerCode': customerCode,
#             'customerName': customerName,
#             'collection': collection,
#             'collectionId' : collectionId,
#             'comment': pickingComment,
#             'userCreated': userCreated,
#             'dateCreated': now,
#             'userModified': userModified,
#             'dateModified': now,
#             'status': Status.objects.get(idStatus=pickingStatus),
#             'company': company
#         }


#         addPicking(newPicking)
#         ultPick = Picking.objects.latest('idPicking')

#         mensaje = "Creado Exitosamente con el id "+str(ultPick.idPicking)

#         messages.success(request, mensaje)
#         return redirect(f"/picking/?selection={orderOrQuotation}&OrderPV={saleOrder}")
#     else:
#         return redirect('/logout/')


# @login_required
# def updateStatusPicking(request):
#     # showtime = colombiaTimezone(datetime.now()) 
#     showtime = timezone.now()

#     ordenPV = request.GET.get("OrderPV-modStatusPick-name")
#     newStatus = request.GET.get("select_status_picking")
#     idPicking = request.GET.get("idPickig-update-name")
#     orderOrQuotation = request.GET.get("orderOrQuotation")

#     console.log(newStatus)

#     if idPicking != "":
#         picking = Picking.objects.filter(idPicking=idPicking)
#         lastpickingStatus = picking[0].status

        
#         picking.update(
#             status=newStatus,
#             userModified=request.user.first_name + " " + request.user.last_name,
#             dateModified=showtime
#         )

#         numberLastpickingStatus = Status.objects.get(name=lastpickingStatus).idStatus
#         console.log(lastpickingStatus)

#         if lastpickingStatus.idStatus != newStatus:

#             status_history = StatusHistory(
#                 status = Status.objects.get(idStatus= newStatus),
#                 picking= Picking.objects.get(idPicking=idPicking),
#                 lastStatus=numberLastpickingStatus,
#             )

#             status_history.save()




#         messages.success(request, "El Picking ha sido modificado con exito!")
#         return redirect(f"/picking/?selection={orderOrQuotation}&OrderPV={ordenPV}")
#     else:
#         messages.success(
#             request, "Error al modificar Picking, primero debe seleccionarlo!")
#         return redirect(f"/picking/?selection={orderOrQuotation}&OrderPV={ordenPV}")


# """ BOX """

# # API que permite listar la cantidad de cajas que tiene un despacho


# @login_required
# def listBoxesInPicking(request, id):
#     boxes = getAllBoxInPicking(id)
#     return JsonResponse({'boxes': boxes})


# @login_required
# def addBoxInPicking(request):

#     showtime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
#     showtime = timezone.now()
#     datos = json.loads(request.body)
#     idPicking = datos['idPicking']
#     saleOrder = datos['OrdenDeVenta']
#     idDimension = datos['Dimension']
#     idWarehouse = datos['warehouse']
#     userCreated = request.user.first_name + " " + request.user.last_name
#     dateCreated = showtime
#     userModified = request.user.first_name + " " + request.user.last_name
#     dateModified = showtime
#     grossWeight = 0.0
#     netWeight = 0.0
#     comment = ""
#     dimension = Dimension.objects.get(idDimension=int(idDimension))
#     picking = Picking.objects.get(idPicking=int(idPicking))

#     try:
#         barcode = int(Box.objects.latest('codebars').codebars) + 1
#     except:
#         barcode = "80000000001"

#     if idWarehouse == "":
#         warehouse = None
#         addBox(barcode, comment, userCreated, dateCreated, userModified, dateModified,
#                float(grossWeight), float(netWeight), dimension, picking, warehouse)
#     else:
#         warehouse = WarehouseCustomer.objects.get(
#             idWarehouseCustomer=idWarehouse)
#         addBox(barcode, comment, userCreated, dateCreated, userModified, dateModified,
#                float(grossWeight), float(netWeight), dimension, picking, warehouse)

#     return HttpResponse(str(datos))


# @login_required
# def updateBox(request):

#     datos = json.loads(request.body)
#     # now = strftime("%Y-%m-%d %H:%M:%S", gmtime())
#     now = timezone.now()
#     idBox = datos['idCaja']
#     saleOrder = datos['OrdenDeVenta']
#     comment = datos['comentario']
#     userModified = request.user.first_name + " " + request.user.last_name
#     dateModified = now
#     #dateModified = colombiaTimezone(datetime.now())
#     grossWeight = datos['grossWeight']
#     dimension = datos['dimension']
#     warehouse = datos['warehouse']

#     if dimension != "" and grossWeight != "" and warehouse != "":

#         newDimension = Dimension.objects.get(idDimension=dimension)
#         newWarehouse = WarehouseCustomer.objects.get(
#             idWarehouseCustomer=warehouse)
#         boxWeight = getBoxWeight(idBox)
#         netWeight = float(grossWeight)-float(boxWeight)
#         Box.objects.filter(idBox=idBox).update(
#             comment=comment,
#             userModified=userModified,
#             dateModified=dateModified,
#             grossWeight=grossWeight,
#             netWeight=netWeight,
#             idDimension=newDimension,
#             idWarehouseCustomer=newWarehouse)
#     elif dimension != "" and grossWeight != "":

#         newDimension = Dimension.objects.get(idDimension=dimension)
#         boxWeight = getBoxWeight(idBox)
#         netWeight = float(grossWeight)-float(boxWeight)
#         Box.objects.filter(idBox=idBox).update(
#             comment=comment,
#             userModified=userModified,
#             dateModified=dateModified,
#             grossWeight=grossWeight,
#             netWeight=netWeight,
#             idDimension=newDimension)
#     elif dimension != "" and warehouse != "":

#         newDimension = Dimension.objects.get(idDimension=dimension)
#         newWarehouse = WarehouseCustomer.objects.get(
#             idWarehouseCustomer=warehouse)
#         Box.objects.filter(idBox=idBox).update(
#             comment=comment,
#             userModified=userModified,
#             dateModified=dateModified,
#             idDimension=newDimension,
#             idWarehouseCustomer=newWarehouse)
#     elif grossWeight != "" and warehouse != "":

#         newWarehouse = WarehouseCustomer.objects.get(
#             idWarehouseCustomer=warehouse)
#         boxWeight = getBoxWeight(idBox)
#         netWeight = float(grossWeight)-float(boxWeight)
#         Box.objects.filter(idBox=idBox).update(
#             comment=comment,
#             userModified=userModified,
#             dateModified=dateModified,
#             grossWeight=grossWeight,
#             netWeight=netWeight,
#             idWarehouseCustomer=newWarehouse)
#     elif dimension != "":

#         newDimension = Dimension.objects.get(idDimension=dimension)

#         Box.objects.filter(idBox=idBox).update(
#             comment=comment,
#             userModified=userModified,
#             dateModified=dateModified,
#             idDimension=newDimension)

#     elif grossWeight != "":

#         boxWeight = getBoxWeight(idBox)
#         netWeight = float(grossWeight)-float(boxWeight)
#         Box.objects.filter(idBox=idBox).update(
#             comment=comment,
#             userModified=userModified,
#             dateModified=dateModified,
#             grossWeight=grossWeight,
#             netWeight=netWeight)
#     elif warehouse != "":

#         newWarehouse = WarehouseCustomer.objects.get(
#             idWarehouseCustomer=warehouse)
#         Box.objects.filter(idBox=idBox).update(
#             comment=comment,
#             userModified=userModified,
#             dateModified=dateModified,
#             idWarehouseCustomer=newWarehouse)
#     else:

#         Box.objects.filter(idBox=idBox).update(
#             comment=comment,
#             userModified=userModified,
#             dateModified=dateModified)

#     return HttpResponse(str(datos))


# @login_required
# def deleteBox(request):

#     idBox = request.GET.get("idBox")
#     deleteBoxComplete(idBox)

#     mensaje = "Ha sido Eliminada Correctamente"
#     json = {
#         'mensaje': mensaje
#     }

#     return JsonResponse(json)


# """ REFERENCE """


# def listReferencesInBoxQR(request, numBox):
#     box = Box.objects.get(codebars=numBox)
#     boxItem = BoxItem.objects.filter(idBox=box.idBox)
#     noBox = [{'noBox': numBox}]
#     context = {
#         'references': boxItem,

#         'nomBoxes': noBox
#     }
#     return render(request, 'listReferencesInBox.html', context)

# # listReferencias -> referencesListInBox()
# # API que permite listar la cantidad de referencias que tiene una caja


# @login_required
# def listReferencesInBox(request, id):

#     references = getReferencesInBoxMonitor(id)
#     response = ""
#     if (response != None):
#         response = list(references)
#     else:
#         response = []
#         response = list(response)
#     return JsonResponse({'references': response})

# # API que permita listar las referencias con sus saldos


# @login_required
# def listReferencesBalances(request, id, orderOrQuotation):
#     database = request.session['databaseSAP']
#     #orderPv = SaleOrder.objects.get(docNum=id)
#     #idSaleOrderPV = orderPv.idSaleorder
#     saldos = getBalancesItemsBySaleOrder(database, str(id), orderOrQuotation)
#     response = list(saldos)
#     return JsonResponse({'saldosReferences': response})


# @login_required
# def addReferenceInBox(request):
#     database = request.session['databaseSAP']
#     if database != "":
#         mensaje = ""
#         #now = strftime("%Y-%m-%d %H:%M:%S", gmtime())
#         # nowC = colombiaTimezone(datetime.now())
#         nowC = timezone.now()
        
#         datos = json.loads(request.body)
#         #print(datos)
#         pattern = datos['codebar']  # se puede recibir un codebar o un itemCode
#         qantity = datos['quantity']
#         idBox_temp = datos['idBox']
#         saleOrder = datos['OrdenDeVenta']
#         orderOrQuotation = datos['orderOrQuotation']

#         #print(orderOrQuotation)
#         userCreated_temp = request.user.first_name + " " + request.user.last_name
#         # dateCreated_temp = now
#         userModified_temp = request.user.first_name + " " + request.user.last_name
#         # dateModified_temp = now
#         pattern = pattern.strip()
#         # Consultamos la informacion del item en SAP
#         if pattern != "":
#             if idBox_temp != "":
#                 referenceInfo = ""

#                 # Se valida si es un codebars
#                 if pattern[0] == '7':
#                     # Se valida su existencia
#                     referenceInfo = getInfoReferenceSAPCodebarsArray(
#                         database,
#                         saleOrder,
#                         pattern,
#                         orderOrQuotation,
#                     )
#                     #print(referenceInfo)
#                     try:
#                         referenceInfo = referenceInfo[0]
#                     except:
#                         print("")

#                 # Se valida si es un itemCode
#                 else:
#                     # Se valida su existencia
#                     referenceInfo = getInfoReferenceSAPitemCode(
#                         pattern, database, saleOrder, orderOrQuotation)
#                     #print(referenceInfo)

#                 if referenceInfo != None:
#                     codigoSAP = referenceInfo['itemCode']
#                     codebars = referenceInfo['barcode']
#                     itemName = referenceInfo['itemName']
#                     price = referenceInfo['price']
#                     codigoSAP_split = codigoSAP.split("_")
#                     referencia = codigoSAP_split[0]
#                     size = codigoSAP_split[1]
#                     color = codigoSAP_split[2]

#                     #si la caja no existe enviar error
#                     try: 
#                         idBox_ins = Box.objects.get(idBox=idBox_temp)
#                         console.log(idBox_ins)
#                     except  ObjectDoesNotExist: 
#                         console.log("se ejecuto el error")
#                         return JsonResponse({"Error":"no existe caja, seleccione una caja valida."})



#                     if qantity == '':
#                         qantity = 1
#                     userCreated = userCreated_temp
#                     #dateCreated = dateCreated_temp
#                     userModified = userModified_temp
#                     #dateModified = dateModified_temp
#                     idBox = idBox_ins

#                     existItem = existInOrder(
#                         database,
#                         saleOrder,
#                         codebars,
#                         codigoSAP,
#                         orderOrQuotation
#                     )
#                     #print(f"Existe: {existItem}")
#                     if existItem == True:
#                         superaMonto = supMontoInOrder(
#                             database,
#                             qantity,
#                             saleOrder,
#                             codebars,
#                             codigoSAP,
#                         )

#                         if superaMonto == False:
#                             if codebars == None:
#                                 codebars = ""

#                         #     addItems = {
#                         #     'qantity': qantity,
#                         #     'userCreated': userCreated,
#                         #     'dateCreated': nowC,
#                         #     'userModified': userModified,
#                         #     'dateModified': nowC,
#                         #     'idBox': idBox,
#                         #     'codigoSAP': codigoSAP,
#                         #     'referencia': referencia,
#                         #     'color': color,
#                         #     'size': size,
#                         #     'itemName': itemName,
#                         #     'codebars': codebars,
#                         #     'price': price,
#                         # }

#                             # addItemBox(addItems)

#                             console.log(userModified)
#                             addItemBox(
#                                 qantity,
#                                 userCreated,
#                                 # dateCreated,
#                                 nowC,
#                                 userModified,
#                                 # dateModified,
#                                 nowC,
#                                 idBox,
#                                 codigoSAP,
#                                 referencia,
#                                 color,
#                                 size,
#                                 itemName,
#                                 codebars,
#                                 price
#                             )

#                         else:
#                             #print("La cantidad que intenta adicionar, supera a la solicitada en el pedido de venta")
#                             mensaje = "La cantidad que intenta adicionar, supera a la solicitada en el pedido de venta"
#                     else:
#                         #print("El item que intenta adicionar a la caja no se encuentra en la orden de venta")
#                         mensaje = "El item que intenta adicionar a la caja no se encuentra en la orden de venta"
#                 else:
#                     #print("El item que intenta adicionar a la caja no se encuentra en registrado en SAP")
#                     mensaje = "El item que intenta adicionar a la caja no se encuentra en registrado en SAP"
#             else:
#                 #print("Olvidaste seleccionar la caja")
#                 mensaje = "Olvidaste seleccionar la caja"
#         else:
#             #print("Ingrese un codigo de barras o una referencia para continuar")
#             mensaje = "Ingrese un codigo de barras o una referencia para continuar"

#         return HttpResponse(str(mensaje))
#     else:
#         return redirect('/logout/')


# @login_required
# def deleteReferenceInBox(request):
#     itemCode = request.GET.get("itemCode")
#     saleOrder = request.GET.get("saleOrder")
#     picking = request.GET.get("picking")
#     idBox = request.GET.get("box")
#     deleteReference(idBox, itemCode)
#     mensaje = "Ha sido Eliminada Correctamente"
#     json = {
#         'mensaje': mensaje
#     }

#     return JsonResponse(json)


# def testMysqlConnector(request):
#     mess = TestMysqlConnection()
#     # mess = list(mess)
#     # serialized_data = serializers.serialize('json', mess)
#     json_response = JsonResponse(mess, safe=False)

#     # return HttpResponse(mess)
#     return json_response

# def testOrm(request):

#     mess = list(BoxItem.objects.all()[:5])
#     serialized_data = serializers.serialize('json', mess)
#     # timeout = 5
#     time.sleep(12)
    
#     return HttpResponse(serialized_data)
#     # json_response = JsonResponse(serialized_data, safe=False)

#     # # Return the JSON response
#     # return json_response

# @login_required
# @api_view(('GET', 'POST',))
# def updateCollectionId(request):
#     database = request.session['databaseSAP']

#     collections = Picking.objects.all().distinct().values('collection', 'company').order_by('collection')
#     # collections = [collection for collection in collections]
#     console.log(collections)
#     console.log(collections[3])
#     # console.log(len(collections))


#     for i, item in enumerate(collections):
        
#         # if i > 4:
#         #     break
#         console.log(item)
#         collection = item["collection"]
#         company = item['company']
#         try:
#             collectionId = getCollectionIDByName(database, collection)
#         except:
#             continue
#         console.log(collectionId)

#         console.log(company)

#         data = Picking.objects.filter(collection=collection, company=company)
#         data.update(collectionId=collectionId)
#         console.log(data.values('collection', 'collectionId'))


#     return Response({"OK":"OK"}, status=status.HTTP_200_OK)


# @login_required
# # @api_view(('GET', 'POST',))
# def downloadPickingTemplate(request, pvOrder):
#     console.log("Va pa esa mano")
#     database = request.session['databaseSAP']
#     company = Company.objects.get(name=database)

#     columns = []

#     query = f"""
#             SELECT * 
#             FROM picking_picking T0
#             INNER JOIN picking_box T1 ON T0.idPicking = T1.idPicking_id
#             INNER JOIN picking_boxitem T2 ON T2.idBox_id = T1.idBox
#             where t0.saleOrder = {pvOrder}
#             and T0.company_id = {company}
#             order by itemCode;
#         """
#     with connections['default'].cursor() as cursor:
#         cursor.execute(query)
#         columns = [col[0] for col in cursor.description]
#         # result = [dict(zip(columns, row)) for row in cursor.fetchall()]
#         result = list(cursor.fetchall())

#     queryset = QuerySet(model=passTable, using='default')
#     queryset._result_cache = list(result)

#     today = datetime.now()
#     strToday = today.strftime("%Y%m%d")

    

#     console.log(result[0:10])

#     data = [list(row) for row in result]
    

#     data.insert(0, columns)
#     sheet = excel.pe.Sheet(data)
#     return excel.make_response(sheet, "xlsx", file_name=f"pickingTemplate-{pvOrder}-{database}-{strToday}.xlsx")




#     # DuplicatePickingRegister

#     # return Response({"OK":"OK"}, status=status.HTTP_200_OK)

# # def readExcelfileToJson():

# import pandas as pd
# from django.core.files.storage import FileSystemStorage
# from django.core.files.uploadedfile import UploadedFile


# @api_view(('GET', 'POST',))
# def readExcelfileToJson(request):

#     # console.log(request.FILES)
#     console.log(request.data)
#     database = request.session['databaseSAP']
#     orderOrQuotation = request.query_params["selection"]
#     pvOrder = request.query_params["pvOrder"] 

#     originOrder = request.data["originOrder"] 
#     originDatabaseSelected = request.data["originDatabaseSelected"] 

#     destinationOrder = request.data["destinationOrder"] 
#     destinationDatabaseSelected = request.data["destinationDatabaseSelected"] 

#     database = request.session['databaseSAP']
#     company = Company.objects.get(id=originDatabaseSelected)

#     destinationDb = Company.objects.get(id=destinationDatabaseSelected)

#     columns = []

#     query = f"""
#         SELECT * 
#         FROM picking_picking T0
#         INNER JOIN picking_box T1 ON T0.idPicking = T1.idPicking_id
#         INNER JOIN picking_boxitem T2 ON T2.idBox_id = T1.idBox
#         where t0.saleOrder = {originOrder}
#         and T0.company_id = {company}
#         order by itemCode;
#         """

#     queryItemsQuantities = f"""
#         SELECT itemCode, SUM(quantity) as quantity
#         FROM picking_picking T0
#         INNER JOIN picking_box T1 ON T0.idPicking = T1.idPicking_id
#         INNER JOIN picking_boxitem T2 ON T2.idBox_id = T1.idBox
#         where t0.saleOrder = {originOrder}
#         and T0.company_id = {originDatabaseSelected}
#         group by itemCode
#         order by itemCode;
#     """
        
#     with connections['default'].cursor() as cursor:
#         cursor.execute(queryItemsQuantities)
#         columns = [col[0] for col in cursor.description]
#         result = [dict(zip(columns, row)) for row in cursor.fetchall()]
#         # result = list(cursor.fetchall())

#     queryset = QuerySet(model=passTable, using='default')
#     queryset._result_cache = list(result)


#     console.log(pvOrder)
#     console.log(orderOrQuotation)

#     if request.method == 'POST': # and request.FILES:
#         # file = request.FILES['originPicking']
#         # console.log(file)

#         # try:
#             # Leer el archivo Excel
#         # df = pd.read_excel(file)
#         # # console.log(df[0:10])

#         # df = df.drop_duplicates(subset='itemCode', keep='first')

#         # # Reemplazar valores nan con None
#         # df = df.where(pd.notnull(df), "")

#         # console.log(df)

        

#         # # Convertir el DataFrame a un diccionario
#         # data = df.to_dict(orient='records')

#         # console.log(data[0:10])

#         itemCodes = ",".join([filterCharacters(str(f"'{i['itemCode']}'")) for i in result])[0::]
#         quantities = ",".join([filterCharacters(str(f"'{i['quantity']}'")) for i in result])[0::]
#         # itemCodes = ",".join([filterCharacters(str(f"'{i['itemCode']}'")) for i in data])[0::]

#         # console.log(itemCodes)

#         sapSaleOrderInformation = getSaleOrderOrQuotationInformation(destinationDb.name, originOrder, destinationOrder, orderOrQuotation, itemCodes, quantities)
#         console.log(sapSaleOrderInformation)

#         # return Response({"excelInformation":data, "saleOrder": sapSaleOrderInformation})
#         return Response(sapSaleOrderInformation)

#         # except Exception as e:
#         #     return HttpResponse(f"Error leyendo el archivo Excel: {e}")

#     return HttpResponse("Método no permitido")




# @api_view(('GET', 'POST',))
# def copyPickingRegistersToNewDb(request):
#     console.log(request.data)
#     database = request.session['databaseSAP']

#     usuario = request.session['usuario']
#     company = Company.objects.get(name=database)




#     pvOrder = request.query_params["pvOrder"]
#     orderOrQuotation = request.query_params["selection"]
#     pvOrder = request.data['originOrder']
#     destinationOrder = request.data['destinationOrder']

#     # if request.data['originDatabaseSelected'] == request.data['destinationDatabaseSelected']:
#     #     return Response({"error": "error"}, status=status.HTTP_400_BAD_REQUEST)

#     originCompany = Company.objects.get(id=request.data['originDatabaseSelected'])
#     destinationCompany = Company.objects.get(id=request.data['destinationDatabaseSelected'])
    
#     pickingList = Picking.objects.filter(saleOrder=pvOrder, company=originCompany)

#     if orderOrQuotation == "order":
#         saleOrderQuotationItems = queryGetItemsSaleOrder(destinationOrder, destinationCompany.name)
#     else:
#         saleOrderQuotationItems = getItemsSaleQuotation(destinationOrder, destinationCompany.name)

#     console.log(saleOrderQuotationItems)

#     saleOrderItems = [item['ItemCode'] for item in saleOrderQuotationItems]

#     console.log(saleOrderItems)

#     console.log(pickingList)

#     for picking in pickingList:

#         # isPickingDuplicated = DuplicatedPicking.objects.filter(idOrigen=picking.idPicking)

#         ####################################

#         queryValidateExistCopy = f"""
#             SELECT 
#                 idDestino_id,
#                 idOrigen_id,
#                 T1.company_id as companyOrigen,
#                 T2.company_id as companyDestino
#             FROM picking_duplicatedpicking T0
#             INNER JOIN picking_picking T1 ON T1.idPicking = T0.idOrigen_id 
#             INNER JOIN picking_picking T2 ON T2.idPicking = T0.idDestino_id
#             where (T0.idOrigen_id = {picking.idPicking} or T0.idDestino_id =  {picking.idPicking})  and T1.company_id = {request.data['originDatabaseSelected']} and T2.company_id = {request.data['destinationDatabaseSelected']};
#         """
            
#         with connections['default'].cursor() as cursor:
#             cursor.execute(queryValidateExistCopy)
#             columns = [col[0] for col in cursor.description]
#             result = [dict(zip(columns, row)) for row in cursor.fetchall()]
#             # result = list(cursor.fetchall())

#         # queryset = QuerySet(model=passTable, using='default')
#         # queryset._result_cache = list(result)


#         console.log(result)

        
#         if len(result) > 0:
#             # continue
#             updatePicking = Picking.objects.get(idPicking=result[0]['idDestino_id'])
#             updatePicking.updateCopiedDate = timezone.now()
#             updatePicking.userUpdatedCopy = usuario
#             updatePicking.save()

#             boxes = Box.objects.filter(idPicking_id=updatePicking.idPicking)

#             for box in boxes:
#                 boxitems = BoxItem.objects.filter(idBox=box.idBox).delete()

#             boxes.delete()

#             pickingBoxes = Box.objects.filter(idPicking=picking.idPicking)

#             for pickingBox in pickingBoxes:
#                 boxInformation = model_to_dict(pickingBox)
#                 latestIdBox = boxInformation['idBox']
#                 boxInformation.pop('idBox')

#                 boxInformation['idDimension'] = Dimension.objects.get(idDimension=boxInformation['idDimension'])
#                 boxInformation['idPicking'] = Picking.objects.get(idPicking=updatePicking.idPicking)
#                 try:
#                     boxInformation['idWarehouseCustomer'] = WarehouseCustomer.objects.get(idWarehouseCustomer=boxInformation['idWarehouseCustomer'])
#                 except:
#                     pass
#                 boxInformation['codebars'] = int(Box.objects.latest('codebars').codebars) + 1
                
#                 nuevaBox = Box(**boxInformation)
#                 nuevaBox.save()

#                 pickingBoxItems = BoxItem.objects.filter(idBox=latestIdBox)

#                 for boxItem in pickingBoxItems:
#                     boxItemInformation = model_to_dict(boxItem)
#                     latestIdBoxItem = boxItemInformation['idBoxItem']
#                     boxItemInformation.pop('idBoxItem')
#                     boxItemInformation['idBox'] = Box.objects.get(idBox=nuevaBox.idBox)

#                     if boxItemInformation['itemCode'] in saleOrderItems:
#                         nuevoBoxItem = BoxItem(**boxItemInformation)
#                         nuevoBoxItem.save()
#                     else:
#                         console.log(F"No se encontro {boxItemInformation['itemCode']}")
#             continue

#             # return Response({"res": "Realizado"}, status=status.HTTP_200_OK)
#         # console.log(orderOrQuotation)

#         ####################################

        
#         # console.log(isPickingDuplicated)
        

#         # kwargs  = picking.__dict__.copy()
#         information = model_to_dict(picking)
#         latestIdPicking = information['idPicking']
#         information .pop('idPicking')
#         information['saleOrder'] = destinationOrder
#         information['isDuplicated'] = True
#         information['copiedDate'] = timezone.now()
#         information['updateCopiedDate'] = None
#         information['userCreatedCopy'] = usuario
#         information['userUpdatedCopy'] = None
#         information['status'] = Status.objects.get(idStatus=information['status'])
#         information['company'] = destinationCompany # Company.objects.get(id=information['company'])
#         # information.pop('status_id')
        
#         #Creacion del picking
#         nuevoPicking = Picking(**information)
#         nuevoPicking.save()
#         console.log(nuevoPicking.idPicking)
        

#         pickingBoxes = Box.objects.filter(idPicking=latestIdPicking)

#         pickingDuplicado =  DuplicatedPicking(
#             idOrigen=Picking.objects.get(idPicking=latestIdPicking),
#             idDestino=Picking.objects.get(idPicking=nuevoPicking.idPicking),
#         )
#         pickingDuplicado.save()


#         for pickingBox in pickingBoxes:
#             boxInformation = model_to_dict(pickingBox)
#             latestIdBox = boxInformation['idBox']
#             boxInformation.pop('idBox')

#             console.log(boxInformation)

#             boxInformation['idDimension'] = Dimension.objects.get(idDimension=boxInformation['idDimension'])
#             boxInformation['idPicking'] = Picking.objects.get(idPicking=nuevoPicking.idPicking)

#             try:
#                 boxInformation['idWarehouseCustomer'] = WarehouseCustomer.objects.get(idWarehouseCustomer=boxInformation['idWarehouseCustomer']) 
#             except:
#                 pass
#             boxInformation['codebars'] = int(Box.objects.latest('codebars').codebars) + 1
            
#             nuevaBox = Box(**boxInformation)
#             nuevaBox.save()

#             pickingBoxItems = BoxItem.objects.filter(idBox=latestIdBox)

#             for boxItem in pickingBoxItems:
#                 boxItemInformation = model_to_dict(boxItem)
#                 latestIdBoxItem = boxItemInformation['idBoxItem']
#                 boxItemInformation.pop('idBoxItem')
#                 boxItemInformation['idBox'] = Box.objects.get(idBox=nuevaBox.idBox)
#                 if boxItemInformation['itemCode'] in saleOrderItems:
#                     nuevoBoxItem = BoxItem(**boxItemInformation)
#                     nuevoBoxItem.save()
    


#     return Response({"res": "Realizado"})

