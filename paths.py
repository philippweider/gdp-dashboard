from pathlib import Path

# Get the root directory (where app.py is located)
ROOT_DIR = Path(__file__).parent.absolute()

# Define all path constants
SETTINGS_FILE = ROOT_DIR / "settings.yaml"
CACHE_DIR = ROOT_DIR / "cache"
HISTORY_DIR = ROOT_DIR / "history"
AUTH_DEVICES_FILE = ROOT_DIR / "auth_devices.json"
