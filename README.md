Plukk App - Minimum Viable Product
=
A simple Dash app meant to serve as a prototype for our "Practical entrepreneurship" class. Utilizes an e-mail form to gauge interest.
The Flask server is run on Heroku with a Postgres database.

You can see the result here: https://www.plukkappen.no.

## File structure

#### Main files
- app.py (Declares app and server settings)
- index.py (Runs the app)
- __app__
    - resources.py (Interactive components of app, as well as finished forms)
    - layout.py (Structure of the page)
- __assets__
    - __images__
        - image files
    - bootstrap.css (Customized bootstrap CSS file)

#### Other files
- requirements.txt
- config.py (Heroku server settings)
- Procfile (Heroku server settings)
- runtime.txt (Heroku server settings)



