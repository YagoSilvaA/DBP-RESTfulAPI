superindice^^2

Nombre del proyecto: Control de citas para veterinarias: Venvet
Integrantes:
* Yago Silva Albarracin
* Alejandro Martín Garay Saavedra
* Cesar Enrique Cabezas Baquerizo

Descripción del proyecto.
El proyecto tiene como finalidad el crear una plataforma para llevar a cabo el control de citas dentro de una veterinaria.  Esta contara con una sección donde se pondrán visualizar todas las citas así como las fecha y la hora, también se dará a conocer la información del animal, como nombre y especie para que los empleados de la institución puedan digitalizar el control de citas. 
Objetivos principales
El proyecto tiene como objetivo principal el poder solucionar el problema de no tener un buen control de citas en veterinarias, se planea implementar una plataforma en la cual la entidad pueda avisar al cliente de cuando se agenda la cita y si se llegara a cambiar la fecha notificarle. De esta forma facilitando él acceso a la información para tener un proceso interno de servicio más eficiente. 
Misión
Brindar una plataforma de registros eficiente y práctica de manera local para veterinarias innovadoras.

Visión
Tener una plataforma eficiente y de fácil acceso para brindar un servicio de buena calidad e innovar el sistema de citas en las veterinarias del Perú.

Información de librerías/frameworks/plugins
alembic==1.7.7, bcrypt==3.2.2, certifi==2021.10.8, cffi==1.15.0, charset-normalizer==2.0.12, click==8.1.3, colorama==0.4.4, export==0.2.0, Flask==2.1.2, Flask-Bcrypt==1.0.1, Flask-Cors==3.0.10, Flask-Login==0.6.1, Flask-Migrate==3.1.0Flask-SQLAlchemy==2.5.1, greenlet==1.1.2, idna==3.3, itsdangerous==2.1.2, Jinja2==3.1.2, Mako==1.2.0, MarkupSafe==2.1.1, psycopg2-binary==2.9.3, pycparser==2.21, python-dotenv==0.20.0, requests==2.27.1, six==1.16.0, SQLAlchemy==1.4.36, urllib3==1.26.9, Werkzeug==2.1.2

Pasos para ejecutar la app
(En la terminal de VS code)
- Backend: flask run 
- Frontend: yarn serve

Endpoints
- /: metodo GET
    - Muestra la pagina principal de la plataforma
- /me: metodo GET
    - Perfil del usuario
- /users: metodo GET
    - Obtiene a los usuarios registrados en la base de datos 
- /citas: metodo GET
    - Obtiene las citas registradas 
- /signup: metodo POST
    - Permite que un nuevo usuario cree una cuenta para utilizar la plataforma
- /login: metodo POST
    - Permite que usuarios ya registrados ingresen a la plataforma
- /logout: metodo POST
    - Facilita la salida del usuario de la plataforma
- /citas/<id>: metodo patch 
    - Permite actualizar citas ya realizadas
- /citas/<id>: metodo DELETE
    - Permite eliminar citas ya realizadas
