from core import db
from datetime import datetime

class Motor(db.Model):
    #Define Motor table name.
    __tablename__ = 'Motor'
    #Define Motor table variables. Asset tag is primary_key.
    asset_tag = db.Column('Asset Tag', db.String(100), unique=True, primary_key = True, nullable = False)
    horsepower = db.Column('Horsepower', db.Integer, nullable = False)
    voltage = db.Column('Voltage', db.Integer, nullable = False)
    rpm = db.Column('RPM', db.Integer, nullable = False)
    frame = db.Column('Frame', db.String(30), nullable = False)
    enclosure = db.Column('Enclosure', db.String(30), nullable = False)
    secondary_voltage = db.Column('Secondary Voltage', db.Numeric)
    attachments = db.Column('Attachments', db.String(30))
    pub_date = db.Column(db.DateTime())
    
    
    
    def __init__(self, asset_tag, horsepower, voltage, rpm, frame, enclosure, secondary_voltage, attachments, pub_date=None):
        self.asset_tag = asset_tag
        self.horsepower = horsepower
        self.voltage = voltage
        self.rpm = rpm
        self.frame = frame
        self.enclosure = enclosure
        self.secondary_voltage = secondary_voltage
        self.attachments = attachments
        self.pub_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")