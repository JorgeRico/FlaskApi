from flask import Flask, jsonify
from flask_restful import Api, MethodNotAllowed, NotFound
from flask_cors import CORS
from endpoints.endpointResources import Endpoints

# ============================================
# initialize
# ============================================
app = Flask(__name__)
CORS(app)
api = Api(app, prefix='', catch_all_404s=True)

# ============================================
# error handlers
# ============================================
@app.errorhandler(NotFound)
def handle_method_not_found(e):
    response = jsonify({"message": str(e)})
    response.status_code = 404
    return response

#error handler
@app.errorhandler(MethodNotAllowed)
def handle_method_not_allowed_error(e):
    response = jsonify({"message": str(e)})
    response.status_code = 405
    return response

# ============================================
# Add Api Endpoints
# ============================================
# GET swagger config
# api.add_resource(SwaggerConfig, '/swagger-config')

api = Endpoints(api)

# ============================================
# run
# ============================================
app.run(host='0.0.0.0', port=5000, debug=True)
