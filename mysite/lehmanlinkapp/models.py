from django.db import models

# Create your models here.

class Lehmanuser(models.Model):
    emplid = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    phone = models.CharField(max_length=15, blank=True, null=True)
    photo = models.CharField(max_length=50, blank=True, null=True)

    # like the toString() from java
    def __str__(self):
        output = "\n" +str(self.emplid) +"\t"+ self.username +"\t"+ self.email +"\t"+ self.phone +"\t"+ self.photo
        return output


    class Meta:
        managed = False
        db_table = 'lehmanuser'

# ---------------------------------------------------------

class Department(models.Model):
    dept_name = models.CharField(unique=True, max_length=30)

    def __str__(self):
        output = "\n" + self.dept_name
        return output

    class Meta:
        managed = False
        db_table = 'department'

# ---------------------------------------------------------

class Student(models.Model):
    user = models.ForeignKey(Lehmanuser, models.DO_NOTHING, primary_key=True)
    major_dept = models.ForeignKey(Department, models.DO_NOTHING, related_name="major")
    minor_dept = models.ForeignKey(Department, models.DO_NOTHING, blank=True, null=True, related_name="minor")
    major_vis = models.IntegerField()
    minor_vis = models.IntegerField(blank=True, null=True)

    def __str__(self):
        output = "\n" + str(self.user.emplid) +"\t"+ self.major_dept+"\t"+ self.minor_dept +"\t"+self.major_vis+"\t"+self.minor_vis
        return output

    class Meta:
        managed = False
        db_table = 'student'
        unique_together = (('user', 'major_dept'),)

# ---------------------------------------------------------

class Experience(models.Model):
    emplid = models.ForeignKey('Lehmanuser', models.DO_NOTHING, db_column='emplid')
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=100, blank=True, null=True)
    from_field = models.DateField(db_column='from')  # Field renamed because it was a Python reserved word.
    to = models.DateField()

    def __str__(self):
        output = "\n" + str(self.emplid) +"\t"+ self.title+"\t"+ self.description +"\t"+ str(self.from_field)+"\t"+self.to
        return output

    class Meta:
        managed = False
        db_table = 'experience'
        unique_together = (('id', 'emplid'),)

# ---------------------------------------------------------

class Instructor(models.Model):
    user = models.ForeignKey('Lehmanuser', models.DO_NOTHING, primary_key=True)
    dept = models.ForeignKey(Department, models.DO_NOTHING)

    def __str__(self):
        output = "\n" + str(self.emplid) +"\t"+dept.dept_name
        return output

    class Meta:
        managed = False
        db_table = 'instructor'
        unique_together = (('user', 'dept'),)

# ---------------------------------------------------------

class Course(models.Model):
    course_name = models.CharField(max_length=10)
    dept = models.ForeignKey('Department', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'course'
        unique_together = (('id', 'dept'),)

# ---------------------------------------------------------

class Coursesection(models.Model):
    user = models.ForeignKey('Lehmanuser', models.DO_NOTHING, primary_key=True)
    instruct = models.ForeignKey('Instructor', models.DO_NOTHING)
    course = models.ForeignKey(Course, models.DO_NOTHING)
    cs_year = models.TextField()  # This field type is a guess.
    semester = models.CharField(max_length=6)
    vis = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'coursesection'
        unique_together = (('user', 'instruct', 'course'),)

# ---------------------------------------------------------

class Alumni(models.Model):
    user = models.ForeignKey('Lehmanuser', models.DO_NOTHING, primary_key=True)
    grad_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'alumni'