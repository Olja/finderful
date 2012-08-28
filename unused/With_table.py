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

       #ordered_dictionary = dict(zip(score, result))  
       #my_sorted_list = sorted(ordered_dictionary.items(), reverse=True)#orders by alphabet by names
       #my_ordered_list_of_scores = sorted(ordered_dictionary.keys(), reverse=True) #this orders by names!I don't need it
       #my_list_of_names_ordered_by_score = sorted(ordered_dictionary.values(), reverse=True)
    # Now result is a list of objects that you have to process.
    def get_score(author):
       return author.score
    sorted_list = sorted(author_list, key=get_score, reverse=True)
    self.response.out.write("""
          <html>
            <head>
              <title>I have my PhD!!!</title>
              <style type="text/css">
               span.score {
                 color:red;
                 font-weight:bold;
               }
	       span.name {
		 color:green;
		 font-style:italic;font-weigt:italic
               }
              </style>
            </head>
            <body>
              The list of the best scores and authors is the following:
              <ol><table border cellspacing=0 cellpadding=5>
                                    <caption align bottom>
			               Table</caption>
				    <tr>
				      <th> </th>
				      <th>name</th>
				      <th>score</th>
				    </tr>
				    <tr align=center>
				      <th> position on the list</th>
				      <td> %s </td>
				      <td> %s </td>
                                    </tr>
				    </table>"""
for author in sorted_list: 
       self.response.out.write("""<li><span class="name"> %s: </span><span class="score">%s</span> </li>""" % (author.name, author.score))
			 	    </tr>
				  </table>""")
    
    self.response.out.write("""</ol></body></html>""")

  def get(self):
    self.redirect('/')


app = webapp2.WSGIApplication([
  ('/', MainPage),
  ('/query', QueryPage),
])
