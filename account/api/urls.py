from django.urls import path
from .import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('current_user/',views.CurrentUser.as_view(),name='current_user'),
    
    path('cand_register/',views.CandidateRegisterView.as_view(),name="cand_register"),
    path("emp_register/",views.EmployerRegisterView.as_view(),name="emp_register"),

    path('otp_verify/',views.OtpVarificationView.as_view(),name="otp_verify"),
    path('resend_otp/',views.ResendOtpView.as_view(),name="resend_otp"),

    path('forgot_pass/',views.ForgotPassView.as_view(),name="forgot_pass"),
    path('reset_password/',views.ResetPassword.as_view(),name="reset_password"),
    
    path('Emplogin/',views.EmpLoginView.as_view(),name="login"),
    path('candidatelogin/',views.CandidateLoginView.as_view(),name="login"),
    path('admin/login/',views.AdminLoginView.as_view(),name="adminlogin"),

    path('auth/employer/',views.AuthEmployerView.as_view(),name="authemployer"),
    path('auth/candidate/',views.AuthCandidateView.as_view(),name="authcandidate"),

    path("user/details/", views.UserDetails.as_view(), name="user-details"),
    path("user/profile_creation/",views.CandidateProfileCreation.as_view(),name='CandidateProfileCreation'),
    path("user/emp_profile_creation/",views.EmployerProfileCreatView.as_view(),name="employerProfileCreation"),
    path("user/edit/",views.UserEditView.as_view(),name="useredit"),
    # path("user/Empedit/",views.EmpUserEditView.as_view(),name="empUserEdit")

]

