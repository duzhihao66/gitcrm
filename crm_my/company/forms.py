# -*- coding: utf-8 -*-
from django import forms
from company import models
from django.core.exceptions import ValidationError

class BaseForm(forms.ModelForm):
    def __int__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for filed in self.fields.values():
            filed.widget.attrs.update({'class': 'form-control'})

# 学生form
# class StudentForm(BaseForm):
#     class Meta:
#         model = models.Student
#         fields = '__all__'


# 班级form
class RoomForm(BaseForm):
    class Meta:
        model = models.Room
        fields = "__all__"
        widgets = {
            'room':forms.widgets.SelectMultiple
        }

