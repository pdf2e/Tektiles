Current Development version of the Tektiles App for Textile Fabric Inc


1. Inorder for the package to work you must have python and django installed.

2. unpack the archive to your home directory
	$tar xf filename 

3. in your home directory issue:

	$python manage.py runserver
	
   3.1 
	This will start a local webserver at the loopback address on port 8000
	**alternative: you can specify the address and port by appending it to the end of the cmd 
	e.g. 
		$python manage.py runserver 10.0.1.25:8080

		note: The port you choose may be protected by the os and you may have to run as super user.

   3.2
	Once the server is running, test by opening your web browser and enter 127.0.0.1:8000/ this will 		show the boot page for the django app
