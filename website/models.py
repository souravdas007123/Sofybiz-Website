from django.db import models

# Create your models here.

# section models

class Section(models.Model):
    landing_heading=models.CharField(max_length=200)
    contact_heading=models.CharField(max_length=200)
    contact_para=models.CharField(max_length=200)
    service_heading=models.CharField(max_length=200)
    service_para=models.CharField(max_length=200)
    milestone_heading=models.CharField(max_length=200)
    milestone_para=models.CharField(max_length=200)
    project_heading=models.CharField(max_length=200)
    project_para=models.CharField(max_length=200)
    gallery_heading=models.CharField(max_length=200)
    gallery_para=models.CharField(max_length=200)
    team_heading=models.CharField(max_length=200)
    team_para=models.CharField(max_length=200)
    teximonial_heading=models.CharField(max_length=200)
    teximonial_para=models.CharField(max_length=200)
    achivement_heading=models.CharField(max_length=200)
    achivement_para=models.CharField(max_length=200)
    about_heading=models.CharField(max_length=200)
    about_para=models.CharField(max_length=200)


# query models

class Query_data(models.Model):
    date=models.DateTimeField(auto_now=True,null=True)
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    address=models.CharField(max_length=200)
    number=models.CharField(max_length=12)
    queries=models.CharField(max_length=1000)

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
    person_name=models.CharField(max_length=400)
    person_photo=models.ImageField(upload_to="web_photos",blank=True)
    person_post=models.CharField(max_length=400)
    company_name=models.CharField(max_length=400)
    company_photo=models.ImageField(upload_to="web_photos",blank=True)
    work_designation=models.CharField(max_length=400)
    work_description=models.CharField(max_length=800)
    address=models.CharField(max_length=400)
    end_of_work_date=models.DateField()
    rating=models.IntegerField(default=4)


# employee models

class Employee(models.Model):
    name=models.CharField(max_length=400)
    address=models.CharField(max_length=400)
    id_card=models.CharField(max_length=400)
    work_designation=models.CharField(max_length=50,blank=True)
    employee_photo=models.ImageField(upload_to="web_photos",blank=True)

# gallery models


class Gallery(models.Model):
    falseceilling_photo=models.ImageField(upload_to="web_photos")
    floor_photo=models.ImageField(upload_to="web_photos")
    wallpannel_photo=models.ImageField(upload_to="web_photos")
    washroom_photo=models.ImageField(upload_to="web_photos")
    bedroom_photo=models.ImageField(upload_to="web_photos")
    livingroom_photo=models.ImageField(upload_to="web_photos")
    kitchen_photo=models.ImageField(upload_to="web_photos")
    drawingroom_photo=models.ImageField(upload_to="web_photos")


# profile models

class Profile(models.Model):
    company_name=models.CharField(max_length=100)
    company_logo=models.ImageField(upload_to="web_photos")
    gst_no=models.CharField(max_length=50)
    pan_no=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    number=models.IntegerField(default=9830229942)
    monday_friday=models.CharField(max_length=100,blank=True)
    saturday=models.CharField(max_length=100,blank=True)
    sunday=models.CharField(max_length=100,blank=True)
    years_of_market=models.IntegerField(blank=True)
    instra_link=models.URLField(blank=True)
    facebook_link=models.URLField(blank=True)
    twitter_link=models.URLField(blank=True)
    google_link=models.URLField(blank=True)
    award=models.IntegerField(blank=True)


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

    Cateto=[
            ("Wallpaper" ,"Wallpaper"),
            ("Door" ,"Door"),
            ("Roof_Water_Profing" ,"Roof_Water_Profing"),
            ("Paint" ,"Paint"),
            ("Marble" ,"Marble"),
            ("Siding_Window" ,"Siding_Window"),
            ("Ceiling_Light" ,"Ceiling_Light"),
            ("Falseceiling" ,"Falseceiling"),
            ("Bathroom" ,"Bathroom"),
            ("Basin" ,"Basin"),
            ("Kitchen_Counter" ,"Kitchen_Counter"),
            ("Tiles" ,"Tiles"),
        ]

    category=models.CharField(max_length=400,choices=Cateto,blank=True)
    item_name=models.CharField(max_length=400)
    brand=models.CharField(max_length=400)
    rate=models.IntegerField()
    item_description=models.CharField(max_length=400)
    remarks=models.CharField(max_length=400)