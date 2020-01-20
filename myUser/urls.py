from django.urls import path , include
from . import views
from django.contrib.auth import views as auth_views

app_name = "myUser"

urlpatterns = [
    path('',views.index, name="index"),
    path('register/',views.register, name ='register'),
    path('logout/',views.logout_view,name='logout'),
    path('login/',views.login_view,name="login"),
    path('update/',views.update_view,name = 'update'),

    path('password_change/',auth_views.PasswordChangeView.as_view(template_name = 'registration/password_change.html'),name='password_change'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),name="password_change_done"),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name="password_reset"),#this path didn't need to apply template name. it's using form
    path('passowrd_reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name="password_reset_complete"),
]