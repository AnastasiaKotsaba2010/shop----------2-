import flask, os
from flask_login import current_user

def contacts_render():
    if current_user.is_authenticated:
        return flask.render_template(
            template_name_or_list ='contacts.html', 
            is_auth = current_user.is_authenticated,
            name = current_user.name, 
            is_admin = current_user.is_admin
        )
    return flask.render_template(template_name_or_list ='contacts.html')

print(os.path.abspath(__file__))