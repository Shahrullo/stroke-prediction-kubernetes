## How to run 
### Train the model and get model weights
create conda or any other virtual environment. We will use conda
`conda create -n stroke_kubernetes python==3.10`
`conda activate stroke_kubernetes`
 install the required libraries
`pip install -r requirements.txt`

`python ml_pipeline.py`

### Custom inference
`python app.py`

go to `http://127.0.0.1:5000/apidocs`

### Build the docker image
`docker build -t stroke-prediction:v1 .`
### Run the docker image and do prediction
`docker run --rm -it -p 5000:5000 stroke-prediction:v1`
