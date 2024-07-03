from rest_framework import serializers
from account.models import *
from EmpJobs.models import *

class CandidateSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    class Meta:
        model = Candidate
        fields = ["id","phone","profile_pic","user_name","email","status"]
    
    def get_user_name(self, obj):
        return obj.user.full_name if obj.user.full_name else ""

    def get_email(self, obj):
        return obj.user.email if obj.user.email else ""
    
    def get_status(self,obj):
        return obj.user.is_active   

class EmployerSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    class Meta:
        model = Employer
        fields = ["id","phone","profile_pic","user_name","email","status"]
    
    def get_user_name(self, obj):
        return obj.user.full_name if obj.user.full_name else ""

    def get_email(self, obj):
        return obj.user.email if obj.user.email else ""
    
    def get_status(self,obj):
        return obj.user.is_active
    


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['education', 'college', 'specilization', 'completed', 'mark']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['full_name', 'email', 'user_type', 'date_joined', 'last_login', 'is_superuser', 'is_email_verified', 'is_staff', 'is_active']

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = ['title', 'location', 'lpa', 'jobtype', 'jobmode', 'experiance', 'applyBefore', 'posteDate', 'about', 'responsibility', 'active', 'industry', 'employer']

class ApplyedJobsSerializer(serializers.ModelSerializer):
    job = JobSerializer(read_only=True)
    class Meta:
        model = ApplyedJobs
        fields = ['job', 'status', 'applyed_on']

class CandidateDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    education = serializers.SerializerMethodField()
    applied_jobs = ApplyedJobsSerializer(many=True, read_only=True, source='applyedjobs_set')

    class Meta:
        model = Candidate
        fields = ['id', 'phone', 'dob', 'profile_pic', 'Gender', 'skills', 'resume', 'linkedin', 'github', 'place', 'user', 'education', 'applied_jobs']
    
    def get_education(self, obj):
        education = Education.objects.filter(user=obj.user)
        return EducationSerializer(education, many=True).data
    
class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = '__all__'

class EmployerDetailsSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    jobs = serializers.SerializerMethodField()

    class Meta:
        model = Employer
        fields = '__all__'
    
    def get_jobs(self, obj):
        jobs = Jobs.objects.filter(employer=obj)
        serializer = JobsSerializer(jobs, many=True)
        return serializer.data