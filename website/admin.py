from django.contrib import admin
from website.models import Term_policy,Query_data,Team,Soceity_work,Employee,Gallery,Profile,About,Achivement,Section,Service,Service_caterory

# Register your models here.


# section models here.

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display=['id','landing_heading','contact_heading','contact_para','service_heading','service_para','milestone_heading','milestone_para','project_heading','project_para','gallery_heading','gallery_para','team_heading','team_para','teximonial_heading','teximonial_para','achivement_heading','achivement_para','about_heading','about_para']


# contact models here.

@admin.register(Query_data)
class Query_dataAdmin(admin.ModelAdmin):
    list_display=['id','name','email','address','number','queries']

# term and policy models here.

@admin.register(Term_policy)
class Term_policyAdmin(admin.ModelAdmin):
    list_display=['id','condition_use','privacy_policy','age_restriction','intellectual_propertye','user_accounts','disputes','indemnification','limitation_on_liability']  

# team models here.

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display=['id','designer_name','designer_designation','designer_photo','designer_instra_link','designer_facebook_link','designer_twitter_link','designer_google_link','founder_name','founder_designation','founder_photo','founder_instra_link','founder_facebook_link','founder_twitter_link','founder_google_link','manager_name','manager_designation','manager_photo','manager_instra_link','manager_facebook_link','manager_twitter_link','manager_google_link','engineer_name','engineer_designation','engineer_photo','engineer_instra_link','engineer_facebook_link','engineer_twitter_link','engineer_google_link']


# soceity models here.

@admin.register(Soceity_work)
class Soceity_workAdmin(admin.ModelAdmin):
    list_display=['id','person_photo','person_name','person_post','company_name','company_photo','work_designation','work_description','address','end_of_work_date','rating']

# employee models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','name','address','id_card','work_designation','employee_photo']


# gallery models here.

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display=['id','falseceilling_photo','floor_photo','wallpannel_photo','washroom_photo','bedroom_photo','livingroom_photo','kitchen_photo','drawingroom_photo'] 


# profile models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=['id','company_name','company_logo','gst_no','pan_no','address','email','number','years_of_market','instra_link','facebook_link','twitter_link','google_link','award']            


# about models here.
 
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display=['id','vision_head','vision','vision_img','inspire_head','inspire','inspire_img','dreams_head','dreams','dreams_img']    


# achivement models here.
 
@admin.register(Achivement)
class AchivementAdmin(admin.ModelAdmin):
    list_display=['id','achivement_img_one','achivement_img_two']    


# service models here.
 
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display=['id','item_name','brand','category','rate','item_description','remarks'] 


# service category here.
 
@admin.register(Service_caterory)
class Service_cateroryAdmin(admin.ModelAdmin):
    list_display=['id','category_name'] 