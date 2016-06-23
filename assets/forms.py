from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, FloatField
from wtforms.validators import DataRequired, Optional

class SubmitAssetForm(Form):
    asset_tag = StringField('asset_tag', validators=[DataRequired()])
    horsepower = IntegerField('horsepower', validators=[DataRequired()])
    voltage = IntegerField('voltage', validators=[DataRequired()])
    rpm = IntegerField('rpm', validators=[DataRequired()])
    frame = StringField('frame', validators=[DataRequired()])
    enclosure = StringField('enclosure', validators=[DataRequired()])
    secondary_voltage = FloatField('secondary_voltage', validators=[Optional()])
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