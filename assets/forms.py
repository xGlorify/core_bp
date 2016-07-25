from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, FloatField, FileField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Optional

class SubmitAssetForm(Form):
    asset_tag = StringField('asset_tag', validators=[DataRequired()])
    serial = StringField('serial', validators=[Optional()])
    manufacturer = StringField('manufacturer', validators=[DataRequired()])
    model_number = StringField('model_number', validators=[DataRequired()])
    current = StringField('current', validators=[DataRequired()])
    frequency_choices = [('60', '60'), ('50', '50'), ('50-60', '50-60')]
    frequency = SelectField('frequency', choices = frequency_choices, validators=[DataRequired()])
    voltage_choices = [('115-230', '115-230'), ('230', '230'), ('230-460', '230-460'), ('460', '460'), ('380-500', '380-500'), ('575', '575')]
    voltage = SelectField('voltage', choices = voltage_choices, validators=[DataRequired()])
    secondary_voltage = FloatField('secondary_voltage', validators=[Optional()])
    power_factor = FloatField('power_factor', validators=[Optional()])
    efficiency = FloatField('efficiency', validators=[Optional()])
    horsepower = FloatField('horsepower', validators=[DataRequired()])
    #rpm_choices = [('1800', '1800'), ('900', '900'), ('1200', '1200'), ('3600', '3600')]
    rpm = StringField('rpm',  validators=[DataRequired()])
    design_choices = [('B', 'B'), ('A', 'A'), ('C', 'C'), ('D', 'D')]
    design = SelectField('design', choices = design_choices, validators=[DataRequired()])
    frame = StringField('frame', validators=[Optional()])
    enclosure_choices = [('TEFC', 'TEFC'), ('ODP', 'ODP'), ('TENV', 'TENV'), ('TEBC', 'TEBC')]
    enclosure = SelectField('enclosure', choices = enclosure_choices, validators=[DataRequired()])
    attachments = TextAreaField('attachments', validators=[Optional()])
    location = StringField('location', validators=[Optional()])
    status_choices = [('Live', 'Live'), ('Stores', 'Stores'), ('Repair', 'Repair')]
    status = SelectField('status', choices = status_choices, validators=[DataRequired()])
    picture = FileField('img', validators=[Optional()])

class EditAssetForm(Form):
    asset_tag = StringField('asset_tag', validators=[Optional()])
    serial = StringField('serial', validators=[Optional()])
    manufacturer = StringField('manufacturer', validators=[Optional()])
    model_number = StringField('model_number', validators=[Optional()])
    current = StringField('current', validators=[Optional()])
    frequency_choices = [('', ''), ('60', '60'), ('50', '50'), ('50-60', '50-60')]
    frequency = SelectField('frequency', choices = frequency_choices, validators=[Optional()])
    voltage_choices = [('', ''), ('115-230', '115-230'), ('230', '230'), ('230-460', '230-460'), ('460', '460'), ('380-500', '380-500'), ('380-380', '380-380'), ('575', '575')]
    voltage = SelectField('voltage', choices = voltage_choices, validators=[Optional()])
    secondary_voltage = FloatField('secondary_voltage', validators=[Optional()])
    power_factor = FloatField('power_factor', validators=[Optional()])
    efficiency = FloatField('efficiency', validators=[Optional()])
    horsepower = FloatField('horsepower', validators=[Optional()])
    #rpm_choices = [('1800', '1800'), ('900', '900'), ('1200', '1200'), ('3600', '3600')]
    rpm = StringField('rpm', validators=[Optional()])
    design_choices = [('', ''), ('B', 'B'), ('A', 'A'), ('C', 'C'), ('D', 'D')]
    design = SelectField('design', choices = design_choices, validators=[Optional()])
    frame = StringField('frame', validators=[Optional()])
    enclosure_choices = [('', ''), ('TEFC', 'TEFC'), ('ODP', 'ODP'), ('TENV', 'TENV'), ('TEBC', 'TEBC')]
    enclosure = SelectField('enclosure', choices = enclosure_choices, validators=[Optional()])
    attachments = TextAreaField('attachments', validators=[Optional()])
    location = StringField('location', validators=[Optional()])
    status_choices = [('', ''), ('Live', 'Live'), ('Stores', 'Stores'), ('Repair', 'Repair')]
    status = SelectField('status', choices = status_choices, validators=[Optional()])
    picture = FileField('img', validators=[Optional()])
    
class FilterAssetsForm(Form):
    asset_tag_search = StringField('asset_tag', validators=[Optional()])
    serial_search = StringField('serial', validators=[Optional()])
    manufacturer_search = StringField('manufacturer', validators=[Optional()])
    model_number_search = StringField('model_number', validators=[Optional()])
    current_search = StringField('current', validators=[Optional()])
    frequency_choices = [('', ''), ('60', '60'), ('50', '50'), ('50-60', '50-60')]
    frequency_search = SelectField('frequency', choices = frequency_choices, validators=[Optional()])
    voltage_choices = [('', ''), ('115-230', '115-230'), ('230', '230'), ('230-460', '230-460'), ('460', '460'), ('380-500', '380-500'), ('380-380', '380-380'), ('575', '575')]
    voltage_search = SelectField('voltage', choices = voltage_choices, validators=[Optional()])
    secondary_voltage_search = FloatField('secondary_voltage', validators=[Optional()])
    power_factor_search = FloatField('power_factor', validators=[Optional()])
    efficiency_search = FloatField('efficiency', validators=[Optional()])
    horsepower_search = FloatField('horsepower', validators=[Optional()])
    #rpm_choices = [('1800', '1800'), ('900', '900'), ('1200', '1200'), ('3600', '3600')]
    rpm_search = StringField('rpm', validators=[Optional()])
    design_choices = [('', ''), ('B', 'B'), ('A', 'A'), ('C', 'C'), ('D', 'D')]
    design_search = SelectField('design', choices = design_choices, validators=[Optional()])
    frame_search = StringField('frame', validators=[Optional()])
    enclosure_choices = [('', ''), ('TEFC', 'TEFC'), ('ODP', 'ODP'), ('TENV', 'TENV'), ('TEBC', 'TEBC')]
    enclosure_search = SelectField('enclosure', choices = enclosure_choices, validators=[Optional()])
    attachments_search = TextAreaField('attachments', validators=[Optional()])
    location_search = StringField('location', validators=[Optional()])
    status_choices = [('', ''), ('Live', 'Live'), ('Stores', 'Stores'), ('Repair', 'Repair')]
    status_search = SelectField('status', choices = status_choices, validators=[Optional()])
    
class SearchAssetTag(Form):
    asset_tag_search = StringField('asset_tag_search', validators=[DataRequired()])
