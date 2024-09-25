from django.db import models

# Create your models here.

TITLE_CHOICES = {
    ('Intro to Python','Intro to Python'),
    ('Django for Beginners','Django for Beginners'),
    ('Data Science Fundamentals','Data Science Fundamentals'),
}

class djangoClasses(models.Model):
    title = models.CharField(max_length=60, choices=TITLE_CHOICES)
    course_number = models.IntegerField()
    instructor_name = models.CharField(max_length=60)
    duration = models.FloatField()

    class Meta:
        verbose_name_plural = "Django Classes"

    objects = models.Manager()
    def __str__(self):
        return f"{self.title} ({self.course_number}) by {self.instructor_name}"



