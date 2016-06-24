from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, FloatField
from wtforms.validators import DataRequired, Optional

class SubmitAssetForm(Form):
    asset_tag = StringField('asset_tag', validators=[DataRequired()])
    manufacturer = StringField('manufacturer', validators=[DataRequired()])
    model_number = IntegerField('model_number', validators=[DataRequired()])
    current = IntegerField('current', validators=[DataRequired()])
    frequency = IntegerField('frequency', validators=[DataRequired()])
    voltage = IntegerField('voltage', validators=[DataRequired()])
    secondary_voltage = FloatField('secondary_voltage', validators=[Optional()])
    power_factor = IntegerField('power_factor', validators=[DataRequired()])
    efficiency = IntegerField('efficiency', validators=[DataRequired()])
    horsepower = IntegerField('horsepower', validators=[DataRequired()])
    rpm = IntegerField('rpm', validators=[DataRequired()])
    design = StringField('design', validators=[DataRequired()])
    frame = StringField('frame', validators=[DataRequired()])
    enclosure = StringField('enclosure', validators=[DataRequired()])
    attachments = StringField('attachments', validators=[Optional()])
    
class FilterAssetsForm(Form):
    horsepower_search = IntegerField('horsepower_search', validators=[Optional()])
    voltage_search = IntegerField('voltage_search', validators=[Optional()])
    rpm_search = IntegerField('rpm_search', validators=[Optional()])
    frame_search = StringField('frame_search', validators=[Optional()])
    enclosure_search = StringField('enclosure_search', validators=[Optional()])
    secondary_voltage_search = IntegerField('secondary_voltage_search', validators=[Optional()])
    attachments_search = StringField('attachments_search', validators=[Optional()])
    
class SearchAssetTag(Form):
    asset_tag_search = StringField('asset_tag_search', validators=[DataRequired()])