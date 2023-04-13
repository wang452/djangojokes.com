from django.urls import path

# new add CustomPasswordChangeView to redirect my account page after
# password changed success
from .views import CustomPasswordChangeView, MyAccountPageView

urlpatterns = [
    # new path redirect after password changed success
    path(
        "password/change/", CustomPasswordChangeView.as_view(),
        name="account_change_password"
    ),

    path('my-account/', MyAccountPageView.as_view(), name='my-account'),
]
