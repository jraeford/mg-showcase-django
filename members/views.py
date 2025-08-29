
from django.shortcuts import render, get_object_or_404
from .models import Member

def home(request):
    members = Member.objects.all()
    return render(request, "members/home.html", {"members": members})

def member_detail(request, slug):
    member = get_object_or_404(Member, slug=slug)
    return render(request, "members/detail.html", {"member": member})
