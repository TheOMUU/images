Objective
 Dockerize a Flask or FastAPI app
 Build, run, test the Docker container
 Push the image to Docker Hub ([username]/myapp)

Prerequisites
Make sure you have these installed:
 Docker Desktop for Windows
 Visual Studio Code
 Python
 A Docker Hub account

1. Create Your Flask App
Create a folder docker-flask-app and inside it, create:

app.py (in vscode)
from flask import Flask
app = Flask(__name__)
@app.route(&#39;/&#39;)
def hello():
return &#39;Hello from Dockerized Flask!&#39;
if __name__ == &#39;__main__&#39;:
app.run(host=&#39;0.0.0.0&#39;, port=5000)

requirements.txt (in vscode)
flask

2. Create &lt;Dockerfile&gt; (in vscode)
Note: Make sure you have Docker Extension installed in VSCode before
exactly creating Dockerfile
# Use official Python base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy app files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the app
CMD [&quot;python&quot;, &quot;app.py&quot;]

3. Build the Docker Image (in vscode terminal)
Open VS Code terminal in the project folder and run:
docker build -t [username]/myapp:latest .

4. Run the Container (Use Port 5050 if 5000 is occupied) (in vscode terminal)
docker run -d -p 5050:5000 [username]/myapp:latest

on browser
Then visit: http://localhost:5050

You should see: Hello from Dockerized Flask!

5. Push to Docker Hub (in vscode terminal) {if you already have docker app open it
will automatically log in by itself}
First, log in:
docker login

# Username: [username]
# Password: [enter your Docker Hub password or token]

If not already done, create the repo on hub.docker.com: (on browser)
 Name: myapp
 Visibility: Public

Now push: (in vscode terminal)
docker push [username]/myapp:latest

You should see multiple Pushed lines and a digest: at the end, confirming success.