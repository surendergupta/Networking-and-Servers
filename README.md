# Networking-and-Servers
Assignment on Networking and Servers
**Question 1:**

1. First Install the virtual box and instal ubuntu on it.
2. After installation of ubuntu to install nginx server open terminal
3. Step of NGINX Server
	3.1 sudo apt-get update
	3.2 sudo apt-get install nginx -y
4. sudo mkdir -p /var/www/awesomeweb/html 		(create awesomeweb folder inside www directory –p tag used for parent folder )
5. cd /var/www/awesomeweb/html
6. sudo chown -R $USER:$USER /var/www/awesomeweb/html 		(Ownership permission set to user )
7. sudo chmod -R 755 /var/www			(www folder give read write and execute permission)
8. nano /var/www/awesomeweb/html/index.html	(create the index.html file)
9. create basic structure of website home page and save it
Index.html file
```
<html>
<head>
<title>Awesomeweb</title>
</head>
<body>
<h1>Welcome to awesomeweb best template website portal.</h1>
</body>
</html>
```

10. sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/awesomeweb
11. sudo nano /etc/nginx/sites-available/awesomeweb
	11.1 change root path with /var/www/awesomeweb/html
	11.2 Update server_name awesomeweb
	11.3 file save and close it
12. sudo ln -s /etc/nginx/sites-available/awesomeweb /etc/nginx/sites-enabled/
13. sudo rm /etc/nginx/sites-enabled/default
14. sudo nano /etc/nginx/nginx.conf
	14.1 uncomment the server_names_hash_bucket_size 64;
	14.2 file save and close it
15. sudo service nginx restart
16. sudo nano /etc/hosts
	16.1 update ip_address and domain_name like 127.0.0.1 awesomeweb
	16.2 file save and close it
17. Open browser and type: http://awesomeweb

**Question 2:**

1. subdomainlist.txt
2. domaincheck.py
3. setup crontab -e
4. ```* * * * * /usr/bin/python3 /home/vboxuser/python/subdomaincheck.py```
