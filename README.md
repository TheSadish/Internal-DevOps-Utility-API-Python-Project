# Internal DevOps Utility API 🚀

A small FastAPI service that demonstrates internal DevOps utilities such as system metrics (CPU, memory, disk). 
It also includes an endpoint to fetch AWS resources information.
The project is organized to keep routes, services, and app configuration separated for clarity and testability.

---

## Features ✅

- Minimal FastAPI app with modular routers
- `/metrics` endpoint returning CPU, memory, and disk usage (powered by `psutil`)
- `/s3` endpoint returning AWS S3 bucket info (powered by `boto3`)
- Clean separation between request handling (routers) and business logic (services)

---

## Quickstart 🔧

Prerequisites:
- Python 3.10+ (or compatible)
- Git
- awscli with user creds

Setup:

# clone repo
git clone [repo-url](https://github.com/TheSadish/Internal-DevOps-Utility-API-Python-Project)
cd Internal-DevOps-Utility-API-Python-Project

# create venv (Windows example)
python -m venv myEnv
myEnv\Scripts\activate

# install deps
pip install -r requirements.txt

# configure AWS credentials
aws configure -> provide your AWS Access Key, Secret Key for user

# Run the server:
python main.py


Open API docs: http://localhost:8000/docs
For better view : http://localhost:8000/redocs