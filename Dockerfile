FROM python:3.11.0

# set the working directory in the container
WORKDIR /weather-app

# ADD the file to execute on the current directory
COPY weather.py .

# install dependencies requests
RUN pip3 install --no-cache-dir requests==2.28.2

# command to run on container start
CMD [ "python3", "weather.py" ]
# CMD ["sh", "-c", "python3, weather.py API_KEY LAT LONG" ]

