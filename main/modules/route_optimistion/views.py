from flask import jsonify, make_response, request
from flask_restx import Namespace, Resource
from flask import render_template,make_response
from main.modules.route_optimistion.controller import RouteOptimzer

class GetPage(Resource):
    def get(self):
        """
        This view function is used to get 
        
        """

        return make_response(render_template('index.html'))
    


route_namespace = Namespace("route", description="route optimiser application")

route_namespace.add_resource(GetPage, "/index")

