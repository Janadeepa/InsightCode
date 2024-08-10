### **docs/setup_guide.md**
This document provides step-by-step instructions on how to set up the project.

```markdown
# Setup Guide

## Prerequisites

- Python 3.8 or later
- Node.js 14 or later
- npm (Node Package Manager)
- Git

## Setting Up the Backend

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/InsightCode.git
   cd InsightCode
   ```

2. **Create and Activate a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Backend Dependencies**
   ```bash
   pip install -r backend/requirements.txt
   ```

4. **Set Up Environment Variables**

   Copy `config/settings.py` to `config/.env` and configure the necessary environment variables.

5. **Run Migrations and Start the Backend**
   ```bash
   cd backend
   python run.py
   ```

## Setting Up the Frontend

1. **Navigate to the Frontend Directory**
   ```bash
   cd frontend
   ```

2. **Install Frontend Dependencies**
   ```bash
   npm install
   ```

3. **Run the Frontend Application**
   ```bash
   npm start
   ```

## Running Tests

To run backend tests:
```bash
cd backend
pytest
```

To run frontend tests:
```bash
cd frontend
npm test
```

## Deploying the Application

Refer to the CI/CD documentation for deployment instructions using GitHub Actions or Jenkins.

For more details, check the `README.md` file for additional information.
