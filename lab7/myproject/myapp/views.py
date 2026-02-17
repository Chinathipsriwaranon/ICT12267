from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("ICT123 SPU")

def about(request):
    return HttpResponse("<h1>เกี่ยวกับเรา</h1>")

def form(request):
    return HttpResponse("<h1>แบบฟอร์มบันทึกข้อมูล</h1>")

def contact(request):
    return HttpResponse("<h1>ติดต่อ 68108992 Chinathip Sriwaranon</h1>")