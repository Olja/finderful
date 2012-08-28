import cgi
import webapp2
from google.appengine.ext.webapp import template
import django.core.handlers.wsgi

from random import Random


class Author(object): 
   pass

class MainPage(webapp2.RequestHandler):
    def get(self):
        filled_template = template.render("template_for_main_page.html", None)
        self.response.out.write(filled_template)
        

class QueryPage(webapp2.RequestHandler):
  def post(self):
    content = self.request.get("content")
    # Fake processing.
    author_list = []
    name_and_score = {}
    for i in range(10):
       random_author = Author()

       first_name = Random().choice((
          'Albert',
          'Robert',
          'Terry',
          'Monica',
          'Tony',
          'Edward',
          'Miranda',
          'Lucy',
       ))
       last_name = Random().choice((
          'Ward',
          'Johnson',
          'Yi',
          'Li',
          'Smith',
          'Charles',
          'Dreyfuss-Aiden',
          'Dylan',
       ))
       random_author.score = Random().random()
       random_author.name = first_name + ' ' + last_name

       author_list.append(random_author)

    def get_score(author):
       return author.score
    sorted_list = sorted(author_list, key=get_score, reverse=True)
    template_values = {
       'author_list': sorted_list,
       'maximal_score': sorted_list[0].score,
    }
    filled_template = template.render("template_query_page.html", template_values)
    self.response.out.write(filled_template)

  def get(self):
    self.redirect('/')

app = webapp2.WSGIApplication([
  ('/', MainPage),
  ('/query', QueryPage),
])
