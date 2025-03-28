from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    
    # Register error handlers at the application level
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404
    
    with app.app_context():
        # Import parts of our application
        from . import routes
        
        # Register Blueprints
        app.register_blueprint(routes.bp)
        
    return app