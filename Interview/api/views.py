from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import *
from account.models import *
from Interview.models import *
from EmpJobs.models import *
from .email import cancelMail
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from Interview.tasks import send_shedule_mail,cancell_shedule_mail
from EmpJobs.api.serializer import *
from EmpJobs.models import *

class InterviewSheduleView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self, request):
        print("step1")
        user = request.user
        employer = Employer.objects.get(user=user)
        candidate_id = request.data.get('candidate')
        job_id = request.data.get('job')
        date = request.data.get('date')
       
        try:
            candidate=Candidate.objects.get(id=candidate_id)
            job=Jobs.objects.get(id=job_id)
            email=candidate.user.email
            title=job.title
            username = employer.user.full_name
            print(email,date,user,title)
        except Candidate.DoesNotExist:
            print("error")
        
        
        print(request.data)
        serializer = SheduleInterviewSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            send_shedule_mail.delay(email,date,username,title)
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CancelApplicationView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        user=request.user
        employer = Employer.objects.get(user=user)
        candidate_id = request.data.get('candidate_id')
        job_id = request.data.get('job_id')
        job=Jobs.objects.get(id=job_id)
        candidate=Candidate.objects.get(id=candidate_id)
        application = InterviewShedule.objects.get(job=job_id,candidate=candidate_id)
        applyed = ApplyedJobs.objects.get(candidate=candidate_id,job=job_id)
        email=candidate.user.email
        date=application.date
        title=job.title
        username = employer.user.full_name
        try:
            if application:
                application.active = False
                application.status = "Canceled"
                applyed.status='Interview Cancelled'
                application.save()
                applyed.save()
                cancell_shedule_mail.delay(email,date,username,title)
                
                return Response({"message":"application cancelled sucessfull"},status=status.HTTP_200_OK)
        except application.DoesNotExist:
            return Response({"message":"something went wrong"},status=status.HTTP_404_NOT_FOUND)
        
class getShedulesView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        user = request.user
        print("5cr67vt8by9un0im",user)
        try:
            try:
                candidate = Candidate.objects.get(user=user)
                shedules=InterviewShedule.objects.filter(candidate=candidate)
            except Candidate.DoesNotExist:
                employer = Employer.objects.get(user=user)
                shedules=InterviewShedule.objects.filter(employer=employer)
       
            print(shedules)
            serializer = InterviewSheduleSerializer(shedules, many=True)
            if serializer:
                return Response (serializer.data,status=status.HTTP_200_OK)
            
        except (Candidate.DoesNotExist, Employer.DoesNotExist):
            return Response({"message": "User is neither a candidate nor an employer"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class InterviewView(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
        print(request.data)
        roomId = request.data.get("roomId")
        interviewId = request.data.get("interviewId")
        try:
            interview = InterviewShedule.objects.get(id = interviewId)
            candidate_id =interview.candidate.id 
            print(interview)
            print("candidate",candidate_id)
            message = f'Interview call - {roomId} - {interviewId}'
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                    f'notifications_{candidate_id}',  
                    {
                        'type': 'send_notification',
                        'message': message
                    }
                )
            return Response(status=status.HTTP_200_OK)
            
        except InterviewShedule.DoesNotExist:
            return Response({"message":"no interview data found"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    

class InterviewStatusView(APIView):
        permission_classes=[AllowAny]
        def post(self,request):
            print(request.data)
            interviewId = request.data.get('interviewId')
            jobId =request.data.get('jobId')
            candidateId = request.data.get('candidateId')
            action = request.data.get('action')
            job = Jobs.objects.get(id=jobId)
            candidate = Candidate.objects.get(id=candidateId)
            try:
                interview = InterviewShedule.objects.get(id=interviewId)
                applyedjobs = ApplyedJobs.objects.get(candidate=candidate,job=job)
            except:
                return Response({"message":"something went wrong"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
            if action =='accept':
                if interview and applyedjobs:
                    interview.status = 'Selected'
                    interview.selected = True
                    applyedjobs.status = 'Accepted'
                    interview.save()
                    applyedjobs.save()
                else:
                    return Response({"message":"cannot make a change now"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
            if action =='reject':
                if interview and applyedjobs:
                    interview.status = 'Rejected'
                    interview.selected = True
                    applyedjobs.status = 'Rejected'
                    interview.save()
                    applyedjobs.save()
                else:
                    return Response({"message":"cannot make a change now"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

            return Response({"message":"status changeed"},status=status.HTTP_200_OK)

def testView(request):
    test.delay()
    return HttpResponse("Done")
  