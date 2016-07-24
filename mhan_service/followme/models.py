"""
The MIT License (MIT)

Copyright (c) 2016 mhan-team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from django.db import models
from django.contrib.auth.models import User


class Trace(models.Model):
    name = models.CharField(max_length=64)
    created_on = models.DateTimeField()
    created_by = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Trace {self.name} created on {self.created_on}'.format(self=self)


class Point(models.Model):
    time = models.DateTimeField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    trace = models.ForeignKey(Trace, on_delete=models.CASCADE)

    def __str__(self):
        return '{self.time}: {self.latitude}, {self.longitude}'.format(self=self)
