from flask import Flask
from api.v1.routes import v1_bp
from api.v2.routes import v2_bp

app = Flask(__name__)

app.register_blueprint(v1_bp, url_prefix='/api/v1')
app.register_blueprint(v2_bp, url_prefix='/api/v2')

if __name__=="__main__":
    app.run(debug=True)

api/v1/routes.py code:
