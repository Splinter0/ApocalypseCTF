FROM python:3.8-alpine

# Add user
RUN adduser -D -u 1000 -g 1000 -s /bin/sh www

# Install system dependencies
RUN apk add --update --no-cache nginx supervisor uwsgi-python3 chromium terminus-font supervisor

# Upgrade pip
RUN python -m pip install --upgrade pip

# Setup app
RUN mkdir -p /app
WORKDIR /app

# Add application
COPY challenge .
RUN chown -R www /app/application/static/pdfs/

# Install dependencies
RUN python -m venv venv
RUN . /app/venv/bin/activate && pip install -r requirements.txt

# Fix permissions
RUN chown -R www:www /var/lib/nginx

# Copy configs
COPY config/supervisord.conf /etc/supervisord.conf
COPY config/nginx.conf /etc/nginx/nginx.conf

# Expose port the server is reachable on
EXPOSE 80

# Disable pycache
ENV PYTHONDONTWRITEBYTECODE=1

# Run supervisord
ENTRYPOINT [ "/usr/bin/supervisord", "-c", "/etc/supervisord.conf" ]