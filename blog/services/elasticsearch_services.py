import asyncio
from blog.models import Comment
from elasticsearch_dsl import Index, connections


class ElasticsearchServices:

  def __get_client(self):
    return connections.create_connection(hosts=['localhost'])

  def add_index_comment(self, comment):
    client = self.__get_client()
    #INDEX_NAME = "comment"
    #my_index = Index(INDEX_NAME, using=client)
    #my_index.settings(number_of_shards=1, number_of_replicas=1)
    #my_index.create()
    comment.save_elasticsearch_entity(client)



#services = ElasticsearchAsyncServices()
#c = Comment(body="Meu corpo", author="Meu autor")
#services.add_index_comment(c)