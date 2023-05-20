# Streamlit+Nginx docker apps

In this folder, I will make a demo for proxy server with 1 streamlit app1. The app exposes their service through port number `8503`, and Nginx server exposes to the port number `8890` in the demo.

Over the app, there is an nginx acting as api-gateway on app2.localhost (create entry in /etc/hosts) on port 82.

## run app dev mode
```bash
cd subdomain2/app
streamlit run app3.py --server.port 8503 --server.enableCORS false --server.baseUrlPath /app3
```

## build dockers and access
- Execute `docker-compose build`.
- Execute `docker-compose up`.
- Open your webbrowser and hit `app1.localhost:82/app3`. Also, you can check to hit `localhost:8890/app3`
