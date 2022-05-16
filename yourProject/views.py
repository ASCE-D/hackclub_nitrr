from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

# Create your views here.

from yourProject.models import ProjectDetails
from yourProject.serializers import ProjectDetailsSerializer

@csrf_exempt
def ProjectDetailsApi(request,id=0):

    #   ========== code to display data ==================
    
    if request.method == 'GET':
        ProjectDetails = ProjectDetails.objects.all() 
        ProjectDetails_serializer = ProjectDetailsSerializer(ProjectDetails, many= True)
        return JsonResponse(ProjectDetails_serializer.data, safe = False)
    
    # ================= code to add data =======================
    
    elif request.method == 'POST':
        ProjectDetails_data = JSONParser().parse(request)
        ProjectDetails_serializer = ProjectDetailsSerializer(data = ProjectDetails_data)
        if ProjectDetails_serializer.is_valid():
            ProjectDetails_serializer.save()
            return JsonResponse("Added Successfully", safe = False)
        return JsonResponse("Failed to Add", safe = False)
    
    # ================== to update data ==========================

    elif request.method == 'PUT':
        ProjectDetails_data = JSONParser().parse(request)
        ProjectDetails = ProjectDetails.objects.get(projectName = ProjectDetails_data['projectName'])
        ProjectDetails_serializer = ProjectDetailsSerializer(ProjectDetails,data=ProjectDetails_data)
        if ProjectDetails_serializer.is_valid():
            ProjectDetails_serializer.save()
            return JsonResponse("Updated Successfully",safe= False)
        return JsonResponse("Failed to Update", safe = False)
    
    # ==================== To delete  data =========================

    elif request.method == 'DELETE':
        ProjectDetails = ProjectDetails.objects.get(projectName=id)
        ProjectDetails.delete()
        return JsonResponse("Deleted Successfully", safe = False)
    