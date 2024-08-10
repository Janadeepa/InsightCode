# services/__init__.py

# Initialize the services module.
# Import services here to make them available when the module is imported.
from .github_integration import get_pull_requests
from .ci_cd_integration import trigger_build
