from django.shortcuts import render
from django.shortcuts import render
from django.views.generic.base import View


class IndexView(View):
    def get(self, request):
        return render(
            request,
            'index.html',
        )