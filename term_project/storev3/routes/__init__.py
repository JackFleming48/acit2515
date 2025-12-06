from .products import products_bp
from .home import home_bp
from .users import users_bp
from .categories import categories_bp
from .order import order_bp

def register_blueprints(app):

    app.register_blueprint(products_bp, url_prefix="/products")
    app.register_blueprint(home_bp, url_prefix="/home")
    app.register_blueprint(users_bp, url_prefix="/users")
    app.register_blueprint(categories_bp, url_prefix="/categories")
    app.register_blueprint(order_bp, url_prefix="/order")