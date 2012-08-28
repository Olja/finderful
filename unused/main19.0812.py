import cgi
import webapp2

from random import Random

class Author(object): 
   pass

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("""
          <html>
            <body>
              <form action="/query" method="post">
                <p align="center">
                <div><textarea name="content" rows="3" cols="60"></textarea></div>
                <div><input type="submit" value="Send the keyword"></div>
                </p>
              </form>
            </body>
          </html>""")

class QueryPage(webapp2.RequestHandler):
  def post(self):
    content = self.request.get("content")
    # do something with 'content'.
    # Fake processing.
    result = list()
    score = list()
    name_and_score = {}
    for i in range(10):
       random_author = Author()
       random_author.score = Random().random()
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
       random_author.name = first_name + ' ' + last_name
       result.append(random_author.name)
       score.append(random_author.score)
       ordered_dictionary = dict(zip(score, result))  
       sorted_dictionary = sorted(ordered_dictionary.items(), reverse=True) 
    # Now result is a list of objects that you have to process.
    self.response.out.write("""
          <html>
            <head>
              <style type="text/css">
               <!--
               p {color:red}
               -->
              </style>
            </head>
            <body>
              The list of the best scores and authors is the following:<span><strong><b><p><ol><li> %s ></ol><p></b></strong></span>
            </body>
          </html>""" % sorted_dictionary)

  def get(self):
    self.redirect('/')


app = webapp2.WSGIApplication([
  ('/', MainPage),
  ('/query', QueryPage),
])
