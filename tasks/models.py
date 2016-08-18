from core import db, current_user
from assets.models import *

link_table = db.Table('link_table',
	db.Column('id', db.Integer, primary_key=True),
    db.Column('asset_id', db.Integer, db.ForeignKey('motor.id')),
    db.Column('task_id', db.Integer, db.ForeignKey('tasks.task_id'))
    )

class Tasks(db.Model):
	task_id = db.Column(db.Integer, primary_key=True)
	task_title = db.Column('Task Title', db.String(50), unique=True, nullable = False)
	description = db.Column('Description', db.Text, nullable = False)
	#assets = db.relationship('Motor', secondary = link_table, backref = db.backref('asset'), lazy = 'dynamic')

	def __init__(self, task_title, description):
		self.task_title = task_title
		self.description = description
		#self.assets = assets