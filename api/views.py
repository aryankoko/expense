from rest_framework.response import Response
from rest_framework.decorators import api_view
from .seralizers import ItemsSerializer 
from .models import Items
# Create 
# your views here.

@api_view(['GET'])
def serverRun(req):
    return Response(status=200)


@api_view(['GET'])
def getAllTask(req):
    items = Items.objects.all()
    serializer = ItemsSerializer(items, many=True)
    return Response(serializer.data, status=200)

@api_view(['GET'])
def getSingleTask(req, pk):
    try:
        oneTask = Items.objects.get(id=pk)  # Try to get the item by its id (pk)
    except Items.DoesNotExist:
        return Response({'message': 'Invalid Id'}, status=404)  # Return 404 if item does not exist
    
    seralize = ItemsSerializer(oneTask)  # Serialize the item
    return Response(data=seralize.data)  # Return serialized data


@api_view(['POST'])
def addTask(req):
    newItem = req.data
    serialize = ItemsSerializer(data = newItem)
    if serialize.is_valid():
        serialize.save()
        return Response({'msg':'success', 'data':serialize.data},status=201)
    else:
        return Response(status=404)
    
@api_view(['DELETE'])
def delTask(req, pk):
    ite = Items.objects.get(pk=pk)
    if ite:
        ite.delete()
        return Response({'msg':'deleted'}, status=200)
    return Response({'msg':'Item not found'}, status=404)