# Streamlit+Nginx docker apps

In this repository, I will make a demo for proxy server with streamlit application. The application exposes their service through port number `8501`/`8502`, and Nginx server exposes to the port number `8888`/`8889` in the demo.

Then, you can see Streamlit application with `localhost:8888` in your webbrowser. Of course, it is possible to run the application with `localhost:2022` due to the fact that I did not set any blocking other port numbers in Nginx configuration.

## run app dev mode
```bash
cd subdomain1/app
streamlit run app1.py --server.port 8501 --server.address 0.0.0.0 --server.enableCORS false --server.enableXsrfProtection false --server.baseUrlPath /app1
streamlit run app2.py --server.port 8502 --server.address 0.0.0.0 --server.enableCORS false --server.enableXsrfProtection false --server.baseUrlPath /app2
```

## build dockers
- Execute `docker-compose build`.
- Execute `docker-compose up`.
- Check the logs which are running at Streamlit application. It runs `http://0.0.0.0:2022`
- Open your webbrowser and hit `localhost:8888/app1`. Also, you can check to hit `localhost:2022`
- Open your webbrowser and hit `localhost:8889/app2`. Also, you can check to hit `localhost:2022`

## Source
- The original code for Streamlit application is from this [repository](https://github.com/streamlit/release-demos), and its [License](https://github.com/streamlit/release-demos/blob/master/LICENSE).
