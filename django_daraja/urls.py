from django.urls import re_path, include
from . import views

test_patterns = [
	re_path(r'^$', views.index, name='django_daraja_index'),
	re_path(r'^oauth/success$', views.oauth_success, name='test_oauth_success'),
	re_path(r'^stk-push/success$', views.stk_push_success, name='test_stk_push_success'),
	re_path(r'^business-payment/success$', views.business_payment_success, name='test_business_payment_success'),
	re_path(r'^salary-payment/success$', views.salary_payment_success, name='test_salary_payment_success'),
	re_path(r'^promotion-payment/success$', views.promotion_payment_success, name='test_promotion_payment_success'),
]

urlpatterns = [
	re_path(r'^$', views.index, name='index'),
	# re_path(r'^tests/', include(test_patterns)),
    re_path(r'^oauth/success$', views.oauth_success, name='test_oauth_success'),
	re_path(r'^stk-push/success$', views.stk_push_success, name='test_stk_push_success'),
]

