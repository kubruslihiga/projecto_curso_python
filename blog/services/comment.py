from blog.models import Category
from django.db import transaction


class CommentServices:

  @transaction.atomic
  def add_category(self):
    c = Category(name="My category")
    c.save()
    raise Exception("TESTE")


  def add_category_partial_non_atomic(self):
    try:
      with transaction.atomic():
        c = Category(name="My category - atomic part")
        c.save()
        raise Exception("error")
    except Exception as e:
      print(e)
  
    c = Category(name="My category - non atomic part")
    c.save()
    raise Exception("TESTE")