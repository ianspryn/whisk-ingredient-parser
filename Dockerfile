FROM mtlynch/crfpp

RUN apt-get update -y && \
    apt-get install -y git python2.7 python-pip

ADD . /app
WORKDIR /app

ENV PORT 8080

# Clean up.
RUN rm -rf /var/lib/apt/lists/* && \
    rm -Rf /usr/share/doc && \
    rm -Rf /usr/share/man && \
    apt-get autoremove -y && \
    apt-get clean
