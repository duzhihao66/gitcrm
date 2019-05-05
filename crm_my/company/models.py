from django.db import models


class Student(models.Model):
    # 学生
    name = models.CharField("姓名",max_length=64,blank=True,null=True)
    # sex_type = (('male','男'),('female','女'))
    # sex = models.CharField("性别",choices=sex_type,max_length=32,default='male',blank=True,null=True)
    birthday = models.DateField("出生日期",default=None,help_text="格式yyyy-mm-dd",blank=True,null=True)
    qq = models.CharField('QQ', max_length=64, unique=True, help_text='QQ号必须唯一')
    phone = models.BigIntegerField("手机号",blank=True,null=True)
    room = models.ForeignKey("Room",default="未选择教室",verbose_name="教室名")
    course = models.ForeignKey("Course",default="未选择课程",verbose_name="课程")

    class Meta:
        verbose_name = "学生"
        verbose_name_plural = "学生"

    def __str__(self):
        return self.name

class Room(models.Model):
    # 教室
    city = models.CharField('城市',max_length=32,blank=True,null=True)
    area = models.CharField('地区',max_length=32,blank=True,null=True)
    name = models.CharField("教室名",max_length=32,blank=True,null=True)

    class Meta:
        verbose_name = "教室名"
        verbose_name_plural = "教室名"

    def __str__(self):
        return self.name

class Course(models.Model):
    # 课程
    name = models.CharField("课程名",max_length=32,blank=True,null=True)
    intro = models.CharField("课程简介",max_length=32,blank=True,null=True)
    cycle = models.CharField("课程周期",max_length=32,blank=True,null=True)
    lecturer = models.CharField("讲师",max_length=32,blank=True,null=True)

    class Meta:
        verbose_name = "课程名"
        verbose_name_plural = "课程名"

    def __str__(self):
        return self.name
