from types import NoneType
from django.db import models

# Create your models here.
from instagram import InstagramAPI
from cats.home.models import Item


def get_item(instagram_id):
    api = InstagramAPI(client_id='f7a905471d5c4f29a8f6797c83499bb6')
    media = api.media(instagram_id)

    item = Item()
    item.link = media.link
    if(type(media.caption) is not NoneType):
        item.caption = media.caption.text
    item.image_url = media.images['standard_resolution'].url
    item.thumbnail_url = media.images['thumbnail'].url
    item.user_name = media.user.username
    item.user_profile_url = media.user.profile_picture
    item.create_time = media.created_time

    return item

