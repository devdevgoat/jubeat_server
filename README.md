
# Setup
1. Git Pull bemaniutils
2. Create venv
3. Install requirements file
4. Update the following files to match your system:
    - uwsgi/_app.skel
        -- virtualenv = /opt/ju_services/venv -> the newly created venv
        -- chdir = /opt/ju_services/bemaniutils -> to where ever you pulled bemaniutils down too
    - emperor.ini
        -- emperor = /opt/ju_services/uwsgi -> to the working directory where your other vassal ini files are in
    - emperor.uwsgi.service:
        -- ExecStart=/usr/bin/uwsgi --ini /opt/ju_services/uwsgi/emperor.ini -> to the same workign direcotry as the emporor.ini file above
    - all nginx/*.conf files
        -- alias  /opt/ju_services/static/; -> to the static directory
        -- include     /opt/ju_services/extras/uwsgi_params; -> to the extras directory
5. Setup Symbolic Links:
    - all files in nginx need to link to /etc/nginx/sites-enabled
        -- sudo ln -sf /opt/ju_services/nginx/*.conf /etc/nginx/sites-enabled
6. Copy the following files (symbolic links will result in having to manually start the service)
    - sudo cp emperor.uwsgi.service /etc/systemd/system
    - systemctl enable emperor.uwsgi.service

# Chagnes to the BemaniUtils repo:

1. Update /bemani/frontend/app.py#L32-L33 so that nginx can properly load the webui
    -    # static_folder=static_location -> static_folder="static"
2. Update local /config/server.yaml with settings needed. ignore the port setting as we've dealth with that via nginx.confs
3. Copy local /config/server.yaml to /opt/ju_services/bemaniutils/bemani/wsgi, this bc the wsgi's in the repo use a relative import and this is easier than updated 3 files


# Notes

- NGINX Error means the uwsgi isn't running, or the socket file doesn't have the correct permissions
- Services OK but the game doen't connect? The server file defaults to port 80 but suggest 5730 in the services run command, also I prefer 80 for the front end app, so change the server.yaml port number to 5730 and restart emperor.