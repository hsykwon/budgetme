import webapp2
import jinja2
import os

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        main_template = env.get_template('mainPage.html')
        self.response.out.write(main_template.render())
    def post(self):
        complete_template = env.get_template('resultsPage.html')
        template_variables = {
            'income':self.request.get('income'),
            'budget':self.request.get("budget"),
            }
        self.response.out.write(complete_template.render(template_variables))

app = webapp2.WSGIApplication([
 ('/', MainPageHandler),
], debug=True)
