# django-channels-tutorial
Following the tutorial for Django Channels


### Virtual Environment
It is strongly recommended to use a Python virtual environment. To create a virtual env, use the venv feature of python3. Run the command below in the root project directory. Recommended folder name for the virtual environment is env.
```
python3.6 -m venv --without-pip <env-folder-name>
```


To activate that virtual environment, use the command:
```
source <env-folder-name>/bin/activate
```

After activating, to install the dependencies run
```
pip install -r requirements.txt
```

### Other dependencies
 - Install python3.6
 - Install python3.6-dev
 - Create python3.6 venv without pip to avoid error
 - Curl pip and install after activating venv (`curl https://bootstrap.pypa.io/ez_setup.py -o - | python3.6 && python3.6 -m easy_install pip`)
 - Deactivate and reactivate venv
 - Install django and channels