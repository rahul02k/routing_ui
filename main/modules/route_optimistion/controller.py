# from main.modules.route_optimistion.models import Distance_Matrix,Order_Details,Source_Coordinates,Destination_Coordinates,Fleet_Details,Vehicle_Availability
from flask import Flask, render_template, Response, request,send_file
import pandas as pd
import uuid
from datetime import datetime,timezone
import json
import os
class RouteOptimzer:

    """
    This class is used to handler all operation related to route optimizer
    """
    file_dict = {}

    @classmethod
    def index(cls):
        return render_template('index.html')
    
    @classmethod
    def download_distance_template(cls):
        current_path = os.getcwd()
        path = r'/main/excel_templates/distance_matrix_data.xlsx'
        final_path = current_path+path
        return send_file(final_path, as_attachment=True)

    @classmethod
    def download_source_template(cls):
        current_path = os.getcwd()
        path = 'excel_templates/Template_Source Coordinates.xlsx'
        final_path = current_path+path
        return send_file(path, as_attachment=True)
    
    @classmethod
    def download_destination_template(cls):
        current_path = os.getcwd()
        path = 'excel_templates/Template_Destination Coordinates.xlsx'
        final_path = current_path+path
        return send_file(path, as_attachment=True)
    
    @classmethod
    def download_fleet_template(cls):
        current_path = os.getcwd()
        path = 'excel_templates/Template_Fleet Details.xlsx'
        final_path = current_path+path

        return send_file(path, as_attachment=True)
    
    @classmethod
    def download_vehicle_template(cls):
        current_path = os.getcwd()
        path = 'excel_templates/Template_Vehicle Availability Times.xlsx'
        final_path = current_path+path
        return send_file(path, as_attachment=True)
    
    @classmethod
    def download_order_template(cls):
        current_path = os.getcwd()
        path = 'excel_templates/Template_Order Details.xlsx'
        final_path = current_path+path

        return send_file(path, as_attachment=True)
    
    @classmethod
    def upload_file_distance_matrix(cls):
        print("UPLOAD FILE METHOD CALLED")
            # Read the File using Flask request
        print(request.files.keys())
        file = request.files['uploaded_file']
        # save file in local directory
        file.save(file.filename)

        # # Parse the data as a Pandas DataFrame type
        data = pd.read_excel(file.filename,engine='openpyxl')
        uid = str(uuid.uuid4())
        data['uid']=uid
        file_dict['distance_matrix'] = uid
        data['created_at'] = datetime.now(timezone.utc)
        print(data.head())
        print(data.to_sql(name='distance_matrix', con=db.engine, if_exists = 'append', index=False))
        print("dictionary :", file_dict)

        # Return HTML snippet that will render the table
        return {'success':True,"uid":uid}

    @classmethod    
    def upload_file_source_coordinates(cls):
        if request.method=='POST':
            # Read the File using Flask request
            print(request.files.keys())
            file = request.files['uploaded_file']
            # save file in local directory
            file.save(file.filename)
        
            # # Parse the data as a Pandas DataFrame type
            data = pd.read_excel(file.filename,engine='openpyxl')
            uid = str(uuid.uuid4())
            data['uid']= uid
            file_dict['source_coordinates'] = uid
            data['created_at'] = datetime.now(timezone.utc)
            print(data.head())
            print(data.to_sql(name='source_coordinates', con=db.engine, if_exists = 'append', index=False))

            print("dictionary :", file_dict)

            # Return HTML snippet that will render the table
            return {'success':True,"uid":uid}
        
    @classmethod
    def upload_file_destination_coordinates(cls):
        if request.method=='POST':
            # Read the File using Flask request
            print(request.files.keys())
            file = request.files['uploaded_file']
            # save file in local directory
            file.save(file.filename)
        
            # # Parse the data as a Pandas DataFrame type
            data = pd.read_excel(file.filename,engine='openpyxl')
            uid = str(uuid.uuid4())
            data['uid']=uid
            file_dict['destination_coordinates'] = uid
            data['created_at'] = datetime.now(timezone.utc)
            print(data.head())
            print(data.to_sql(name='destination_coordinates', con=db.engine, if_exists = 'append', index=False))
            print("dictionary :", file_dict)

            # Return HTML snippet that will render the table
            return {'success':True,"uid":uid}
        
    @classmethod
    def upload_file_order_details(cls):
        if request.method=='POST':
            # Read the File using Flask request
            print(request.files.keys())
            file = request.files['uploaded_file']
            # save file in local directory
            file.save(file.filename)
        
            # # Parse the data as a Pandas DataFrame type
            data = pd.read_excel(file.filename,engine='openpyxl')
            uid = str(uuid.uuid4())
            data['uid']=uid
            file_dict['order_details'] = uid
            data['created_at'] = datetime.now(timezone.utc)
            print(data.head())
            print(data.to_sql(name='order_details', con=db.engine, if_exists = 'append', index=False))
            # Return HTML snippet that will render the table

            print("dictionary :", file_dict)

            return {'success':True,"uid":uid}
        
    @classmethod
    def upload_file_fleet_details(cls):
        if request.method=='POST':
            # Read the File using Flask request
            print(request.files.keys())
            file = request.files['uploaded_file']
            # save file in local directory
            file.save(file.filename)
        
            # # Parse the data as a Pandas DataFrame type
            data = pd.read_excel(file.filename,engine='openpyxl')
            uid = str(uuid.uuid4())
            data['uid']= uid
            file_dict['fleet_details']=uid
            data['created_at'] = datetime.now(timezone.utc)
            print(data.head())
            print(data.to_sql(name='fleet_details', con=db.engine, if_exists = 'append', index=False))
            # Return HTML snippet that will render the table
            print("dictionary :", file_dict)

            return {'success':True,"uid":uid}

    @classmethod    
    def upload_file_vehicle_availability(cls):
        if request.method=='POST':
            # Read the File using Flask request
            print(request.files.keys())
            file = request.files['uploaded_file']
            # save file in local directory
            file.save(file.filename)
            uid = str(uuid.uuid4())
            # # Parse the data as a Pandas DataFrame type
            data = pd.read_excel(file.filename,engine='openpyxl')
            data['uid']=uid
            file_dict['vehicle_availability'] = uid
            data['created_at'] = datetime.now(timezone.utc)
            print(data.head())
            print(data.to_sql(name='vehicle_availability', con=db.engine, if_exists = 'append', index=False))
            # Return HTML snippet that will render the table

            print("dictionary :", file_dict)
            return {'success':True,"uid":uid}
    @classmethod    
    def generate_route_plan(cls):
        config = request.get_json()
        config = config['config']
        config['file_upload_uids'] = file_dict
        print(config)
        print("successfully hit ajax request")
        return "200ok"