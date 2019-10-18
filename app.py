import dash
from moesifwsgi import MoesifMiddleware
# from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy


app = dash.Dash(__name__,
                suppress_callback_exceptions=True,
                external_stylesheets=["url('/assets/boostrap.css')"]
)

server = app.server

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>{%title%}</title>
        <link href="/assets/_favicon.png" rel="icon" type="image/x-icon">
        {%css%}
        <!-- Facebook Pixel Code -->
        <script>
        !function(f,b,e,v,n,t,s)
        {if(f.fbq)return;n=f.fbq=function(){n.callMethod?
        n.callMethod.apply(n,arguments):n.queue.push(arguments)};
        if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
        n.queue=[];t=b.createElement(e);t.async=!0;
        t.src=v;s=b.getElementsByTagName(e)[0];
        s.parentNode.insertBefore(t,s)}(window,document,'script',
        'https://connect.facebook.net/en_US/fbevents.js');
         fbq('init', '1291977107642635'); 
        fbq('track', 'PageView');
        </script>
        <noscript>
         <img height="1" width="1" 
        src="https://www.facebook.com/tr?id=1291977107642635&ev=PageView
        &noscript=1"/>
        </noscript>
        <!-- End Facebook Pixel Code -->
    </head>
    <body>
        <header class="container">
    </header>
        <div></div>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
        <div></div>
    </body>
</html>
'''


moesif_settings = {
    'APPLICATION_ID': 'eyJhcHAiOiI2MTc6MjIxIiwidmVyIjoiMi4wIiwib3JnIjoiMjA3OjIzNCIsImlhdCI6MTU3MTAxMTIwMH0.vL8LqwLnVjAhfpV9JIgn1ZkAPSatTsEVIk9v8mfzq3M',
    'CAPTURE_OUTGOING_REQUESTS': False, # Set to True to also capture outgoing calls to 3rd parties.
    'LOG_BODY': True,
}

server.wsgi_app = MoesifMiddleware(server.wsgi_app, moesif_settings)

app.title = 'PLUKK'
