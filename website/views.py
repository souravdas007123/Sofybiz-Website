from django.shortcuts import render
from website.forms import Queryform
from website.models import Term_policy,Query_data,Team,Soceity_work,Employee,Profile,About,Achivement,Gallery,Section,Service
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    gallery=Gallery.objects.all().order_by('-id')[0:1]
    section_heading_para=Section.objects.all()
    achivements=Achivement.objects.all()
    abouts=About.objects.all()
    employee=Employee.objects.all().order_by('-id')[0:1]
    soceity_work=Soceity_work.objects.all()
    soceity_work_count=Soceity_work.objects.all().order_by('-id')[0:1]
    team=Team.objects.all()
    profile=Profile.objects.all()

    # form area
    if request.method == 'POST':
        form=Queryform(request.POST)
        if form.is_valid():
          name=form.cleaned_data['name']
          email=form.cleaned_data['email']
          address=form.cleaned_data['address']
          number=form.cleaned_data['number']
          queries=form.cleaned_data['queries']
          user=Query_data(name=name,email=email,number=number,address=address,queries=queries)
          user.save()
        return HttpResponseRedirect('/')
    else: 
        form=Queryform(label_suffix=' ')
    return render(request,'website/home.html',{'form':form,'profile':profile,'team':team,'soceity_work':soceity_work,'soceity_work_count':soceity_work_count,'employee':employee,'abouts':abouts,'achivements':achivements,'section_heading_para':section_heading_para,'gallery':gallery})


def term(request):
    tp=Term_policy.objects.all()
    return render(request,'website/term_poly.html',{'tp':tp})

def kitchen(request):
    gallerys=Gallery.objects.all().order_by('-id')
    return render(request,'website/kitchen.html',{'gallerys':gallerys})

def living(request):
    gallerys=Gallery.objects.all().order_by('-id')
    return render(request,'website/living.html',{'gallerys':gallerys})

def bedroom(request):
    gallerys=Gallery.objects.all().order_by('-id')
    return render(request,'website/bedroom.html',{'gallerys':gallerys})

def washroom(request):
    gallerys=Gallery.objects.all().order_by('-id')
    return render(request,'website/washroom.html',{'gallerys':gallerys})

def drawingroom(request):
    gallerys=Gallery.objects.all().order_by('-id')
    return render(request,'website/drawingroom.html',{'gallerys':gallerys})

def floor(request):
    gallerys=Gallery.objects.all().order_by('-id')
    return render(request,'website/floor.html',{'gallerys':gallerys})

def wallpannel(request):
    gallerys=Gallery.objects.all().order_by('-id')
    return render(request,'website/wallpannel.html',{'gallerys':gallerys})

def falseceiling(request):
    gallerys=Gallery.objects.all().order_by('-id')
    return render(request,'website/falseceiling.html',{'gallerys':gallerys})

def constructionservice(request):
    if request.method=="POST":
        filter=request.POST.get('item_name')
        filter_data=Service.objects.filter(item_name=filter)
        return render(request,'website/construction_inner.html',{'data':filter_data})
    else:
     filter_data=Service.objects.all()
    return render(request,'website/construction_inner.html',{'data':filter_data})

def interiorservice(request):
    if request.method=="POST":
        filter=request.POST.get('item_name')
        filter_data=Service.objects.filter(item_name=filter)
        return render(request,'website/interior_inner.html',{'data':filter_data})
    else:
     filter_data=Service.objects.all()
    return render(request,'website/interior_inner.html',{'data':filter_data})

def lightingservice(request):
    if request.method=="POST":
        filter=request.POST.get('item_name')
        filter_data=Service.objects.filter(item_name=filter)
        return render(request,'website/lighting_inner.html',{'data':filter_data})
    else:
     filter_data=Service.objects.all()
    return render(request,'website/lighting_inner.html',{'data':filter_data})


