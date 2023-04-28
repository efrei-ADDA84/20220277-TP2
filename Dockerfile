FROM python:3.11.0

# set the working directory in the container
WORKDIR /weather-app

# ADD all files 
COPY . .

# install required dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# command to run on container start
CMD [ "python3", "weather.py" ]

