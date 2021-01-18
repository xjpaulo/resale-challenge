FROM 3.8.7-alpine3.12

RUN apk add --virtual .build-dependencies \ 
            --no-cache \
            python3-dev \
            build-base \
            linux-headers \
            pcre

WORKDIR /var/www/resale-challenge
RUN mkdir -p /var/www/resale-challenge/app
COPY ./app /var/www/resale-challenge/app
COPY requirements.txt /var/www/resale-challenge
RUN pip3 install -r requirements.txt
WORKDIR /var/www/resale-challenge/app
RUN apk del .build-dependencies && rm -rf /var/cache/apk/*

EXPOSE 8080
CMD ["uwsgi", "--ini", "/var/www/resale-challenge/app/wsgi.ini"]