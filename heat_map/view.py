from django.views.generic import View
from django.shortcuts import render
from django.conf import settings


class Index(View):

    def get(self, request):
        return render(request, 'index.html', {'accessToken': settings.ACCESSTOKEN})
