from models import setup_db, Users, Appointments
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask import Flask, request, Blueprint
from flask_login import LoginManager, login_manager, login_user, logout_user,login_required, current_user
from flask_cors import CORS
from flask import Flask, Blueprint, jsonify, redirect, render_template, request, flash
from flask.helpers import url_for
from werkzeug.security import generate_password_hash, check_password_hash

login_manager = LoginManager()


def create_app(test_config=None):
    app = Flask(__name__)
    app.config["JWT_SECRET_KEY"] = 'Hola1$'
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False
    setup_db(app)
    CORS(app,origins=['http://localhost:8080'])

    api = Blueprint("api", __name__, url_prefix="/api")
    jwt = JWTManager(app)
    login_manager.init_app(app)

    @jwt.expired_token_loader
    def expired_token_callback():
        return jsonify({
            'description': 'The token has expired.',
            'error': 'token_expired'
        }), 401

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(user_id)

    @login_manager.unauthorized_handler
    def noautorizado():
        if request.path.startswith(api.url_prefix):
            return {
                "success": False,
                "message": "Usuario no loggeado"
            }, 401
        else:
            flash("Primero debes registrarte")
            return redirect(url_for("/login"))

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(user_id)

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(user_id)

    @login_manager.unauthorized_handler
    def noautorizado():
        if request.path.startswith(api.url_prefix):
            return {
                "success": False,
                "message": "Usuario no loggeado"
            }, 401
        else:
            return {
                "success": True,
                "message": "Usuario loggeado"
            }

    @app.after_request
    def after_request(response):
        response.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorizations, true")
        response.headers.add("Access-Control-Allow-Methods", "GET, OPTIONS, POST, PATCH, DELETE")
        return response

  
    @api.route('/', methods=['GET'])
    def api_index():
        try:
            return {
                "success": True,
                "message": "Bienvenido a la API Venvet"
            }
        except Exception as e:
            return {
                "success": False,
                "message": str(e)
            }, 500
    
    @api.route('/me', methods=['GET'])
    @jwt_required()
    def api_me():
        return current_user.format(), 200

    @api.route("/users", methods=["GET"])
    def get_users():
        users = Users.query.order_by("id").all()

        if len(users) == 0:
            return {
                "message": "No se encontaron usuarios"
            }, 404
        
        return {
            "success": True,
            "users": [user.format() for user in users],
            "total_users": len(users)
        }, 200

    @api.route("/citas1", methods=["GET"])
    def get_citas():
        
        users = Appointments.query.order_by("id").all()
        return {
            "citas": [c.format() for c in users]
        }, 200
    
    @api.route("/citas/<id>", methods=["GET"])
    @jwt_required()
    def get_cita(id):
        c = Appointments.query.get(id)

        if c is None:
            return {
                "success": False,
                "message": "Cita no encontrada"
            }, 404

        if c.user_id != current_user.id:
            return {
                "success": False,
                "message": "La cita no le pertenece a este usuario"
            }, 403

        return c.format(), 200
    
    @api.route('/signup', methods=['POST'])
    def api_signup():
        if current_user.is_authenticated:
            return {
                "success": False,
                "message": "Usuario ya loggeado"
            }, 400

        username = request.json.get('username')
        password = request.json.get('password')

        if username is None:
            return {
                "success": False,
                "message": "No se ha enviado el nombre"
            }, 400

        if password is None:
            return {
                "success": False,
                "message": "No se ha enviado contraseña"
            }, 400


        if len(password) < 8:
            return {
                "success": False,
                "message": "La contraseña debe tener minimo 8 caracteres"
            }, 400
    
        if password.islower():
            return {
                "success": False,
                "message": "La contraseña debe tener minimo una mayúscula"
            }, 400

        if True not in [char.isdigit() for char in password]:
            return {
                "success": False,
                "message": "La contraseña debe tener mínimo un número"
            }, 400

        try:
            user = Users(username=username, password=generate_password_hash(password, method='sha256'))
            user.insert()
            login_user(user)
            token = create_access_token(identity=user.id)
        except Exception as e:
            return {
                "success": False,
                "message": "Error al registrar usuario",
                "error": str(e)
            }, 400
        else:
            return {"success": True, "token":token}, 200


    @api.route('/login', methods=['POST'])
    def api_login():
        if request.method == 'POST':
            username = request.json.get("username")
            password1 = request.json.get("password")

            user = Users.query.filter_by(username=username).first()

            if user:
                if check_password_hash(user.password, password1):
                    token = create_access_token(identity=user.id)
                    login_user(user, remember=True)
                    return {
                        "success": True,
                        "message": "Usuario autenticado correctamente",
                        "token": token
                    }, 200
                else:
                    return {
                        "success": False,
                        "message": "Contraseña incorrecta"
                    }, 401
            else:
                return {
                    "success": False,
                    "message": "Usuario no encontrado"
                }, 404


    @api.route("/logout", methods=["POST"])
    
    def api_logout():
        logout_user()
        return {"success": True}, 200

    @api.route("/citas", methods=['POST'])
    def api_registrar_cita():
        petOwner = request.json.get("petOwner")
        petName = request.json.get("petName")
        aptDate = request.json.get("aptDate")
        aptNotes = request.json.get("aptNotes")

        if petOwner is None:
            return {
                "success": False,
                "message": "No se ha enviado el nombre"
            }, 400

        if petName is None:
            return {
                "success": False,
                "message": "No se ha enviado la raza de la mascota"
            }, 400
    
        if aptDate is None:
            return {
                "success": False,
                "message": "No se ha enviado la fecha"
            }, 400

        try:
            c = Appointments(owner_id= 1, petOwner=petOwner, petName=petName, aptDate=aptDate,aptNotes=aptNotes)
            c.insert()
        except:
            return {
                "success": False,
                "message": "Error al registrar su cita"
            }, 400

        return {"success": True}, 200

    # PATCH / PUT

    @api.route("/citas/<id>", methods=['PATCH'])
    @login_required
    def api_editar_cita(id):
        petOwner = request.json.get("petOwner")
        petName = request.json.get("petName")
        aptDate = request.json.get("aptDate")
    
        c = Appointments.query.get(id)

        if c is None:
            return {
                "success": False,
                "message": "Cita no encontrada"
            }, 404

        if c.user_id != current_user.id:
            return {
                "success": False,
                "message": "La cita no le pertenece a este usuario"
            }, 403

        if petOwner is not None:
            try: 
                c.petOwner = petOwner
            except:
                return {
                    "success": False,
                    "message": "Error al actualizar el nombre"
                }, 400

        if petName is not None:
            try: 
                c.petName = petName
            except:
                return {
                    "success": False,
                    "message": "Error al actualizar la raza de la"
                }, 400

        if aptDate is not None:
            try: 
                c.aptDate = aptDate
            except:
                return {
                    "success": False,
                    "message": "Error al actualizar la fecha de reserva"
                }, 400

        try:
            c.update()
        except Exception as e:
            return {
                "success": False,
                "message": "Error al actualizar la cita",
                "error": str(e)
            }, 400
        else:
            return {"success": True}, 200

    # DELETE

    @api.route("/citas12", methods=['POST'])
    
    def api_eliminar_cita():
        id = request.json.get("id")
        c = Appointments.query.get(id)

        if c is None:
            return {
                "success": False,
                "message": "Cita no encontrada"
            }, 404


        try:
            c.delete()
        except:
            return {
                "success": False,
                "message": "Error al eliminar la cita"
            }, 400
        else:
            return {"success": True}, 200

    app.register_blueprint(api)

    return app