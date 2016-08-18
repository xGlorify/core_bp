from flask import render_template, request, session, url_for, redirect, flash, Blueprint, g
from core import app, db
from flask.ext.login import login_required
from models import *
from forms import CreateTasksForm, AssignTasksForm
from assets.models import *

tasks_blueprint = Blueprint('tasks', __name__, template_folder = 'templates', static_folder='./static')

@tasks_blueprint.route('/create_tasks', methods=['GET', 'POST'])
@login_required
def create_tasks():
	form = CreateTasksForm()
	if request.method == 'POST':
		if form.validate_on_submit():
			try:
				title_input = form.task_title.data
				description_input = form.description.data
				pass_to_db = Tasks(title_input, description_input)
				db.session.add(pass_to_db)
				db.session.commit()
			except Exception as e:
				flash(e)
                db.session.rollback()
	return render_template('create_task.html', form = form)

@tasks_blueprint.route('/assign_tasks', methods=['GET', 'POST'])
@login_required
def assign_tasks():
	form = AssignTasksForm()
	form.task_title.choices = [(tc.task_id, tc.task_title) for tc in Tasks.query.order_by('task_id')]
	if request.method == 'POST':
		if form.validate_on_submit():
			try:
				asset_tag = form.asset_tag.data
				asset = Motor.query.filter_by(asset_tag = asset_tag).first_or_404()
				task_id = form.task_title.data
				task = Tasks.query.filter_by(task_id = task_id).first_or_404()
				task.asset_tasks.append(asset)
				db.session.add(task)
				db.session.commit()
				flash('Task successfully assigned.')
			except Exception as e:
				flash(e)
				db.session.rollback()
	return render_template('assign_tasks.html', form=form)

