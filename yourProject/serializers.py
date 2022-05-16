from dataclasses import field
from rest_framework import serializers
from yourProject.models import ProjectDetails

class ProjectDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectDetails
        field = ('projectName', 'developerNames', 'dateOfStart', 'dateOfEnd', 'languagesUsed', 'projectContent')