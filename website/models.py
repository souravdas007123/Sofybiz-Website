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

    class Meta:
        verbose_name_plural='4. Section'


# query models

class Query_data(models.Model):
    date=models.DateTimeField(auto_now=True,null=True)
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    address=models.CharField(max_length=200)
    number=models.CharField(max_length=12)
    queries=models.CharField(max_length=1000)

    class Meta:
        verbose_name_plural='3. Query'


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

    class Meta:
        verbose_name_plural='6. Team'


# employee models

class Employee(models.Model):
    name=models.CharField(max_length=400)
    address=models.CharField(max_length=400)
    id_card=models.CharField(max_length=400)
    work_designation=models.CharField(max_length=50,blank=True)
    employee_photo=models.ImageField(upload_to="web_photos",blank=True)

    class Meta:
        verbose_name_plural='2. Employee'

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

    class Meta:
        verbose_name_plural='5. Gallery'


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

    class Meta:
        verbose_name_plural='1. Profile'


# achivement models  #

class Achivement(models.Model):
    achivement_img_one=models.ImageField(upload_to="web_photos")
    achivement_img_two=models.ImageField(upload_to="web_photos")

    class Meta:
        verbose_name_plural='8. Achivement'


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

    class Meta:
        verbose_name_plural='9. About'


# service work models

class Service(models.Model):

    Unit=[

        ("Cft" ,"Cft"),
        ("Kg" ,"Kg"),
        ("Mtr" ,"Mtr"),
        ("Ltr" ,"Ltr"),
        ("Pc" ,"Pc"),
        ("Pcs" ,"Pcs"),
        ("Roll" ,"Roll"),
        ("Sqft" ,"Sqft"),
        ("Sqmtr" ,"Sqmtr"),

        ]

    Cateto=[
            ("Basin" ,"Basin"),
            ("Bathroom" ,"Bathroom"),
            ("Ceiling_Light" ,"Ceiling Light"),
            ("Door" ,"Door"),
            ("Falseceiling" ,"False Ceiling"),
            ("Kitchen_Counter" ,"Kitchen Counter"),
            ("Marble" ,"Marble"),
            ("Paint" ,"Paint"),
            ("Roof_Water_Profing" ,"Roof Water Profing"),
            ("Siding_Window" ,"Siding Window"),
            ("Tiles" ,"Tiles"),
            ("Wallpaper" ,"Wallpaper"),
        ]

    category=models.CharField(max_length=400,choices=Cateto,blank=True)
    item_name=models.CharField(max_length=400)
    brand=models.CharField(max_length=400)
    rate=models.CharField(max_length=400)
    unit=models.CharField(max_length=400,choices=Unit,blank=True)
    item_description=models.CharField(max_length=400)
    remarks=models.CharField(max_length=400)

    class Meta:
        verbose_name_plural='7. Service'


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

    class Meta:
        verbose_name_plural='10. Soceity'



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

    class Meta:
        verbose_name_plural='11. Policy'
