# Streamlit+Nginx docker apps

In this folder, I will make a demo for proxy server with 2 streamlit apps. The apps exposes their service through port number `8501`/`8502`, and Nginx server exposes to the port number `8888`/`8889` in the demo.

Over the 2 apps, there is an nginx acting as api-gateway on app1.localhost (create entry in /etc/hosts) on port 81.

## run app dev mode
```bash
cd subdomain1/app
streamlit run app1.py --server.port 8501 --server.enableCORS false --server.baseUrlPath /app1
streamlit run app2.py --server.port 8502 --server.enableCORS false --server.baseUrlPath /app2
```

## build dockers and access
- Execute `docker-compose build`.
- Execute `docker-compose up`.
- Open your webbrowser and hit `app1.localhost:81/app1`. Also, you can check to hit `localhost:8888/app1`
- Open your webbrowser and hit `app1.localhost:81/app2`. Also, you can check to hit `localhost:8889/app2`
