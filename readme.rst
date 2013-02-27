paste-math
==========

A pastebin type application meant for displaying mathematics.

This project is designed use the MathJAX library for displaying MathML in
HTML.  It is meant to allow users to post pages.  The pages will then be
able to be edited and viewed.  Additionally, there will be an admin
interface. 



Install GAE
-----------

To get this app running on google app engine you will have to download the
google app engine api.

Download and unzip::

    mkdir ~/google_projects
    update-gae !$


Or you could use the following after checking for the newest version, but
make sure you check the sha1sum::

    cd google_projects
    wget -O gae.zip http://googleappengine.googlecode.com/files/google_appengine_1.7.4.zip
    unzip gae.zip
    rm gae.zip

Next you can create and start the development server::

    cp -r google_appengine/new_project_template testapp
    python google_appengine/dev_appserver.py testapp


Run the app locally
-------------------

::

	python ~/google_projects/google_appengine/dev_appserver.py ~/paste-math/

Upload the app
--------------

::

	python ~/google_projects/google_appengine/appcfg.py update ~/paste-math/


Update the GAE SDK
-------------------

Use the script to update the sdk::

	update-gae ~/google_projects


Or check the version from https://developers.google.com/appengine/downloads. Then update using::

	cd ~/google_projects
	rm -r google_appengine
	wget -O gae.zip http://googleappengine.googlecode.com/files/google_appengine_1.X.X.zip
	sha1sum gae.zip
	unzip !$
	rm !$




Logs
----

GAE will also allow the download of log files::

	python ~/google_projects/google_appengine/appcfg.py request_logs -n 0 -e u@d.c -a ~/paste-math/ ~/paste-math/log.txt
