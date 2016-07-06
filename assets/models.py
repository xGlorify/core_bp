from core import db
from datetime import datetime

class Motor(db.Model):
    #Define Motor table name.
    __tablename__ = 'Motor'
    #Define Motor table variables. Asset tag is primary_key.
    asset_tag = db.Column('Asset Tag', db.String(100), unique=True, primary_key = True, nullable = False)
    manufacturer = db.Column('Manufacturer', db.String(30), nullable = False)
    model_number = db.Column('Model Number', db.String(50), nullable = False)
    current = db.Column('Current', db.Integer, nullable = False)
    frequency = db.Column('frequency', db.Integer, nullable = False)
    voltage = db.Column('Voltage', db.Integer, nullable = False)
    secondary_voltage = db.Column('Secondary Voltage', db.Numeric)
    power_factor = db.Column('Power Factor', db.Integer, nullable = False)
    efficiency = db.Column('Efficiency', db.Integer, nullable = False)
    horsepower = db.Column('Horsepower', db.Integer, nullable = False)
    rpm = db.Column('RPM', db.Integer, nullable = False)
    design = db.Column('Design', db.String(20), nullable = False)
    frame = db.Column('Frame', db.String(30), nullable = False)
    enclosure = db.Column('Enclosure', db.String(30), nullable = False)
    attachments = db.Column('Attachments', db.String(30))
    picture = db.Column('Picture', db.String(100))
    #status = db.Column('Status', db.String(50))
    pub_date = db.Column(db.DateTime())
    
    
    
    def __init__(self, asset_tag, manufacturer, model_number, current, frequency, voltage, secondary_voltage,
        power_factor, efficiency, horsepower, rpm, design, frame, enclosure, attachments, picture, pub_date=None):
        self.asset_tag = asset_tag
        self.manufacturer = manufacturer
        self.model_number = model_number
        self.current = current
        self.frequency = frequency
        self.voltage = voltage
        self.secondary_voltage = secondary_voltage
        self.power_factor = power_factor
        self.efficiency = efficiency
        self.horsepower = horsepower
        self.rpm = rpm
        self.design = design
        self.frame = frame
        self.enclosure = enclosure
        self.attachments = attachments
        self.picture = picture
        #self.status = status
        self.pub_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")