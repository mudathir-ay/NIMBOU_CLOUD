# NIMBOU_CLOUD
# Chatbot Deployment with Flask and JavaScript

In this tutorial, we deploy the chatbot I created in [this](#) tutorial with Flask and JavaScript.

This gives **two deployment options**:

- **Deploy within Flask app** using a `jinja2` template.
- **Serve only the Flask prediction API**, so that the frontend (HTML & JavaScript) can run separately.

---

## 🔗 **Initial Setup**

This repo contains the starter files.

### **Clone the Repository & Create a Virtual Environment**
```sh
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
python3 -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows
