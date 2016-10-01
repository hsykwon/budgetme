import webapp2
import jinja2
import os
from google.appengine.api import users


env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class LoginHandler(webapp2.RequestHandler):

    global income_total
    income_total = []
    global budget_total
    budget_total = []
    global spendings_total
    spendings_total = []

    def get(self):
        user = users.get_current_user()
        template = env.get_template('mainPage.html')
        print "hi"
        if user:
            income_main = self.request.get("income")
            if income_main != "":
                income_main = int(income_main)
                # income_temp = income_total
                # income_total = income_temp + income_main
                # #income_temp = income_total
                # income_main = income_total
                income_total.append(income_main)
            budget_main = self.request.get("budget")
            if budget_main != "":
                budget_main = int(budget_main)
                # budget_temp = budget_total
                # budget_total = budget_temp + budget_main
                # #budget_temp = budget_total
                # budget_main = budget_total
                budget_total.append(budget_main)
            spendings_main = self.request.get("spendings")
            if spendings_main != "":
                spendings_main = int(spendings_main)
                # spendings_temp = spendings_total
                # spendings_total = spendings_temp + spendings_main
                # #spendings_temp = spendings_total
                # spendings_main = spendings_total
                spendings_total.append(spendings_main)
            template_variables = {
                'income_blah': sum(income_total),
                'budget_blah': sum(budget_total),
                'spendings_blah': sum(spendings_total),
            }
            complete_template = env.get_template('mainPage.html')
            self.response.out.write(complete_template.render(template_variables))
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
 #('/main', MainPageHandler),
 ('/', LoginHandler),
 ('/signOutHandler', signOutHandler),
], debug=True)
