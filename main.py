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
        template = jinja_environment.get_tempate('signIn.html')
        user = users.get_current_user()
        if user:
            greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
                (user.nickname(), users.create_logout_url('/')))
        else:
            greeting = ('<a href="%s">Sign in or register</a>.' %
                users.create_login_url('/'))

        self.response.out.write('<html><body>%s</body></html>' % greeting)

app = webapp2.WSGIApplication([
 ('/', MainPageHandler),
 ('/login', LoginHandler)
], debug=True)
