from django.db import models

# Create your models here.


class Business(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    slug = models.SlugField(max_length=255, null=False, blank=False, unique=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    website = models.URLField()
    phone = models.CharField(max_length=15, null=True, blank=False)
    mail = models.EmailField()
    # 署長
    director_general = models.CharField(max_length=20, null=True, blank=False)
    # 副署長
    deputy_director_general1 = models.CharField(max_length=20, null=True, blank=False)
    deputy_director_general2 = models.CharField(max_length=20, null=True, blank=False)
    # 主任秘書
    chief_secretary = models.CharField(max_length=20, null=True, blank=False)

    def __str__(self):
        return self.name


# 海巡署
class Service(Business):
    pass


# 組，企劃組、後勤組
class Division(models.Model):
    superior = models.ForeignKey(Service, on_delete=models.PROTECT)
    name = models.CharField(max_length=50, null=False, blank=False)
    slug = models.SlugField(max_length=255, null=False, blank=False, unique=True)


# 分署，北部分署、中部分署、訓練測考中心
class Branch(Business):
    superior = models.ForeignKey(Service, on_delete=models.PROTECT)


# 室，人事室、主計室(有隸屬海巡署或是各分署)
class Office(models.Model):
    service_superior = models.ForeignKey(Service, on_delete=models.PROTECT, null=True)
    branch_superior = models.ForeignKey(Branch, on_delete=models.PROTECT, null=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    slug = models.SlugField(max_length=255, null=False, blank=False, unique=True)


# 科，巡防科、檢管科
class Section(models.Model):
    superior = models.ForeignKey(Branch, on_delete=models.PROTECT)
    name = models.CharField(max_length=50, null=False, blank=False)
    slug = models.SlugField(max_length=255, null=False, blank=False, unique=True)


# 第一巡防區、第二巡防區
class PatrolAreaCommand(models.Model):
    business_superior = models.ForeignKey(Service, on_delete=models.PROTECT)
    duty_superior = models.ForeignKey(Branch, on_delete=models.PROTECT)
    name = models.CharField(max_length=50, null=False, blank=False)
    slug = models.SlugField(max_length=255, null=False, blank=False, unique=True)


class DutyUnit(models.Model):
    business_superior = models.ForeignKey(Branch, on_delete=models.PROTECT)
    duty_superior = models.ForeignKey(PatrolAreaCommand, on_delete=models.PROTECT)
    name = models.CharField(max_length=50, null=False, blank=False)
    slug = models.SlugField(max_length=255, null=False, blank=False, unique=True)


# 岸巡隊
class CoastPatrolCorps(DutyUnit):
    pass


# 海巡隊
class OffshoreFlotilla(DutyUnit):
    pass


# 查緝隊
class ReconnaissanceBrigade(DutyUnit):
    pass


# 指揮部，目前只有東南沙分署有
class Command(models.Model):
    superior = models.ForeignKey(Branch, on_delete=models.PROTECT)
    name = models.CharField(max_length=50, null=False, blank=False)
    slug = models.SlugField(max_length=255, null=False, blank=False, unique=True)


# 勤務指揮中心
class AssignmentCommandCenter(Command):
    pass


# 勤務中隊、學員中隊
class Company(Command):
    pass


# 巡邏站
class Station(models.Model):
    business_superior = models.ForeignKey(Branch, on_delete=models.PROTECT)
    duty_superior = models.ForeignKey(Company, on_delete=models.PROTECT)
    name = models.CharField(max_length=50, null=False, blank=False)
    slug = models.SlugField(max_length=255, null=False, blank=False, unique=True)
