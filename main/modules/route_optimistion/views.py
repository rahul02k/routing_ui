from flask import jsonify, make_response, request
from flask_restx import Namespace, Resource,reqparse
from flask import render_template,make_response
from main.modules.route_optimistion.controller import RouteOptimzer
from flask import send_file
import os
upload_parser = reqparse.RequestParser()
from werkzeug.datastructures import FileStorage

upload_parser.add_argument('file', location='files',
                           type=FileStorage)
class GetPage(Resource):
    def get(self):
        """
        This view function is used to render html

        """
        print(request)
        return make_response(render_template('index.html'))
    
class DownloadDistanceMatrix(Resource):
    def get(self):
        """
        This view function is used to download distance matrix template
        """

        # final_path =r'C:\Users\rahul\Desktop\statusneo\starter-kit\main\excel_templates\distance_matrix_data.xlsx'

        response = make_response(RouteOptimzer().download_distance_template())

        return response
class SourceTemplateDownload(Resource):
    def get(self):
        """
        This view function is used to download distance matrix template
        """

        # final_path =r'C:\Users\rahul\Desktop\statusneo\starter-kit\main\excel_templates\distance_matrix_data.xlsx'

        response = make_response(RouteOptimzer().download_source_template())

        return response
    
class DestinationTemplateDownload(Resource):
    def get(self):
        """
        This view function is used to download distance matrix template
        """

        # final_path =r'C:\Users\rahul\Desktop\statusneo\starter-kit\main\excel_templates\distance_matrix_data.xlsx'

        response = make_response(RouteOptimzer().download_destination_template())

        return response
    
class FleetTemplateDownload(Resource):
    def get(self):
        """
        This view function is used to download distance matrix template
        """

        # final_path =r'C:\Users\rahul\Desktop\statusneo\starter-kit\main\excel_templates\distance_matrix_data.xlsx'

        response = make_response(RouteOptimzer().download_fleet_template())

        return response
    
class VehicleTemplateDownload(Resource):
    def get(self):
        """
        This view function is used to download distance matrix template
        """

        # final_path =r'C:\Users\rahul\Desktop\statusneo\starter-kit\main\excel_templates\distance_matrix_data.xlsx'

        response = make_response(RouteOptimzer().download_vehicle_template())

        return response
    
class OrderTemplateDownload(Resource):
    def get(self):
        """
        This view function is used to download distance matrix template
        """

        # final_path =r'C:\Users\rahul\Desktop\statusneo\starter-kit\main\excel_templates\distance_matrix_data.xlsx'

        response = make_response(RouteOptimzer().download_order_template())

        return response
    
class GenerateRoutePlan(Resource):
    def post(self):
        """
        The view function is for generating route plan
        """

        config = request.get_json()
        config = config['config']
        # config['file_upload_uids'] = file_dict
        print(config)
        print("successfully hit ajax request")
        return "200ok"


class DistanceMatrixUpload(Resource):

    def post(self):

        """
        This view function is used to upload distance matrix
        
        """
        args = upload_parser.parse_args()
        file = args['file']
        file.save("example")
        print("distance matrix view called")
        # RouteOptimzer.upload_file_distance_matrix()
        return make_response("File Successfully uploaded")
        

route_namespace = Namespace("route", description="route optimiser application")

route_namespace.add_resource(GetPage, "/index")
route_namespace.add_resource(DownloadDistanceMatrix,'/download_distance_template')
route_namespace.add_resource(SourceTemplateDownload,'/download_source_template') 
route_namespace.add_resource(DestinationTemplateDownload,'/download_destination_template') 
route_namespace.add_resource(FleetTemplateDownload,'/download_fleet_template') 
route_namespace.add_resource(VehicleTemplateDownload,'/download_vehicle_template') 
route_namespace.add_resource(OrderTemplateDownload,'/download_order_template') 
route_namespace.add_resource(GenerateRoutePlan,'/generate_route_plan')

route_namespace.add_resource(DistanceMatrixUpload,'/upload_file_distance_matrix') 


