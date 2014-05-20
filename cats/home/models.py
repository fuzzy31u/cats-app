# -*- coding: utf-8 -*-
from types import NoneType
from django.db import models

# Create your models here.
from instagram import InstagramAPI


class Item(models.Model):
    instagram_id = models.BigIntegerField()
    link = models.CharField(max_length=255)
    caption = models.CharField(max_length=255, null=True)
    image_url = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    user_profile_url = models.CharField(max_length=255, null=True)
    create_time = models.DateTimeField()

# Instagram
def get_list():
    api = InstagramAPI(client_id='f7a905471d5c4f29a8f6797c83499bb6')
    recent_media, next = api.tag_recent_media(tag_name=u'捨て猫')

    item_list = []
    for media in recent_media:
        item = Item()
        item.instagram_id = media.id
        item.link = media.link
        if(type(media.caption) is not NoneType):
            item.caption = media.caption.text
        item.image_url = media.images['standard_resolution'].url
        # item.image_url = media.images['thumbnail'].url
        item.user_name = media.user.username
        item.user_profile_url = media.user.profile_picture
        item.create_time = media.created_time
        item_list.append(item)

    return item_list
