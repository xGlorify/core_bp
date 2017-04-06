from flask import render_template, request, session, url_for, redirect, flash, Blueprint, g
from core import app, db, current_user
from flask.ext.login import login_required
from models import *
from forms import CreateTasksForm
from assets.models import *

tasks_blueprint = Blueprint('tasks', __name__, template_folder = 'templates', static_folder='./static')

@tasks_blueprint.route('/create_tasks', methods=['GET', 'POST'])
@login_required
def create_tasks():
	form = CreateTasksForm()
	form.asset_tag.choices = [(tc.id, tc.asset_tag) for tc in Motor.query.order_by('id')]
	if request.method == 'POST':
		if form.validate_on_submit():
			try:
				asset_tag = form.asset_tag.data
				asset = Motor.query.filter_by(id = asset_tag).first_or_404()
				title_input = form.task_title.data
				description_input = form.description.data
				filename = form.report.data.filename
				if form.report.data:
					form.report.data.save('assets/static/reports/' + str(asset_tag) + '_' + filename)
					report_input = '/assets/static/reports/' + str(asset_tag) + '_' + filename
					task = Task(title_input, description_input, report_input)
					asset.asset_tasks.append(task)
					current_user.user_tasks.append(task)
					db.session.add(task)
					db.session.commit()
					flash('Task successfully assigned with report attached.')
				else:
					report_input = None
					task = Task(title_input, description_input, report_input)
					asset.asset_tasks.append(task)
					current_user.user_tasks.append(task)
					db.session.add(task)
					db.session.commit()
					flash('Task successfully assigned.')
			except Exception as e:
				flash(e)
                db.session.rollback()
	return render_template('create_task.html', form = form)

@tasks_blueprint.route('/<task_id>')
@login_required
def task_profile(task_id):
	task = Task.query.filter_by(task_id = task_id).first_or_404()
	return render_template('taskprofile.html', task=task)