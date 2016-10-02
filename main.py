import webapp2
import jinja2
import os
from google.appengine.api import users

global income_total
income_total = []
global budget_total
budget_total = []
global spendings_total
spendings_total = []
global savings_total
savings_total = []
global goals_total
goals_total = [" "]

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        main_template = env.get_template('mainPage.html')
        self.response.write(main_template.render())
    def post(self):
        complete_template = env.get_template('mainPage.html')
        template_variables = {
             'income':self.request.get("income"),
             'budget':self.request.get("budget"),
             'spendings':self.request.get("spendings"),
             }
        self.response.out.write(complete_template.render(template_variables))

class LoginHandler(webapp2.RequestHandler):
    def get(self):

        user = users.get_current_user()
        template = env.get_template('mainPage.html')
        if user:
            income_main = self.request.get("income")
            if income_main != "":
                income_main = int(income_main)
                income_total.append(income_main)
            budget_main = self.request.get("budget")

            if budget_main != "":
                budget_main = int(budget_main)
                budget_total.append(budget_main)
            spendings_main = self.request.get("spendings")

            if spendings_main != "":
                spendings_main = int(spendings_main)
                spendings_total.append(spendings_main)

            if budget_main != "" and spendings_main != "" and income_main != "":
                savings_main = int(budget_main)-int(spendings_main)+int(income_main)
                savings_total.append(savings_main)
            goals_main = self.request.get("goals")

            if goals_main != "":
                goals_main = self.request.get("goals")
                goals_total[0] = self.request.get("goals")
            elif goals_main == "":
                goals_main = goals_total[0]
            template_variables = {
                'income_blah': sum(income_total),
                'budget_blah': sum(budget_total),
                'spendings_blah': sum(spendings_total),
                'savings_blah': sum(savings_total),
                'goals_blah': goals_main,
            }
            complete_template = env.get_template('mainPage.html')
            self.response.out.write(complete_template.render(template_variables))
        else:
            template = env.get_template('login.html')
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
 #('/main', MainPageHandler),
 ('/', LoginHandler),
 ('/signOutHandler', signOutHandler),
], debug=True)
