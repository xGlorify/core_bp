from flask.ext.wtf import Form
from wtforms import StringField, SelectField, FileField, TextField
from wtforms.validators import DataRequired, Optional
from models import Task

class CreateTasksForm(Form):
	asset_tag = SelectField('asset_tag', coerce=int, validators=[DataRequired()])
	task_title = SelectField('task_title', choices=[('Shaft Rotation', 'Shaft Rotation'), ('Vibration Analysis', 'Vibration Analysis')], validators=[DataRequired()])
	description = TextField('description', validators=[DataRequired()])
	report = FileField('report', validators=[Optional()])

#class AssignTasksForm(Form):
#    asset_tag = StringField('asset_tag', validators=[DataRequired()])
#    task_title = SelectField('task_title', coerce=int, validators=[DataRequired()])