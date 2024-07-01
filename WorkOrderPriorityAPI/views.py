from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from bson.objectid import ObjectId
from .models import Resource, AddedWorkOrder, UnaddedWorkOrder
from .mongodb_client import mongodb_client

class ResourceViewSet(viewsets.ViewSet):
    def list(self, request):
        db = mongodb_client.get_database()
        collection = db['WorkOrderPriorityAPI_resource']
        resources = list(collection.find())
        for resource in resources:
            resource['_id'] = str(resource['_id'])
        return Response(resources)

    def create(self, request):
        data = request.data
        resource = Resource(
            name=data['name'],
            capacity=data['capacity'],
            category=data['category']
        )
        resource.save()
        # Fetch the inserted resource to include the _id
        db = mongodb_client.get_database()
        collection = db['WorkOrderPriorityAPI_resource']
        inserted_resource = collection.find_one({'name': resource.name, 'capacity': resource.capacity, 'category': resource.category})
        inserted_resource['_id'] = str(inserted_resource['_id'])
        return Response(inserted_resource, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        db = mongodb_client.get_database()
        collection = db['WorkOrderPriorityAPI_resource']
        resource = collection.find_one({'_id': ObjectId(pk)})
        if resource:
            resource['_id'] = str(resource['_id'])
            return Response(resource)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        db = mongodb_client.get_database()
        collection = db['WorkOrderPriorityAPI_resource']
        data = request.data
        result = collection.update_one({'_id': ObjectId(pk)}, {'$set': data})
        if result.matched_count:
            resource = collection.find_one({'_id': ObjectId(pk)})
            resource['_id'] = str(resource['_id'])
            return Response(resource)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        db = mongodb_client.get_database()
        collection = db['WorkOrderPriorityAPI_resource']
        result = collection.delete_one({'_id': ObjectId(pk)})
        if result.deleted_count:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

class AddedWorkOrderViewSet(viewsets.ViewSet):
    def list(self, request):
        db = mongodb_client.get_database()
        collection = db['WorkOrderPriorityAPI_addedworkorder']
        added_workorders = list(collection.find())
        for workorder in added_workorders:
            workorder['_id'] = str(workorder['_id'])
        return Response(added_workorders)

    def create(self, request):
        data = request.data
        added_workorder = AddedWorkOrder(
            priority=data['priority'],
            woNumber=data['woNumber'],
            description=data['description'],
            requestedBy=data['requestedBy'],
            resourcePriority=data['resourcePriority'],
            notes=data['notes'],
            area=data['area'],
            category=data['category'],
            status=data['status']
        )
        added_workorder.save()
        # Fetch the inserted workorder to include the _id
        db = mongodb_client.get_database()
        collection = db['WorkOrderPriorityAPI_addedworkorder']
        inserted_workorder = collection.find_one({'woNumber': added_workorder.woNumber})
        inserted_workorder['_id'] = str(inserted_workorder['_id'])
        return Response(inserted_workorder, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        db = mongodb_client.get_database()
        collection = db['WorkOrderPriorityAPI_addedworkorder']
        added_workorder = collection.find_one({'_id': ObjectId(pk)})
        if added_workorder:
            added_workorder['_id'] = str(added_workorder['_id'])
            return Response(added_workorder)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        db = mongodb_client.get_database()
        collection = db['WorkOrderPriorityAPI_addedworkorder']
        data = request.data
        result = collection.update_one({'_id': ObjectId(pk)}, {'$set': data})
        if result.matched_count:
            added_workorder = collection.find_one({'_id': ObjectId(pk)})
            added_workorder['_id'] = str(added_workorder['_id'])
            return Response(added_workorder)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        db = mongodb_client.get_database()
        collection = db['WorkOrderPriorityAPI_addedworkorder']
        result = collection.delete_one({'_id': ObjectId(pk)})
        if result.deleted_count:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

class UnaddedWorkOrderViewSet(viewsets.ViewSet):
    def list(self, request):
        db = mongodb_client.get_database()
        collection = db['WorkOrderPriorityAPI_unaddedworkorder']
        unadded_workorders = list(collection.find())
        for workorder in unadded_workorders:
            workorder['_id'] = str(workorder['_id'])
        return Response(unadded_workorders)

    def create(self, request):
        data = request.data
        unadded_workorder = UnaddedWorkOrder(
            instructions=data['instructions'],
            status_date=data['status_date'],
            closed_date=data['closed_date'],
            dispatch=data['dispatch'],
            total_cost=data['total_cost'],
            requested_due_date=data['requested_due_date'],
            externalid=data['externalid'],
            parent_workorder=data['parent_workorder'],
            scheduled_date=data['scheduled_date'],
            parent_dispatch=data['parent_dispatch'],
            number=data['number'],
            createdby=data['createdby'],
            lastupdatedby=data['lastupdatedby'],
            id=data['id'],
            labor_cost=data['labor_cost'],
            created=data['created'],
            spares_estimate=data['spares_estimate'],
            priority=data['priority'],
            createdbyuser=data['createdbyuser'],
            kit_template=data['kit_template'],
            estimated_cost=data['estimated_cost'],
            estimated_hours=data['estimated_hours'],
            spares_cost=data['spares_cost'],
            status=data['status'],
            parent_fives=data['parent_fives'],
            description=data['description'],
            owner_assigned_date=data['owner_assigned_date'],
            requestedby_phone=data['requestedby_phone'],
            requestedby=data['requestedby'],
            project_workorder=data['project_workorder'],
            actual_hours=data['actual_hours'],
            parent_kaizen=data['parent_kaizen'],
            parent_sigevent=data['parent_sigevent'],
            costcenter=data['costcenter'],
            projectid=data['projectid'],
            owner=data['owner'],
            lastupdatedbyuser=data['lastupdatedbyuser'],
            product=data['product'],
            due_date=data['due_date'],
            site=data['site'],
            trade=data['trade'],
            machine=data['machine'],
            closed=data['closed'],
            lastupdated=data['lastupdated'],
            launch_date=data['launch_date'],
            category=data['category'],
            external_cost=data['external_cost'],
            attachment_count=data['attachment_count'],
            area=data['area']
        )
        unadded_workorder.save()
        # Fetch the inserted workorder to include the _id
        db = mongodb_client.get_database()
        collection = db['WorkOrderPriorityAPI_unaddedworkorder']
        inserted_workorder = collection.find_one({'number': unadded_workorder.number})
        inserted_workorder['_id'] = str(inserted_workorder['_id'])
        return Response(inserted_workorder, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        db = mongodb_client.get_database()
        collection = db['WorkOrderPriorityAPI_unaddedworkorder']
        unadded_workorder = collection.find_one({'_id': ObjectId(pk)})
        if unadded_workorder:
            unadded_workorder['_id'] = str(unadded_workorder['_id'])
            return Response(unadded_workorder)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        db = mongodb_client.get_database()
        collection = db['WorkOrderPriorityAPI_unaddedworkorder']
        data = request.data
        result = collection.update_one({'_id': ObjectId(pk)}, {'$set': data})
        if result.matched_count:
            unadded_workorder = collection.find_one({'_id': ObjectId(pk)})
            unadded_workorder['_id'] = str(unadded_workorder['_id'])
            return Response(unadded_workorder)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        db = mongodb_client.get_database()
        collection = db['WorkOrderPriorityAPI_unaddedworkorder']
        result = collection.delete_one({'_id': ObjectId(pk)})
        if result.deleted_count:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
