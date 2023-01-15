from flask import Flask, render_template, request
from .models import EnvVar, Compose, Volume, Port

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
        EnvVar.items = []
        Port.items   = []
        Volume.items = []

        compose = Compose(request.form['service_name'],
                          request.form['logo_url'],
                          request.form['docker_image'],
                          request.form['service_link'],
                          request.form['service_description'],
                          request.form['maintainer_name'],
                          request.form['maintainer_github'])

        nb_envvar  = int(request.form['env_cpt'])
        nb_volumes = int(request.form['volume_cpt'])
        nb_ports   = int(request.form['port_cpt'])

        if nb_envvar > 0:
            for envvar_cpt in range(1,nb_envvar+1):
                new_var_name        = request.form[f'env_name_{envvar_cpt}']
                new_var_hint        = request.form[f'env_hint_{envvar_cpt}']
                new_var_description = request.form[f'env_description_{envvar_cpt}']
                new_var_default     = request.form[f'env_default_{envvar_cpt}']
                new_var = EnvVar(new_var_name,new_var_hint,new_var_description,new_var_default)
                EnvVar.items.append(new_var)
                print(new_var.__dict__)
            compose.envvar = EnvVar.items
            print(EnvVar.items)

        if nb_volumes > 0:
            for volume_cpt in range(1,nb_volumes+1):
                new_volume_name      = request.form[f'volume_name_{volume_cpt}']
                new_volume_container = request.form[f'volume_container_{volume_cpt}']
                new_volume = Volume(new_volume_name,new_volume_container)
                Volume.items.append(new_volume)
            compose.volumlist = Volume.items

        if nb_ports > 0:
            for port_cpt in range(1, nb_ports+1):
                new_port_number = request.form[f'port_{port_cpt}']
                new_port = Port(new_port_number)
                Port.items.append(new_port)
            compose.app_ports = Port.items

        data = {
            'app_name'           : compose.app_name,
            'app_logo'           : compose.app_logo,
            'app_image'          : compose.app_image,
            'app_url'            : compose.app_url,
            'app_description'    : compose.app_description,
            'maintainer_name'    : compose.maintainer_name,
            'maintainer_github'  : compose.maintainer_github,
            'volumlist'          : compose.volumlist,
            'envvar'             : compose.envvar,
            'app_ports'          : compose.app_ports
        }

        return render_template('template.html',**data)
    else:
        return render_template('interactive_form.html')

if __name__ == "__main__":
    app.run()