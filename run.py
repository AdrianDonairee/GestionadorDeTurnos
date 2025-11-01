from app import create_app

# expose `app` variable so gunicorn can import it with `run:app`
app = create_app('production')
