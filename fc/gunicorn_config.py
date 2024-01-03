import multiprocessing

# Gunicorn config variables
bind = "0.0.0.0:8000"  # Bind to all network interfaces on port 8000
workers = multiprocessing.cpu_count() * 2 + 1  # Number of worker processes

# Access log configuration
accesslog = "-"  # Log to stdout
errorlog = "-"   # Log to stderr
loglevel = "info"  # Log level

# Set the path to your Django application's WSGI module
# Replace 'your_project' with the actual name of your Django project
# Replace 'your_project.wsgi' with the actual path to your WSGI module
pythonpath = "/app/fc"
app_module = "fc.wsgi:application"

worker_class = "gthread"
timeout = 120