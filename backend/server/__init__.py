from models import setup_db, Users, Appointments

from flask import Flask, request, Blueprint
from flask_login import LoginManager, login_manager, login_user, logout_user,login_required, current_user
from flask_cors import CORS

login_manager = LoginManager()


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    api = Blueprint("api", __name__, url_prefix="/api")

    login_manager.init_app(app)

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
    @login_required
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

    @api.route("/citas", methods=["GET"])
    @login_required
    def get_citas():
        return {
            "citas": [c.format() for c in current_user.citas]
        }, 200
    
    @api.route("/citas/<id>", methods=["GET"])
    @login_required
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
            u = Users(username, password)
            u.insert()
            login_user(u)
        except Exception as e:
            return {
                "success": False,
                "message": "Error al registrar usuario",
                "error": str(e)
            }, 400
        else:
            return {"success": True}, 200


    @api.route('/login', methods=['POST'])
    def api_login():
        if request.method == 'POST':
            username = request.json.get("username")
            password = request.json.get("password")

            user = Users.query.filter_by(username=username).first()

            if user:
                if user.password==password:
                    login_user(user, remember=True)
                    return {
                        "success": True,
                        "message": "Usuario autenticado correctamente"
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
    @login_required
    def api_logout():
        logout_user()
        return {"success": True}, 200

    @api.route("/citas", methods=['POST'])
    @login_required
    def api_registrar_cita():
        name = request.json.get("name")
        pet = request.json.get("pet")
        date = request.json.get("date")

        if name is None:
            return {
                "success": False,
                "message": "No se ha enviado el nombre"
            }, 400

        if pet is None:
            return {
                "success": False,
                "message": "No se ha enviado la raza de la mascota"
            }, 400
    
        if date is None:
            return {
                "success": False,
                "message": "No se ha enviado la fecha"
            }, 400

        try:
            c = Appointments(user_id=current_user.id, name=name, pet=pet, date=date)
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
        name = request.json.get("name")
        pet = request.json.get("pet")
        date = request.json.get("date")
    
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

        if name is not None:
            try: 
                c.name = name
            except:
                return {
                    "success": False,
                    "message": "Error al actualizar el nombre"
                }, 400

        if pet is not None:
            try: 
                c.pet = pet
            except:
                return {
                    "success": False,
                    "message": "Error al actualizar la raza de la"
                }, 400

        if date is not None:
            try: 
                c.date = date
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

    @api.route("/citas/<id>", methods=['DELETE'])
    @login_required
    def api_eliminar_cita(id):
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