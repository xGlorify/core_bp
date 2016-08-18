from core import db, current_user
from datetime import datetime
from tasks.models import Tasks, link_table

class Motor(db.Model):
    #Define Motor table name.
    #Define Motor table variables. Asset tag is primary_key.
    id = db.Column('id', db.Integer, primary_key=True)
    asset_tag = db.Column('Asset Tag', db.String(100), unique=True, nullable = False)
    serial = db.Column('Serial', db.String(100))
    manufacturer = db.Column('Manufacturer', db.String(30), nullable = False)
    model_number = db.Column('Model Number', db.String(50), nullable = False)
    current = db.Column('Current', db.String, nullable = False)
    frequency = db.Column('frequency', db.String)
    voltage = db.Column('Voltage', db.String, nullable = False)
    secondary_voltage = db.Column('Secondary Voltage', db.Numeric)
    power_factor = db.Column('Power Factor', db.Float)
    efficiency = db.Column('Efficiency', db.Float)
    horsepower = db.Column('Horsepower', db.Float, nullable = False)
    rpm = db.Column('RPM', db.Integer, nullable = False)
    design = db.Column('Design', db.String(20), nullable = False)
    frame = db.Column('Frame', db.String(30))
    enclosure = db.Column('Enclosure', db.String(30), nullable = False)
    attachments = db.Column('Attachments', db.String(200))
    location = db.Column('Location', db.String(30))
    picture = db.Column('Picture', db.String(100))
    status = db.Column('Status', db.String(50))
    tasks = db.relationship('Tasks', secondary = link_table, backref = db.backref('asset_tasks'), lazy = 'dynamic')
    added_by = db.Column('Added By', db.String(50))
    pub_date = db.Column(db.DateTime())
    
    def __init__(self, asset_tag, serial, manufacturer, model_number, current, frequency, voltage, secondary_voltage, power_factor,
	efficiency, horsepower, rpm, design, frame, enclosure, attachments, location, picture, status, added_by=None, pub_date=None):
        self.asset_tag = asset_tag
        self.serial = serial
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
        self.location = location
        self.picture = picture
        self.status = status
        #self.tasks = tasks
        self.added_by = str(current_user.first_name) + " " + str(current_user.last_name)
        self.pub_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
