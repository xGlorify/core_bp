from flask import render_template, request, session, url_for, redirect, flash, Blueprint, g
from core import app, db
from sqlalchemy.exc import IntegrityError
from forms import SubmitAssetForm, FilterAssetsForm
from flask.ext.login import login_required
from models import *

assets_blueprint = Blueprint('assets', __name__, template_folder = 'templates', static_folder='./static')

@assets_blueprint.route('/submitasset', methods=['GET', 'POST'])
@login_required
def submitasset():
    form = SubmitAssetForm() #Pass SubmitAssetForm model to form object.
    result_message = None
    if request.method == 'POST':
        if form.validate_on_submit():# Confirms if all requirements for the form are met (No empty fields in this case).
            try:
                asset_input = form.asset_tag.data #Form input for Asset Tag.
                manufacturer_input = form.manufacturer.data
                model_number_input = form.model_number.data
                current_input = form.current.data
                frequency_input = form.frequency.data
                voltage_input = form.voltage.data #Form input for voltage of corresponding asset.
                secondary_voltage_input = form.secondary_voltage.data #Form input for secondary voltage of corresponding asset.
                power_factor_input = form.power_factor.data
                efficiency_input = form.efficiency.data
                horsepower_input = form.horsepower.data #Form input for Horsepower of corresponding asset.
                rpm_input = form.rpm.data #Form input for RPM of corresponding asset.
                design_input = form.design.data
                frame_input = form.frame.data #Form input for Frame of corresponding asset.
                enclosure_input = form.enclosure.data #Form input for enclosure of corresponding asset.
                attachments_input = form.attachments.data #Form input for any attachments of corresponding asset.
                location_input = form.location.data
                status_input = form.status.data
                filename = form.picture.data.filename
                if form.picture.data:
                    form.picture.data.save('assets/static/img/' + str(asset_input) + '_' + filename)
                    picture_input = 'static/img/' + str(asset_input) + '_' + filename
                    pass_to_db = Motor(asset_input, manufacturer_input, model_number_input, current_input, frequency_input, voltage_input, secondary_voltage_input, 
                    power_factor_input, efficiency_input, horsepower_input, rpm_input, design_input, frame_input, enclosure_input, attachments_input, location_input, picture_input, status_input) #Convert form data to Motor model.
                    db.session.add(pass_to_db) #Add form data in Motor model to database.
                    db.session.commit() #Commit additions to database.
                    result_message = str(asset_input) + " successfully added to the database with photo."
                else:
                    picture_input = 'static/img/NoMotor_Core_No_Photo.png'
                    pass_to_db = Motor(asset_input, manufacturer_input, model_number_input, current_input, frequency_input, voltage_input, secondary_voltage_input, 
                    power_factor_input, efficiency_input, horsepower_input, rpm_input, design_input, frame_input, enclosure_input, attachments_input, location_input, picture_input, status_input)
                    db.session.add(pass_to_db)
                    db.session.commit()
                    result_message = str(asset_input) + " successfully added to the database."
            except Exception as e:
                    flash("This asset tag already exists in the database.")
                    result_message = e #Passes exception errors to e variable for development troubleshooting.
                    db.session.rollback() #Rolls back added / committed changes.

        else:
            result_message = "You must enter a value for all fields and only numbers for the Horsepower, Voltage, RPM and Secondary Voltage fields." # If a field is empty or missing data.
        return render_template('submitasset.html', result_message=result_message, form=form)
    return render_template('submitasset.html', form=form)


@assets_blueprint.route('/delasset', methods=['GET', 'POST'])
@login_required
def delasset():
    motor = Motor.query.filter_by(asset_tag=request.form["delete"]).first_or_404()
    db.session.delete(motor)
    db.session.commit()
    flash("Asset %s successfully deleted." % (motor.asset_tag))
    return redirect(url_for('assets.viewassets'))
    
@assets_blueprint.route('/viewassets', methods=['GET', 'POST'])
@login_required
def viewassets():
    assets = Motor.query.all() #Gives assets object all data in the Motor table.
    return render_template('viewassets.html', assets=assets)
    
@assets_blueprint.route('/filterassets', methods=['GET', 'POST'])
@login_required
def searchassets():
    form = FilterAssetsForm()
    results = None
    if request.method == "POST":
        if form.validate_on_submit():
            try:
                horsepower = form.horsepower_search.data
                voltage = form.voltage_search.data
                current = form.current_search.data
                rpm = form.rpm_search.data
                frame = form.frame_search.data
                secondary_voltage = form.secondary_voltage_search.data
                enclosure = form.enclosure_search.data
                attachments = form.attachments_search.data
                filter_data = {'horsepower' : horsepower, 'voltage' : voltage, 'current' : current, 'rpm' : rpm, 'frame' : frame, 
                'secondary_voltage' : secondary_voltage, 'enclosure' : enclosure, 'attachments' : attachments}
                filter_data = {key: value for (key, value) in filter_data.items()
               if value}
                results = Motor.query.filter_by(**filter_data).all()
            except Exception as e:  
                flash(e)
                db.session.rollback()
            return render_template('filterassets.html', form=form, results=results)
    return render_template('filterassets.html', form=form)

@assets_blueprint.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    results = None
    if request.method == 'POST':
        if g.headersearchform.validate_on_submit():
            try:
                asset_tag = g.headersearchform.asset_tag_search.data
                results = Motor.query.filter_by(asset_tag = asset_tag).first_or_404()
            except Exception as e:
                flash(e)
                db.session.rollback()
            return render_template('searchresults.html', results=results)
        else:
            flash("You must enter a value to search.")
    return render_template('searchresults.html')

@assets_blueprint.route('/<asset_tag>')
@login_required
def asset_profile(asset_tag):
    asset = Motor.query.filter_by(asset_tag = asset_tag).first_or_404()
    return render_template('asset_profile.html', asset=asset)

@assets_blueprint.route('/hotspare/<asset_tag>')
@login_required
def hotspare_search(asset_tag):
    asset = Motor.query.filter_by(asset_tag = asset_tag).first_or_404()
    frequency = asset.frequency
    current = asset.current
    voltage = asset.voltage
    horsepower = asset.horsepower
    filter_data = {'horsepower' : horsepower, 'frequency' : frequency, 'current' : current, 'voltage' : voltage}
    results = Motor.query.filter_by(**filter_data).all()
    return render_template('searchresults.html', results=results)
    
    
    
    
    