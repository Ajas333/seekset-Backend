from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from account.models import *
from EmpJobs.models import *
from .serializer import *

class HomeView(APIView):
    permission_classes=[AllowAny]
    def get(self,request):
        candidates_count = Candidate.objects.count()
        employers_count = Employer.objects.count()
        jobs_count = Jobs.objects.filter(active=True).count()
        applications_count = ApplyedJobs.objects.exclude(status__in=['Rejected', 'Interview Cancelled']).count()
        data = {
            'candidates_count': candidates_count,
            'employers_count': employers_count,
            'jobs_count': jobs_count,
            'applications_count': applications_count,
        }
        return Response(data,status=status.HTTP_200_OK)
    
class CandidateListView(APIView):
    permission_classes=[AllowAny]
    def get(self,request):
        candidates = Candidate.objects.all()
        
        serializer = CandidateSerializer(candidates, many=True)
        print(serializer.data)
        return Response(serializer.data,status=status.HTTP_200_OK)
        # except:
        #     return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

class EmployerListView(APIView):
    permission_classes=[AllowAny]
    def get(self,request):
        employers = Employer.objects.all()
        
        serializer = EmployerSerializer(employers, many=True)
        print(serializer.data)
        return Response(serializer.data,status=status.HTTP_200_OK)
        # except:
        #     return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

class CandidateView(APIView):
    permission_classes=[AllowAny]
    def get(self,request,id):
        try:
            candidate = Candidate.objects.get(id=id)
            serializer = CandidateDetailSerializer(candidate)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Candidate.DoesNotExist:
            return Response({"error": "Candidate not found"}, status=status.HTTP_404_NOT_FOUND)

class EmployerView(APIView):
    permission_classes=[AllowAny]
    def get(self, request, id):
        try:
            employer = Employer.objects.get(id=id)
            serializer = EmployerDetailsSerializer(employer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Employer.DoesNotExist:
            return Response({"error": "Employer not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class StatusView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        print(request.data)
        id= request.data.get('id')
        action = request.data.get('action')
        try:
            candidate = Candidate.objects.get(id=id)
            user = User.objects.get(id=candidate.user.id)
        except:
            employe = Employer.objects.get(id=id)
            user = User.objects.get(id=employe.user.id)
        print(user)
        if user:
            if action == 'block':
                user.is_active = False
                user.save()
            else:
                user.is_active = True
                user.save()
            return Response({"message":"User Status Changed"},status=status.HTTP_200_OK)