from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from .config import Config  # Import the Config class
from dotenv import load_dotenv  # Import dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the Flask application
app = Flask(__name__)

# Apply the configuration from Config class
app.config.from_object(Config)

# Enable CORS (Cross-Origin Resource Sharing)
CORS(app, resources={r"/*": {"origins": "*"}})

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Import routes after app creation
from . import routes


""" from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Enable CORS (Cross-Origin Resource Sharing)
CORS(app)

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Import routes after app creation (this is fine and keeps things modular)
from . import routes """


""" from flask import Flask
from flask_cors import CORS


# Create app with CORS
app = Flask(__name__)
CORS(app)

# Import routes after app creation
from . import routes """