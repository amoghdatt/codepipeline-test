FROM python:3.6
RUN apt-get update && \
    apt-get install -y && \
    apt-get install build-essential && \
    pip install flask pandas cython && \
    pip install pymssql && \
    pip install pytest
ADD run.py /usr/src/profile/
ADD test.py /usr/src/profile/
EXPOSE 5000
WORKDIR /usr/src/profile/
CMD python run.py