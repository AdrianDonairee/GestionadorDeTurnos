from app import create_app
import logging
# Referencia: https://docs.python.org/3/library/logging.html
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
app = create_app()

# Referencia: https://flask.palletsprojects.com/en/3.0.x/appcontext/
app.app_context().push()

if __name__ == '__main__':
        """
        Inicio del servidor
        Referencias:
            - https://flask.palletsprojects.com/en/3.0.x/api/#flask.Flask.run
            - Book Flask Web Development Page 9
        """
        app.run(host="0.0.0.0", debug=True, port=5000)
    