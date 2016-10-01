import webapp2
import jinja2
import os
from google.appengine.api import users

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        main_template = env.get_template('mainPage.html')
        self.response.out.write(main_template.render())
    def post(self):
        complete_template = env.get_template('mainPage.html')
        # template_variables = {
        #     'budget_name':self.request.get("budget_name"),
        #     'budget_spent':self.request.get("budget_spent"),
        #     'income':self.request.get("income"),
        #     'budget':self.request.get("budget"),
        #     'spendings':self.request.get("spendings"),
        #     }
        # self.response.out.write(complete_template.render(template_variables))
        income_main = self.request.get("income")
        if income_main != "":
            income_total = income_total + income_main
            income_temp = income_total
            income_main = income_temp
        budget_main = self.request.get("budget")
        if budget_main != "":
            budget_total = budget_total + budget_main
            budget_temp = budget_total
            budget_main = budget_temp
        spendings_main = self.request.get("spendings")
        if spendings_main != "":
            spendings_total = spendings_total + spendings_main
            spendings_temp = spendings_total
            spendings_main = spendings_temp
        template_variables = {
            'income':self.request.get("income"),
            'budget':self.request.get("budget"),
            'spendings':self.request.get("spendings"),
        }
        self.response.out.write(complete_template.render(template_variables))


class LoginHandler(webapp2.RequestHandler):
    # def get(self):
    #     user = users.get_current_user()
    #     if user:
    #         main_template = env.get_template('mainPage.html')
    #         self.response.out.write(main_template.render())
    #         # greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
    #         #     (user.nickname(), users.create_logout_url('/')))
    #     else:
    #         greeting = ('<a href="%s">Sign in or register</a>.' %
    #             users.create_login_url('/'))
    #
    #     self.response.out.write('<html><body>%s</body></html>' % greeting)

    def get(self):
        user = users.get_current_user()
        template = env.get_template('mainPage.html')
        if user:
            self.response.out.write(template.render())
        else:
            template = env.get_template('signIn.html')
            greeting = ('<a href="%s"></a>' % users.create_login_url('/'))
            self.response.out.write('<html><body>%s</body></html>' % greeting)
            variables = {
                "login" : users.create_login_url('/')
            }
            self.response.out.write(template.render(variables))

class signOutHandler(webapp2.RequestHandler):
    def get(self):
        signouturl = users.create_logout_url('/')
        self.redirect(signouturl)

app = webapp2.WSGIApplication([
 ('/main', MainPageHandler),
 ('/', LoginHandler),
 ('/signOutHandler', signOutHandler),
], debug=True)
