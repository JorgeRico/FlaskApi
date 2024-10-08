
from api.apiResources import BooksGETResource, BookGETResource, BookPOSTResource, BookPUTResource, BookDELETEResource
from api.swaggerConfig import SwaggerConfig

class Endpoints:
    
    def __init__(self, api):
        # GET swagger config
        api.add_resource(SwaggerConfig, '/swagger-config')
        
        # GET books
        api.add_resource(BooksGETResource, '/books')
        api.add_resource(BookGETResource, '/books/<int:id>')

        # POST book
        api.add_resource(BookPOSTResource, '/books')

        # PUT book
        api.add_resource(BookPUTResource, '/books/<int:id>')

        # DELETE book
        api.add_resource(BookDELETEResource, '/books/<int:id>')
