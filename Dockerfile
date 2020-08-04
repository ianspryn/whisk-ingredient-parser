FROM mtlynch/crfpp

RUN apt-get update -y && \
    apt-get install -y git python2.7 python-pip

RUN pip install Flask gunicorn

ADD . /app
WORKDIR /app

ENV PORT 8080

# Clean up.
RUN rm -rf /var/lib/apt/lists/* && \
    rm -Rf /usr/share/doc && \
    rm -Rf /usr/share/man && \
    apt-get autoremove -y && \
    apt-get clean

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app