from django.db import models

# Create your models here.

# section models

class Section(models.Model):
    landing_heading=models.CharField(max_length=200)
    contact_heading=models.CharField(max_length=200,default=0)
    contact_para=models.CharField(max_length=200,default=0)
    service_heading=models.CharField(max_length=200,default=0)
    service_para=models.CharField(max_length=200,default=0)
    milestone_heading=models.CharField(max_length=200,default=0)
    milestone_para=models.CharField(max_length=200,default=0)
    project_heading=models.CharField(max_length=200,default=0)
    project_para=models.CharField(max_length=200,default=0)
    gallery_heading=models.CharField(max_length=200,default=0)
    gallery_para=models.CharField(max_length=200,default=0)
    team_heading=models.CharField(max_length=200,default=0)
    team_para=models.CharField(max_length=200,default=0)
    teximonial_heading=models.CharField(max_length=200,default=0)
    teximonial_para=models.CharField(max_length=200,default=0)
    achivement_heading=models.CharField(max_length=200,default=0)
    achivement_para=models.CharField(max_length=200,default=0)
    about_heading=models.CharField(max_length=200,default=0)
    about_para=models.CharField(max_length=200,default=0)
   

# query models

class Query_data(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    address=models.CharField(max_length=200)
    number=models.CharField(max_length=12,default=0)
    queries=models.CharField(max_length=1000,default=0)

# term and policy models

class Term_policy(models.Model):
    condition_use=models.CharField(max_length=1000)
    privacy_policy=models.CharField(max_length=1000)    
    age_restriction=models.CharField(max_length=1000)    
    intellectual_propertye=models.CharField(max_length=1000)    
    user_accounts=models.CharField(max_length=1000)    
    disputes=models.CharField(max_length=1000)    
    indemnification=models.CharField(max_length=1000)    
    limitation_on_liability=models.CharField(max_length=1000)  


# team models

class Team(models.Model):
    designer_name=models.CharField(max_length=200,default=0)
    designer_designation=models.CharField(max_length=100,default=0)
    designer_photo=models.ImageField(upload_to="web_photos",blank=True)
    designer_instra_link=models.URLField(blank=True)
    designer_facebook_link=models.URLField(blank=True)
    designer_twitter_link=models.URLField(blank=True)
    designer_google_link=models.URLField(blank=True)
    founder_name=models.CharField(max_length=200,default=0)
    founder_designation=models.CharField(max_length=100,default=0)
    founder_photo=models.ImageField(upload_to="web_photos",blank=True)
    founder_instra_link=models.URLField(blank=True)
    founder_facebook_link=models.URLField(blank=True)
    founder_twitter_link=models.URLField(blank=True)
    founder_google_link=models.URLField(blank=True)
    manager_name=models.CharField(max_length=200,default=0)
    manager_designation=models.CharField(max_length=100,default=0)
    manager_photo=models.ImageField(upload_to="web_photos",blank=True)
    manager_instra_link=models.URLField(blank=True)
    manager_facebook_link=models.URLField(blank=True)
    manager_twitter_link=models.URLField(blank=True)
    manager_google_link=models.URLField(blank=True)
    engineer_name=models.CharField(max_length=200,default=0)
    engineer_designation=models.CharField(max_length=100,default=0) 
    engineer_photo=models.ImageField(upload_to="web_photos",blank=True)
    engineer_instra_link=models.URLField(blank=True)
    engineer_facebook_link=models.URLField(blank=True)
    engineer_twitter_link=models.URLField(blank=True)
    engineer_google_link=models.URLField(blank=True) 


# soceity work models

class Soceity_work(models.Model):
    person_name=models.CharField(max_length=400,default=0)
    person_photo=models.ImageField(upload_to="web_photos",default=0)
    person_post=models.CharField(max_length=400,default=0)
    company_name=models.CharField(max_length=400,default=0)
    company_photo=models.ImageField(upload_to="web_photos",default=0)
    work_designation=models.CharField(max_length=400,default=0)
    work_description=models.CharField(max_length=800,default=0)
    address=models.CharField(max_length=400,default=0)
    end_of_work_date=models.DateField()
    rating=models.IntegerField(default=0)


# employee models

class Employee(models.Model):
    name=models.CharField(max_length=400)
    address=models.CharField(max_length=400)
    id_card=models.CharField(max_length=400)
    work_designation=models.CharField(max_length=50,default=0)
    employee_photo=models.ImageField(upload_to="web_photos")  

# gallery models    


class Gallery(models.Model):
    falseceilling_photo=models.ImageField(upload_to="web_photos",default=0)
    floor_photo=models.ImageField(upload_to="web_photos",default=0)
    wallpannel_photo=models.ImageField(upload_to="web_photos",default=0)
    washroom_photo=models.ImageField(upload_to="web_photos",default=0)
    bedroom_photo=models.ImageField(upload_to="web_photos",default=0)
    livingroom_photo=models.ImageField(upload_to="web_photos",default=0)
    kitchen_photo=models.ImageField(upload_to="web_photos",default=0)
    drawingroom_photo=models.ImageField(upload_to="web_photos",default=0)


# profile models    

class Profile(models.Model):
    company_name=models.CharField(max_length=100)
    company_logo=models.ImageField(upload_to="web_photos")
    gst_no=models.CharField(max_length=50)
    pan_no=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    number=models.IntegerField(default=0)
    monday_friday=models.CharField(max_length=100,default=0)
    saturday=models.CharField(max_length=100,default=0)
    sunday=models.CharField(max_length=100,default=0)
    years_of_market=models.IntegerField(default=0)
    instra_link=models.URLField(blank=True)
    facebook_link=models.URLField(blank=True)
    twitter_link=models.URLField(blank=True)
    google_link=models.URLField(blank=True)
    award=models.IntegerField(default=0)


# achivement models  #   
  
class Achivement(models.Model):
    achivement_img_one=models.ImageField(upload_to="web_photos")
    achivement_img_two=models.ImageField(upload_to="web_photos")


# abouts models    

class About(models.Model):
    vision_head=models.CharField(max_length=100,blank=True)
    vision=models.CharField(max_length=300)
    vision_img=models.ImageField(upload_to="web_photos")
    inspire_head=models.CharField(max_length=100,blank=True)
    inspire=models.CharField(max_length=300)
    inspire_img=models.ImageField(upload_to="web_photos")
    dreams_head=models.CharField(max_length=100,blank=True)
    dreams=models.CharField(max_length=300)
    dreams_img=models.ImageField(upload_to="web_photos")

# service category models

class Service_caterory(models.Model):
    category_name=models.CharField(max_length=400)

    def __str__(self):
        return self.category_name

# service work models

class Service(models.Model):
    item_name=models.CharField(max_length=400)
    brand=models.CharField(max_length=400)
    rate=models.IntegerField(default=0)
    item_description=models.CharField(max_length=400)
    category=models.ForeignKey(Service_caterory,on_delete=models.CASCADE)
    remarks=models.CharField(max_length=400)