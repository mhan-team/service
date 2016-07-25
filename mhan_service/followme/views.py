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
from .models import Trace, Point

from django.http import HttpResponse

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, TraceSerializer, PointSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class TraceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows traces to be viewed or edited.
    """
    queryset = Trace.objects.all().order_by('-created_on')
    serializer_class = TraceSerializer


class PointViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows trace points to be viewed or edited.
    """
    queryset = Point.objects.all().order_by('-time')
    serializer_class = PointSerializer


def index(request):
    trace_list = Trace.objects.order_by('created_on')
    if len(trace_list):
        output = ', '.join([t.name for t in trace_list])
    else:
        output = 'Followme has no trace'
    return HttpResponse(output)
