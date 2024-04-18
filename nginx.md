Directives:
    1- Simple Directive that ends with semicolon;
    2- Block Directive that consists of {}

Contexts:
    There are four main contexts in nginx:
        1- events { } : this context is used for setting global configuration regarding how NGINX is going to handle requests on general level.
        2- http { } : this context is used for defining configurations regarding how  servers is going to handle HTTP & HTTPS requests.
        3- server { } : it's a nested contexted inside the http context and configuring a specific virtual server in a single host.
        4- main : is the configuration file itself, anything is written outside the above 3 context is in the main context.


nginx.config:
http {
    server {
        listen 80;  # Directive
    }

    server {
        listen 8080;
    }
}
