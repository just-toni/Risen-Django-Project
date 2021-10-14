from django.urls import path

from . import views
from .views import create_page, hello_world, create_cohort

urlpatterns = [
    path('', views.get_all_cohorts, name="cohorts"),
    path('add_native_to_cohort', create_page),
    path('create_cohort', create_cohort, name="create_cohort"),
    path('<int:pk>', get_a_cohort),
    path('view_details_of_a_cohort', hello_world),
    path('remove_a_native_from_a_cohort', hello_world),
    path('delete_a_cohort', hello_world),
    path('update_a_cohort', hello_world)
]