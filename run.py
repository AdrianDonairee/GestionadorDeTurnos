from app import create_app

# Exponer la variable `app` para que gunicorn la importe con `run:app`
app = create_app('production')
