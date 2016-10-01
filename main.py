import webapp2
import jinja2
import os

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment( loader=jinja2.FileSystemLoader('templates'))

class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('mainPage.html')
        self.response.out.write(template.render())

routes = [
    ('/', MainPageHandler),
]
