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
       name = random_author.name
       number = random_author.score
       name_and_score[name]=[number] 
    # Now result is a list of objects that you have to process.
     
    self.response.out.write("""
          <html>
            <body>
              The list of the most competent authors and their scores for your keyword is %s 
            </body>
          </html>""" % name_and_score)
    
  def get(self):
    self.redirect('/')


app = webapp2.WSGIApplication([
  ('/', MainPage),
  ('/query', QueryPage),
])
