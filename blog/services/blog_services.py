from blog.models import Category, Post
from blog.models.elasticsearch import CommentElastic, PostElastic
from django.db import transaction
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Q
import asyncio


elasticsearch_alias = 'local'

class BlogServices:

    @transaction.atomic
    def insert_post(self, post, category_ids):
        selected_categories = Category.objects.filter(pk__in=category_ids)
        post.save()
        for s in selected_categories:
            post.categories.add(s)
        PostElastic.init(using=elasticsearch_alias)
        elastic = PostElastic(id=post.pk, title=post.title, body=post.body)
        elastic.meta.id=post.pk
        elastic.save(using=elasticsearch_alias)
        for s in selected_categories:
            elastic.add_category(s)


    @transaction.atomic
    def add_comment(self, comment):
        comment.save()
        elastic = PostElastic.get(id=comment.post.pk, using=elasticsearch_alias)
        elastic.add_comment(comment)


    def search(self, term):
        s = PostElastic.search(using=elasticsearch_alias)
        queries = [
            Q("multi_match", query=term, fields=["body", "title"]),
            #Q("match", title=term),
            #Q("match", body=term),
            Q("nested", path="categories", query=Q("match", categories__name=term)),
            Q("nested", path="comments", query=Q("match", comments__body=term)),
            Q("nested", path="comments", query=Q("match", comments__author=term))
        ]
        s.query = Q('bool', should=queries)
        print(s.to_dict())
        response = s.execute()
        ret = []
        if response.success():
            for hit in s:
                ret.append(Post.objects.get(pk=hit.id))
        return ret


    #@transaction.atomic
    #def add_category(self):
    #    c = Category(name="My category")
    #    c.save()
    #    raise Exception("TESTE")


    #def add_category_partial_non_atomic(self):
    #    with transaction.atomic():
    #        c = Category(name="My category - atomic part")
    #        c.save()