FROM python:3.5

RUN apt-get update \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


RUN groupadd -g 799 nby2003 && \
    useradd -r -u 999 -g nby2003 nby2003

# Set up a working folder and install the pre-reqs
WORKDIR /app

RUN pip install Flask
RUN pip install Requests

USER nby2003

COPY --chown=nby2003:nby2003 . .

CMD [ "python", "./Fs.py" ]
