from datetime import datetime
from blog.models import Post
from elasticsearch_dsl import Document, Text, Long, InnerDoc, Nested, Date


class CategoryElastic(InnerDoc):
    name = Text()


class CommentElastic(InnerDoc):
    body = Text(analyzer='snowball')
    author = Text()
    created_on = Date()


class PostElastic(Document):
    id = Long(required=True)
    title = Text()
    body = Text(analyzer='snowball')
    categories = Nested(CategoryElastic)
    comments = Nested(CommentElastic)

    class Index:
        name = 'post'
        settings = {
            "number_of_shards": 1,
        }

    def add_comment(self, comment):
        c = CommentElastic(body=comment.body, author=comment.author, created_on=datetime.now())
        self.comments.append(c)
        self.save(using='local')

    def add_category(self, category):
        c = CategoryElastic(name=category.name)
        self.categories.append(c)
        self.save(using='local')

    def save(self, **kwargs):
        return super(PostElastic, self).save(**kwargs)