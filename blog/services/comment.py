from blog.models import Category
from blog.models.elasticsearch import CommentElastic
from django.db import transaction
from elasticsearch_dsl.connections import connections
import asyncio

class CommentServices:

    