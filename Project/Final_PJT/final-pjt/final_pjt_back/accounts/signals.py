from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# from allauth.socialaccount.models import SocialAccount
# from allauth.socialaccount.signals import pre_social_login, social_account_added
from django.conf import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# @receiver(social_account_added)
# def create_auth_token_for_social(sender, request, sociallogin, **kwargs):
#     user = sociallogin.user
#     Token.objects.get_or_create(user=user)


# @receiver(social_account_added)
# def update_profile_on_social_login(sender, request, sociallogin, **kwargs):
#     user = sociallogin.user
#     extra_data = sociallogin.account.extra_data
#     properties = extra_data.get('properties', {})
#     nickname = properties.get('nickname', user.username)  # 카카오에서 제공하는 닉네임 사용
#     user.nickname = '임시닉네임'
#     user.save()

# @receiver(post_save, sender=SocialAccount)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         User.objects.create(user=instance.user)