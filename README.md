# Complex NGINX microservices apps

Configure multiple streamlit apps in domain & subdomains using NGINX

- main_test (localhost)
- subdomain1 (app1.localhost)
- subdomain2 (app2.localhost)

## Common Python env

Set a common python env for all streamlit apps for simplicity purpose.
```bash
python3.10 -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
```

## Config

Open /etc/hosts and add entries `localhost`, `app1.localhost`, `app1.localhost` pointing to `127.0.0.1`

## Start

1. Run subdomain1
```bash
cd ./subdomain1
docker compose build
docker compose up
```
2. Run subdomain2
```bash
cd ./subdomain2
docker compose build
docker compose up
```
3. Run main
```bash
cd ./main_test
docker compose build
docker compose up
```
4. Access to `localhost`

## further work

Add DuckDNS, Letsencrypt & Certbot

### Work in progress

1. Add main domain in duckdns.org and get duckdns key
2. Create `/main_domain/.env` with appropiate values (based on `dotenv` sample)
3. In `/main_domain/nginx/conf.d/nginx.conf` set your domain in `server_name` section
4. Download letsencrypt script to create first certificate and set as executable
```bash
curl -L https://raw.githubusercontent.com/wmnnd/nginx-certbot/master/init-letsencrypt.sh > init-letsencrypt.sh
```
5. Before running script set `domains` and `email`, and check paths
6. Run
```bash
chmod +x ./init-letsencrypt.sh
./init-letsencrypt.sh
```
