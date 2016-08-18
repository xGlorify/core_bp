from flask.ext.wtf import Form
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired
from models import Tasks

class CreateTasksForm(Form):
    task_title = StringField('task_title', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])

class AssignTasksForm(Form):
    asset_tag = StringField('asset_tag', validators=[DataRequired()])
    task_title = SelectField('task_title', coerce=int, validators=[DataRequired()])