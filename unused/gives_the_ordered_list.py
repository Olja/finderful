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
       my_sorted_list = sorted(ordered_dictionary.items(), reverse=True)#orders by alphabet by names
       #my_ordered_list_of_scores = sorted(ordered_dictionary.keys(), reverse=True) #this orders by names!I don't need it
       #my_list_of_names_ordered_by_score = sorted(ordered_dictionary.values(), reverse=True)
    # Now result is a list of objects that you have to process.
    self.response.out.write("""
          <html>
            <head>
              <style type="text/css">
               <!--
               p {
                 color:red
                 font-weight:bold
               }
               -->
              </style>
            </head>
            <body>
              The list of the best scores and authors is the following:
            </body>
          </html>""") 

    self.response.out.write("""<ol>
                                 <li> %s </li> 
                                 <li> %s </li>
				 <li> %s </li>
				 <li> %s </li>
				 <li> %s </li>
				 <li> %s </li>
				 <li> %s </li>
				 <li> %s </li>
				 <li> %s </li>
				 <li> %s </li>
                                 </ol>""" % (my_sorted_list[0], my_sorted_list[1], my_sorted_list[2], my_sorted_list[3], my_sorted_list[4], my_sorted_list[5], my_sorted_list[6], my_sorted_list[7], my_sorted_list[8], my_sorted_list[9]))

  def get(self):
    self.redirect('/')


app = webapp2.WSGIApplication([
  ('/', MainPage),
  ('/query', QueryPage),
])
