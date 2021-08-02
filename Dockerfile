FROM python:3.6.5

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

# Add the files 

#COPY data .
COPY model_python.pkl .
#COPY templates .
COPY app.py .

# Run the application:
COPY app.py .
COPY wsgi.py .
#CMD ["python", "app.py"]
#CMD ["flask","run"]


# Expose is NOT supported by Heroku
#EXPOSE 5000

#ENTRYPOINT ["python app.py"]
# Run the app.  CMD is required to run on Heroku
# $PORT is set by Heroku
CMD gunicorn --bind 0.0.0.0:$PORT wsgi
#CMD ["python", "app.py"]