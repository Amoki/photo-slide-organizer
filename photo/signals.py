from django.db.models.signals import post_save
from django.dispatch import receiver
from photo.models import Diapo, MotCle
from slugify import slugify


@receiver(post_save, sender=Diapo)
def update_word_list(sender, instance, created, **kwargs):
    if created:
        words = instance.description.split(' ')
        existing_words = MotCle.objects.all().values_list('mot', flat=True)
        for slugged_word in [slugify(word) for word in words]:
            if slugged_word not in existing_words:
                print(slugged_word)
                print(existing_words)
                mc = MotCle(mot=slugged_word)
                mc.save()
            else:
                mc = MotCle.objects.get(mot=slugged_word)
            instance.words.add(mc)
