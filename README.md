# Complex NGINX microservices apps

Configure multiple streamlit apps in domain & subdomains using NGINX, DuckDNS, Letsencrypt & Certbot

- main_domain (loshz.duckdns.org)

- subdomain1 (app1.loshz.duckdns.org)

- subdomain2 (app2.loshz.duckdns.org)

This work is based on this documents:
- `https://pentacent.medium.com/nginx-and-lets-encrypt-with-docker-in-less-than-5-minutes-b4b8a60d3a7`


## Step 1: configure main_domain

1. Add main domain in duckdns.org and get duckdns key
2. Create `/main_domain/.env` with appropiatte values
3. In `/main_domain/nginx/conf.d/nginx.conf` set your domain in `server_name` section
4. Download letsencrypt script to create first certificate and set as executable
```bash
curl -L https://raw.githubusercontent.com/wmnnd/nginx-certbot/master/init-letsencrypt.sh > init-letsencrypt.sh
```
5. Before running script set `domains` and `email`, and check paths

