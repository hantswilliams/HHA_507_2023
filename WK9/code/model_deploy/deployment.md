# Deployment

## Docker Hub - Docker Image
- Create a Docker Hub account
- Create a new repository
- Create a Dockerfile
- Build the image
    - e.g., `docker build -t ml .`
- Add tag that includes your Docker Hub username
    - e.g., `docker tag ml:latest hants/la-crime-ml-demo:latest`
- Push the image to Docker Hub
    - e.g., `docker push hants/la-crime-ml-demo:latest`

## GCP - Cloud Run

### Build and Deploy
- Build and deploy the model to Cloud Run
- Go into GCP project, and into Cloud Run, and create a new service
- Select the container image, and select the image that was created in the previous step
    - Be sure that the container port is set to `5001` which is what is currently set in the `app.py` file