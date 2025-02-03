This is a github page for a HNG task to get interesting information about a number
# Installation
# Usage
# Result

# Installation
- To install the app, clone the github file into your local directory and run the setup file to install all needed dependecies and nginx.
- Using gunicorn run the following command on a different terminal within the home directory "gunicorn -w 4 main:app" to start the flask app.
- Comment out the nginx default configuration present in /etc/nginx/sites-available/default and add the following lines
<!-- 
  server {
    listen 80;
    server_name _;

    location / {
      proxy_pass http://127.0.0.1:8000/;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header X-Forwarded-Proto $scheme;
      proxy_set_header X-Forwarded-Host $host;
      proxy_set_header X-Forwarded-Prefix /;
    }
  } 
-->
- restart nginx using 'systemctl restart nginx' then enable it using 'systemctl enable nginx'

# Usage
The app can be used with the following http code
<!--
  http://toluairbnb.tech/api/classify-number?number=<YOUR NUMBER>
-->

# Result
using http://toluairbnb.tech/api/classify-number?number=900 the result should equal

<!-- 
  {
  "digit_sum": 9,
  "fun_fact": "900 is a boring number.", \\ May change
  "is_perfect": false,
  "is_prime": false,
  "number": 900,
  "properties": [
    "not armstrong",
    "even"
  ]
} 
-->
