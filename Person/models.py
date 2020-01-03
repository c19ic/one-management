from django.db import models


class PersonSizes(models.Model):
    S_NONE = 0
    S0_2_4 = 1
    S6_2_12 = 2
    S12_AND_UP = 3
    SIZE_CHOICES = [(S_NONE,'None'),(S0_2_4,'0-4'),(S6_2_12,'6-12'),(S12_AND_UP,'12 And Up')]
    size = models.PositiveSmallIntegerField(choices = SIZE_CHOICES, default = S_NONE)

    def __str__(self):
        return self.get_size_display()

class PersonGender(models.Model):
    MALE = 0
    FEMALE = 1
    GENDER_CHOICES = [(MALE,'MALE'),(FEMALE,'FEMALE')]
    gender = models.PositiveSmallIntegerField(choices = GENDER_CHOICES)

    def __str__(self):
        return self.get_gender_display()

class HairColor(models.Model):
    HC_NONE = 0 
    HC_BLONDE = 1
    HC_DARK_BLONDE = 2
    HC_DARK_BROWN = 3
    HC_LIGHT_BROWN = 4
    HC_AUBURN = 5 
    HC_BROWN = 6
    HC_BRUNETTE = 7
    HC_BLACK = 8
    HC_RED = 9
    HC_SILVER = 10
    HC_GREY = 11
    HC_LIGHT_BLONDE = 12
    HC_SALT_PEPPER = 13
    HC_STRAWBERRY_BLONDE = 14
    HC_LIGHT_RED = 15
    HC_CHESTNUT = 16
    HC_BROWN_VENETIAN = 17

    HAIR_COLOR_CHOICES = [
        (HC_NONE,'----'),
        (HC_BLONDE,'Blonde'),
        (HC_DARK_BLONDE,'Dark Blonde'),
        (HC_DARK_BROWN,'Dark Brown'),
        (HC_LIGHT_BROWN,'Light Brown'),
        (HC_AUBURN,'Auburn'),
        (HC_BROWN,'Brown'),
        (HC_BRUNETTE,'Brunette'),
        (HC_BLACK,'Black'),
        (HC_RED,'Red'),
        (HC_SILVER,'Silver'),
        (HC_GREY,'Grey'),
        (HC_LIGHT_BLONDE,'Light Blonde'),
        (HC_SALT_PEPPER,'Salt & Pepper'),
        (HC_STRAWBERRY_BLONDE,'Strawberry Blonde'),
        (HC_LIGHT_RED,'Light Red'),
        (HC_CHESTNUT,'Chestnut'),
        (HC_BROWN_VENETIAN,'Brown Venetian')
    ]

    hair_color = models.PositiveSmallIntegerField(choices = HAIR_COLOR_CHOICES, default = HC_NONE)

    def __str__(self):
        return self.get_hair_color_display()

class EyeColor(models.Model):
    EC_NONE = 0
    EC_BLUE = 1 
    EC_BLUE_GREEN = 2
    EC_BLUE_GREY = 3
    EC_GREEN = 4
    EC_HAZEL = 5
    EC_BROWN = 6
    EC_GREY = 7
    EC_GREEN_GREY = 8
    EC_GREEN_BROWN = 9
    EC_BLACK = 10
    EC_DARK_BROWN = 11

    EYE_COLOR_CHOICES = [
        (EC_NONE,'----'),
        (EC_BLUE,'Blue'),
        (EC_BLUE_GREEN,'Blue/Green'),
        (EC_BLUE_GREY,'Blue/Grey'),
        (EC_GREEN,'Green'),
        (EC_HAZEL,'Hazel'),
        (EC_BROWN,'Brown'),
        (EC_GREY,'Grey'),
        (EC_GREEN_GREY,'Green/Grey'),
        (EC_GREEN_BROWN,'Green/Brown'),
        (EC_BLACK,'Black'),
        (EC_DARK_BROWN,'DarkBrown')
    ]

    eye_color = models.PositiveSmallIntegerField(choices = EYE_COLOR_CHOICES, default = EC_NONE)

    def __str__(self):
        return self.get_eye_color_display()


class PersonHeight(models.Model):
    ht_feet = models.PositiveSmallIntegerField()
    ht_inches = models.DecimalField(max_digits=4, decimal_places=1)

    def __str__(self):
        return str(self.ht_feet)+"\'"+str(self.ht_inches)+"\""

class SuitSize(models.Model):
    suit_inches = models.PositiveSmallIntegerField()
    suit_letter = models.CharField(max_length=2)
    def __str__(self):
        return str(self.suit_inches)+" "+self.suit_letter

class SiteMenu(models.Model):
    name = models.CharField(max_length = 25, default="SiteMenu")

    def __str__(self):
        return self.name

    def create_default_menu(self):
        self.save()
        home = BaseLink(name = "HOME", url_name = "Home", is_visible = True, belongs_to_menu = self)
        home.save()
        about = BaseLink(name = "ABOUT", url_name = "About", is_visible = True, belongs_to_menu = self)
        about.save()
        submissions = BaseLink(name = "SUBMISSIONS", url_name = "Submissions", is_visible = True, belongs_to_menu = self)
        submissions.save()
        instagram = BaseLink(name = "INSTAGRAM", url_name = "Instagram", is_visible = True, belongs_to_menu = self, instagram_url="home/instagram/come/onemanagement")
        instagram.save()
        women_group = BoardGroup(name = "WOMEN", url_name = "Women", is_visible = True, is_group = True, is_radio = True, belongs_to_menu = self)
        women_group.save()
        w_image = Board(name = "IMAGE", url_name = "Image", is_visible = True, is_radio = True, belongs_to_group = women_group)
        w_image.save()
        w_main = Board(name = "MAIN", url_name = "Main", is_visible = True, is_radio = True, belongs_to_group = women_group)
        w_main.save()
        w_development = Board(name = "DEVELOPMENT", url_name = "Development", is_visible = True, is_radio = True, belongs_to_group = women_group)
        w_development.save()
        w_one_1 = Board(name = "ONE.1", url_name = "ONE-1", is_visible = True, is_radio = True, belongs_to_group = women_group)
        w_one_1.save()
        w_studio = Board(name = "STUDIO", url_name = "Studio", is_visible = True, is_radio = False, belongs_to_group = women_group)
        w_studio.save()
        men_group = BoardGroup(name = "MEN", url_name = "Men", is_visible = True, is_group = True, is_radio = True, belongs_to_menu = self)
        men_group.save()
        m_main = Board(name = "MAIN", url_name = "Main", is_visible = True, is_radio = True, belongs_to_group = men_group)
        m_main.save()
        m_development = Board(name = "DEVELOPMENT", url_name = "Development", is_visible = True, is_radio = True, belongs_to_group = men_group)
        m_development.save()
        talent_group = BoardGroup(name = "TALENT", url_name = "Talent", is_visible = True, is_group = False, is_radio = False, belongs_to_menu = self)
        talent_group.save()
        engagers_group = BoardGroup(name = "ENGAGERS", url_name = "Engagers", is_visible = True, is_group = False, is_radio = False, belongs_to_menu = self)
        engagers_group.save()

class BaseLink(models.Model):
    name = models.CharField(max_length=25)
    url_name = models.CharField(max_length=25)
    is_visible = models.BooleanField(default = False)
    belongs_to_menu = models.ForeignKey(SiteMenu, on_delete = models.CASCADE)
    instagram_url = models.URLField(null = True)

    def __str__(self):
        return self.name

class BoardGroup(models.Model):
    name = models.CharField(max_length=25)
    url_name = models.CharField(max_length=25)
    is_visible = models.BooleanField(default = False)
    is_group = models.BooleanField(default = True)    
    is_radio = models.BooleanField(default = True) # True => radio, False => add on
    belongs_to_menu = models.ForeignKey(SiteMenu, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class Board(models.Model):
    name = models.CharField(max_length=25)
    url_name = models.CharField(max_length=25)
    is_visible = models.BooleanField(default = False)
    is_radio = models.BooleanField(default = True) # True => radio, False => add on
    belongs_to_group = models.ForeignKey(BoardGroup, on_delete = models.CASCADE)
    def __str__(self):
        return self.belongs_to_group.name +":"+self.name

class PersonInformation(models.Model):
    active = models.BooleanField(default = False)
    full_name = models.CharField(max_length=80)
    linebreak_name = models.CharField(max_length=80)
    email = models.EmailField()
    size_group = models.OneToOneField(PersonSizes, on_delete = models.CASCADE)
    gender = models.OneToOneField(PersonGender, on_delete = models.CASCADE)
    thumbnail = models.ImageField(upload_to='image/%Y/%m/%d')
    instagram = models.URLField()
    belongs_to_board_group = models.ManyToManyField(BoardGroup)
    belongs_to_board = models.ManyToManyField(Board)

    def __str__(self):
        return self.full_name

    @property
    def specs(self):
        if self.gender == PersonGender.MALE:
            return self.male_spec
        if self.gender == PersonGender.FEMALE:
            return self.female_spec

    def add_default_galleries(self):
        self.save()
        portfolio = PictureGallery(name = "Portfolio")
        portfolio.belongs_to_person = self
        portfolio.save()
        polaroids = PictureGallery(name = "Polaroids")
        polaroids.belongs_to_person = self
        polaroids.save()
        cover = PictureGallery(name = "Cover")
        cover.belongs_to_person = self
        cover.save()
        videos = VideoGallery(name = "Videos")
        videos.belongs_to_person = self
        videos.save()
        if self.gender == PersonGender.MALE:
            spec = MaleSpec(hair_color = HairColor.HC_BROWN,
                            eye_color = EyeColor.EC_BROWN,
                            height = PersonHeight(ht_feet = 6, ht_inches = 1),
                            shoe_size = 10,
                            suit = SuitSize(suit_inches = 44, suit_letter = "L"),
                            waist = 30,
                            inseam = 38,
                            belongs_to_person = self)
        if self.gender == PersonGender.FEMALE:
            spec = FemaleSpec(hair_color = HairColor.HC_BROWN,
                            eye_color = EyeColor.EC_BROWN,
                            height = PersonHeight(ht_feet = 6, ht_inches = 1),
                            shoe_size = 10,
                            bust = 34,
                            waist = 24,
                            hips = 34,
                            belongs_to_person = self)

class FemaleSpec(models.Model):
    hair_color = models.OneToOneField(HairColor, on_delete = models.CASCADE)
    eye_color = models.OneToOneField(EyeColor, on_delete = models.CASCADE)
    height = models.OneToOneField(PersonHeight, on_delete = models.CASCADE)
    shoe_size = models.DecimalField(max_digits=4, decimal_places=1)    
    bust = models.PositiveSmallIntegerField()
    waist = models.PositiveSmallIntegerField()
    hips = models.PositiveSmallIntegerField()
    belongs_to_person = models.OneToOneField(PersonInformation, on_delete = models.CASCADE)

class MaleSpec(models.Model):
    hair_color = models.OneToOneField(HairColor, on_delete = models.CASCADE)
    eye_color = models.OneToOneField(EyeColor, on_delete = models.CASCADE)
    height = models.OneToOneField(PersonHeight, on_delete = models.CASCADE)
    shoe_size = models.DecimalField(max_digits=4, decimal_places=1)    
    suit = models.OneToOneField(SuitSize, on_delete = models.CASCADE)
    waist = models.PositiveSmallIntegerField()
    inseam = models.PositiveSmallIntegerField()
    belongs_to_person = models.OneToOneField(PersonInformation, on_delete = models.CASCADE)  


class VideoGallery(models.Model):
    name = models.CharField(max_length=25)
    visible = models.BooleanField(default = False)
    belongs_to_person = models.ForeignKey(PersonInformation, on_delete = models.CASCADE)  

    def __str__(self):
        return self.name

class Video(models.Model):
    name = models.URLField()
    order = models.PositiveSmallIntegerField(default = 0)
    belongs_to_gallery = models.ManyToManyField(VideoGallery)
    belongs_to_person = models.ForeignKey(PersonInformation, on_delete = models.CASCADE)    

class PictureGallery(models.Model):
    name = models.CharField(max_length=25)
    visible = models.BooleanField(default = False)
    belongs_to_person = models.ForeignKey(PersonInformation, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class Picture(models.Model):
    pictureL = models.ImageField(upload_to='image/%Y/%m/%d')
    pictureR = models.ImageField(upload_to='image/%Y/%m/%d',null=True)
    is_linked = models.BooleanField(default = False)
    order = models.PositiveSmallIntegerField(default = 0)
    belongs_to_gallery = models.ManyToManyField(PictureGallery)
    belongs_to_person = models.ForeignKey(PersonInformation, on_delete = models.CASCADE)
