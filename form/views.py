from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from .serializer import alistSerializer,blistSerializer,fieldsSerializer, FieldUpdateSerializer,FieldUpdateSerializerV2
from .models import alist,blist,fields

@api_view(['GET'])
def getFields(request):
    myfields=fields.objects.all()
    serializer= fieldsSerializer(myfields,many=True)
    return Response(serializer.data)
@api_view(['POST'])
def getDataList(request):
        request_type = request.data.get("type")
        request_fields = request.data.get("fields")

        if request_type == 'A':
            queryset = alist.objects.all()
        elif request_type == 'B':
            queryset = blist.objects.all()
        else:
            return Response({"detail": "Invalid type provided."}, status=status.HTTP_400_BAD_REQUEST)

        q_filters = {}
        for field in request_fields:
            for key, value in field.items():
                q_filters[key + "__in"] = value

        queryset = queryset.filter(**q_filters)

        if request_type == 'A':
            serializer = alistSerializer(queryset, many=True)
        elif request_type == 'B':
            serializer = blistSerializer(queryset, many=True)

        return Response(serializer.data)


@api_view(['POST'])
def updateListData(request):
    if request.method == 'POST':
        request_type = request.data.get("type")
        list_data = request.data.get("list")

        if request_type == 'A':
            for item in list_data:
                instance_id = item.get("id")
                try:
                    instance = alist.objects.get(id=instance_id)
                    serializer = alistSerializer(instance, data=item, partial=True)
                    if serializer.is_valid():
                        serializer.save()
                except alist.DoesNotExist:
                    raise NotFound(f"alist with id={instance_id} does not exist.")

            return Response({"message": "Update successful."})

        elif request_type == 'B':
            for item in list_data:
                instance_id = item.get("id")
                try:
                    instance = blist.objects.get(id=instance_id)
                    serializer = blistSerializer(instance, data=item, partial=True)
                    if serializer.is_valid():
                        serializer.save()
                except blist.DoesNotExist:
                    raise NotFound(f"blist with id={instance_id} does not exist.")

            return Response({"message": "Update successful."})

        return Response({"message": "Invalid type provided."}, status=400)

@api_view(['POST'])
def addListData(request):
    if request.method == 'POST':
        request_type = request.data.get("type")
        list_data = request.data.get("list")

        if request_type == 'A':
            serializer = alistSerializer(data=list_data, many=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Rows added successfully."})
            else:
                return Response(serializer.errors, status=400)

        elif request_type == 'B':
            serializer = blistSerializer(data=list_data, many=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Rows added successfully."})
            else:
                return Response(serializer.errors, status=400)

        return Response({"message": "Invalid type provided."}, status=400)
        
@api_view(['POST'])
def deleteListData(request):
    if request.method == 'POST':
        request_type = request.data.get("type")
        ids = request.data.get("ids")

        if request_type == 'A':
            try:
                alist.objects.filter(id__in=ids).delete()
                return Response({"message": "Rows deleted successfully."})
            except Exception as e:
                return Response({"message": str(e)}, status=500)

        elif request_type == 'B':
            try:
                blist.objects.filter(id__in=ids).delete()
                return Response({"message": "Rows deleted successfully."})
            except Exception as e:
                return Response({"message": str(e)}, status=500)

        return Response({"message": "Invalid type provided."}, status=400)

@api_view(['POST'])
def hideFields(request):
      if request.method == 'POST':
        serializer = FieldUpdateSerializer(data=request.data)
        if serializer.is_valid():
            fields_to_update = [field.upper() for field in serializer.validated_data['fields']]
            fields.objects.filter(name__in=fields_to_update).update(hide='yes')
            return Response({"message": "Fields updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def unhideFields(request):
      if request.method == 'POST':
        serializer = FieldUpdateSerializer(data=request.data)
        if serializer.is_valid():
            fields_to_update = [field.upper() for field in serializer.validated_data['fields']]
            fields.objects.filter(name__in=fields_to_update).update(hide=None )
            return Response({"message": "Fields updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def update_fields(request):
    serializer = FieldUpdateSerializerV2(data=request.data)

    if serializer.is_valid():
        fields_data = serializer.validated_data['fields']

        for field_data in fields_data:
            name = field_data['name'].upper()
            width = field_data['width']

            # Update the 'width' value in the 'fields' table
            fields.objects.filter(name=name).update(width=width)

        return Response({'message': 'Fields updated successfully.'})

    return Response(serializer.errors, status=400)
