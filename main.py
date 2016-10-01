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
            'budget_name':self.request.get("budget_name"),
            'budget_spent':self.request.get("budget_spent"),
            }
        self.response.out.write(complete_template.render(template_variables))

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        login_template = env.get_template('login.html')
        self.response.out.write(login_template.render())

app = webapp2.WSGIApplication([
 ('/', MainPageHandler),
 ('/login', LoginHandler)
], debug=True)
