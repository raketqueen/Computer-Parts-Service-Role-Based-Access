# Use official Nginx image
FROM nginx:latest

# Remove default config
RUN rm /etc/nginx/conf.d/default.conf

# Copy our Nginx config into the container
COPY nginx.conf /etc/nginx/conf.d/

# Expose port 80
EXPOSE 80
