# -*- coding: utf-8 -*-
import json
import re
from types import NoneType
from django.db import models
from django.core import serializers

# Create your models here.
from instagram import InstagramAPI
from simplejson import JSONEncoder

api = InstagramAPI(client_id='f7a905471d5c4f29a8f6797c83499bb6')

class Item(models.Model):
    instagram_id = models.BigIntegerField()
    link = models.CharField(max_length=255)
    caption = models.CharField(max_length=255, null=True)
    image_url = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    user_profile_url = models.CharField(max_length=255, null=True)
    create_time = models.DateTimeField()

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, ensure_ascii=False, indent=4)

def get_list():

    recent_media, next = api.tag_recent_media(tag_name=u'捨て猫')
    item_list = []
    item_list = request_instagram(recent_media, item_list)

    return item_list, next

def get_json(next):

    r = re.compile("max_tag_id=")
    m = r.search(next)
    max_id = next[m.end():len(next)]

    print max_id

    recent_media, next = api.tag_recent_media(tag_name=u'捨て猫', max_id=max_id)
    item_list = []
    item_list = request_instagram(recent_media, item_list)

    json_item_list = []
    for item in item_list:
        json_item_list.append(item.to_json())

    return json_item_list, next

def request_instagram(recent_media, item_list):
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
        try:
            item.create_time = media.created_time.strftime('%Y/%m/%d %H:%M:%S')
        except Exception as e:
            print str(e)
            item.create_time = ''
        item_list.append(item)

    return item_list