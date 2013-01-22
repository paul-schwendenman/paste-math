paste-math
==========

A pastebin type application meant for displaying mathematics.

This project is designed use the MathJAX library for displaying MathML in
HTMl.  It is meant to allow users to post pages.  The pages will then be
able to be edited and viewed.  Additionally, there will be an admin
interface. 

Install GAE
-----------

To get this app running on google app engine you will have to download the
google app engine api.

Download and unzip::

    cd ~
    mkdir google_projects
    cd google_projects
    wget -O gae.zip http://googleappengine.googlecode.com/files/google_appengine_1.7.1.zip
    unzip gae.zip
    rm gae.zip

Next you can create and start the development server::

    cp -r google_appengine/new_project_template testapp
    python google_appengine/dev_appserver.py testapp


Run the app locally
-------------------

::

	python ~/google_projects/google_appengine/dev_appserver.py myapp/

Upload the app
--------------

::

	python ~/google_projects/google_appengine/appcfg.py update myapp/


