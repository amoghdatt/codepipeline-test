FROM python:3.6
RUN apt-get update && \
    apt-get install -y && \
    apt-get install build-essential && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update -y && \
    ACCEPT_EULA=Y apt-get install msodbcsql17 -y && \
    ACCEPT_EULA=Y apt-get install mssql-tools -y && \
    echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile && \
    echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc && \
    . ~/.bashrc && \
    apt-get install unixodbc-dev -y && \
    pip install flask pandas cython && \
    pip install pymssql flask_sqlalchemy pyodbc && \
    pip install pytest

ADD run.py /usr/src/profile/
ADD test.py /usr/src/profile/
EXPOSE 5000
WORKDIR /usr/src/profile/
CMD python run.py