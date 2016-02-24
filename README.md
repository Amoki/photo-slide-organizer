photo-slide-organizer
=====================

Install
---------
* `git clone git@github.com:Amoki/photo-slide-organizer.git` : retrieve the repo
* `cd photo-slide-organizer`
* `virtualenv -p python3 --no-site-packages .v_env` : create a virtual-env for python code
* `source .v_env/bin/activate` : activate the v_env
* `pip install -r requirements.txt` : install all requirements
* `./manage.py migrate` : migrate DB
* `./manage.py createsuperuser` : add your own admin.


----------
## In development
#### Start the server
```bash
pyhton manage.py runserver <ip:port>
```
