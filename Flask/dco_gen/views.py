from flask import Flask, render_template, request
from .models import EnvVar, Compose

app = Flask(__name__)
app.config['SECRET_KEY']    = 'iVu"D[%!N*ZL18K)s\rSW=@:s'
app.config['UPLOAD_FOLDER'] = '/static/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generator/interactif',methods = ['GET','POST'])
@app.route('/generator/interactif/',methods = ['GET','POST'])
def generate_compose():
    if request.method == 'POST':
        compose = Compose(request.form['service_name'],
                          request.form['logo_url'],
                          request.form['docker_image'],
                          request.form['service_link'],
                          request.form['service_description'],
                          request.form['maintainer_name'],
                          request.form['maintainer_github'])

        data = {
            'app_name'           : compose.app_name,
            'app_logo'           : compose.app_logo,
            'app_image'          : compose.app_image,
            'app_url'            : compose.app_url,
            'app_description'    : compose.app_description,
            'maintainer_name'    : compose.maintainer_name,
            'maintainer_github'  : compose.maintainer_github,
        }


        return render_template('template.html',**data)
    else:
        return render_template('interactive_form.html')

if __name__ == "__main__":
    app.run()