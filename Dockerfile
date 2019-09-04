FROM nginx
ARG AUTHOR
ENV AUTHOR=$AUTHOR

WORKDIR /usr/share/nginx/html
COPY . /usr/share/nginx/html

CMD nginx -g 'daemon off;'

EXPOSE 80
