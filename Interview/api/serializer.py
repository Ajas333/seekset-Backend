from rest_framework import serializers
from Interview.models import *
from EmpJobs.models import *
from EmpJobs.api.serializer import JobSerializer

class SheduleInterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewShedule
        fields = ['id','candidate', 'employer', 'job', 'date']
        read_only_fields = ['employer']

    def create(self, validated_data): 
        request = self.context.get('request')
        user = request.user
        employer = Employer.objects.get(user=user)
        validated_data['employer'] = employer
        return super().create(validated_data)
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = ['rolename', 'roleemail']

class InterviewSheduleSerializer(serializers.ModelSerializer):
    employer_name=serializers.SerializerMethodField()
    candidate_name = serializers.SerializerMethodField()
    applyDate = serializers.SerializerMethodField()
    job=JobSerializer()
    roles = serializers.SerializerMethodField()
    class Meta:
        model = InterviewShedule
        fields = ['roles','id','candidate','employer','job','date','active','selected','status','employer_name','applyDate','candidate_name']
    
    def get_employer_name(self,obj):
        return obj.employer.user.full_name
    
    def get_applyDate(self, obj):
        applyedJobs = ApplyedJobs.objects.filter(job=obj.job)
        if applyedJobs.exists():
            return applyedJobs.first().applyed_on  
        return None

    
    def get_candidate_name(self,obj):
        return obj.candidate.user.full_name
    
    def get_roles(self, obj):
        roles = Roles.objects.filter(employer=obj.employer)
        return RoleSerializer(roles, many=True).data
    