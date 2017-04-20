from core import db, current_user
from assets.models import *
from users.models import *
from datetime import datetime

link_table = db.Table('link_table',
	db.Column('id', db.Integer, primary_key=True),
    db.Column('asset_id', db.Integer, db.ForeignKey('motor.id')),
    db.Column('task_id', db.Integer, db.ForeignKey('task.task_id')),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
    )

class Task(db.Model):
	task_id = db.Column(db.Integer, primary_key=True)
	task_title = db.Column('Title', db.String(25), nullable = False)
	description = db.Column('Description', db.String(150), nullable = False)
	reports = db.Column('Reports', db.String(100))
	status = db.Column('Status', db.String(25))
	user = db.Column('User', db.String(50))
	date = db.Column(db.DateTime())
	assets = db.relationship('Motor', secondary = link_table, backref = db.backref('asset_tasks'), lazy = 'dynamic')
	user_backref = db.relationship('User', secondary = link_table, backref = db.backref('user_tasks'), lazy = 'dynamic')

	def __init__(self, task_title, description, reports, status, user=None, date=None):
		self.task_title = task_title
		self.description = description
		self.reports = reports
		self.status = status
		self.user = str(current_user.first_name) + " " + str(current_user.last_name)
		self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")