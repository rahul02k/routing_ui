from main.db import BaseModel, db

class Distance_Matrix(BaseModel):
    """
    Model for distance matrix
    """
    __tablename__ = "distance_matrix"
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(500))
    start_node =  db.Column(db.String(500), nullable=True)
    end_node = db.Column(db.String(500), nullable=True)
    distance = db.Column(db.String(500), nullable=True)
    time = db.Column(db.String(500), nullable=True)
    created_at = db.Column(db.DateTime(timezone=True))

class Order_Details(db.Model):
    __tablename__ = "order_details"
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(500))
    Order_ID =  db.Column(db.String(500), nullable=True)
    Destination = db.Column(db.String(500), nullable=True)
    Order_weight = db.Column(db.Double(), nullable=True)
    Order_volume = db.Column(db.Double(), nullable=True)

    Delivery_slot_start_time =  db.Column(db.DateTime(), nullable=True)
    Delivery_slot_end_time = db.Column(db.DateTime(), nullable=True)
    Special_vehicle_requirements =  db.Column(db.String(500), nullable=True)
    created_at = db.Column(db.DateTime(timezone=True))

class Source_Coordinates(db.Model):
    __tablename__ = "source_coordinates"
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(500))
    Hub_ID =  db.Column(db.String(500), nullable=True)
    Hub_latitude = db.Column(db.String(500), nullable=True)
    Hub_longitude = db.Column(db.String(500), nullable=True)
    created_at = db.Column(db.DateTime(timezone=True))

class Destination_Coordinates(db.Model):
    __tablename__ = "destination_coordinates"
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(500))
    Destination_ID =  db.Column(db.String(500), nullable=True)
    Destination_latitude = db.Column(db.Float(), nullable=True)
    Destination_longitude = db.Column(db.Float(), nullable=True)
    created_at = db.Column(db.DateTime(timezone=True))

class Fleet_Details(db.Model):
    __tablename__ = "fleet_details"
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(500))
    Vehicle_type =  db.Column(db.String(500), nullable=True)
    Vehicle_count = db.Column(db.Integer(),nullable=True)
    Fixed_cost =  db.Column(db.Float(), nullable=True)
    Variable_cost_per_km = db.Column(db.Float(), nullable=True)
    Capacity_kg =  db.Column(db.Float(), nullable=True)
    Avg_speed_kmph =  db.Column(db.Float(), nullable=True)
    Characteristics = db.Column(db.String(500))
    created_at = db.Column(db.DateTime(timezone=True))

class Vehicle_Availability(db.Model):
    __tablename__ = "vehicle_availability"
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(500))
    Vehicle_ID = db.Column(db.String(500),nullable=True)
    Availability_start_time = db.Column(db.DateTime(), nullable=True)
    Availability_end_time = db.Column(db.DateTime(), nullable=True)
    created_at = db.Column(db.DateTime(timezone=True))