from django.db.models.signals import post_delete
from django.dispatch import receiver

from professor.models import Professors
from student.models import Students
from tutor.models import Tutors
from manager.models import SchoolManagers

@receiver(post_delete,sender=Professors)
@receiver(post_delete,sender=Students)
@receiver(post_delete,sender=Tutors)
@receiver(post_delete,sender=SchoolManagers)
def delete_user_after_delete_school_entity(sender,instance,**kwargs):
    if instance.user:
        instance.user.delete()