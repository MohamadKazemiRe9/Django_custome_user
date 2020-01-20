from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager , PermissionsMixin
from django.utils.translation import gettext as _

class MyUserManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError("آدرس ایمیل را باید وارد کنید")
        if not username:
            raise ValueError("نام کاربری را باید وارد کنید")
        user = self.model(
            email=self.normalize_email(email),
            username = username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,username,password=None):
        user = self.create_user(
            email,
            username,
            password=password,
        )
        user.is_admin = True
        user.is_superuser=True
        user.is_staff = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser , PermissionsMixin):
    email = models.EmailField(max_length=100,unique=True,verbose_name="ایمیل")
    username = models.CharField(max_length=40,unique=True,verbose_name="نام کاربری")
    signing_date = models.DateField(verbose_name="تاریخ ثبت نام",auto_now_add=True)
    last_login_date = models.DateField(verbose_name="تاریخ آخرین ورود",auto_now=True)
    is_admin = models.BooleanField(_("وضعیت مدیریت"),default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(_("وضعیت کارمندی"),default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(verbose_name="نام",max_length=50)
    last_name = models.CharField(verbose_name="نام خانوادگی",max_length=70)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username",]

    objects = MyUserManager()

    def __str__(self):
        return self.email+" - "+self.username

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'