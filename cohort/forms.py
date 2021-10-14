from django import forms

from cohort.models import Cohort


class CohortCreationForms(forms.ModelForm):

    class Meta:
        model = Cohort
        fields = "--__all__"