# Chat Application with flask and streamlit
## Directories
- **back_end**: directory for flask back end
- **front_end**: directory for streamlit front end.
## Dockerfile:
- **Dockerfile.flask_app**: Dockerfile for creating flask app image.
- **Dockerfile.streamlit**: Dockerfile for creating streamlit app image.

## How to add additional python dependencies:
- **Step 1**: Add the dependencies in the requirements.txt file (front_end_requirements for streamlit and back_end_requirements for flask_app)
- **Step 2**: Rebuild the docker images using the following command:
```bash
docker compose up --build
```

## How to run?
- **Step 1**: Clone the repository.
- **Step 2**: Go to the root directory of the repository.
- **Step 3**: Run the following command to build the docker images.
```bash
docker compose up --build
```
- **Step 4**: Open the browser and go to the following link:
```bash
http://localhost:8501/
```
### Note that:
- Every time you make changes in the python code, you need to rebuild the docker images using the following command:
```bash
docker compose up
```
### Also Note that:
- You don't need to rebuild the docker image if you haven't changed any things related to environment. You can just run the following command:
```bash
docker compose up
#instead of
docker compose up --build
```

