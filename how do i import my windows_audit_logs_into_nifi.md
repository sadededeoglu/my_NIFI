1) first one let's make the nifi and minifi connect. nifi/conf/nifi.properties file opens for this.the following operations are performed. The ip address must be the ip address where the nifi is running.

# Site to Site properties
nifi.remote.input.host=167.71.171.96
nifi.remote.input.secure=false
nifi.remote.input.socket.port=1234
nifi.remote.input.http.enabled=true
nifi.remote.input.http.transaction.ttl=30 sec
nifi.remote.contents.cache.expiration=30 secs

2) run nifi as administrator!

3) ConsumeWindowsEventLog, this processor knows where the audit logs in windows are and takes it from there. I chose to get system logs here. you can choose security logs if you want.

![image](https://user-images.githubusercontent.com/58874305/127830231-6032be01-c113-43aa-b1b6-d38e15fbe3e8.png)

3) logs are now in nifi. now i create a port to use them inside the system.I created a remote process group and added the ip address where nifi is running.now we have our logs and a port to deploy them.

![image](https://user-images.githubusercontent.com/58874305/127831042-e2f76d7f-c62c-4b9b-850d-188201b6fb21.png)

4)To use the logs, we need to get it from that port. I am creating an input port for this.

![image](https://user-images.githubusercontent.com/58874305/127831752-6980760d-44ba-40c0-b564-08174c146c50.png)

5)At this point we have data. we have the port and we have the input. Now we can connect.

![image](https://user-images.githubusercontent.com/58874305/127832471-ad68a048-e53f-4480-86f0-99e4d8cbeced.png)

6)we have to use minifi toolkit to use it this way.this is because this template minifi is made into a config file that can be used.this template is saved.and cmd opens.
Go to where the toolkit is installed.

![image](https://user-images.githubusercontent.com/58874305/127841354-57987ace-fd45-4e7c-8635-b996325605b4.png)

7)Now we can run it. We can do whatever we want on the logs.

![image](https://user-images.githubusercontent.com/58874305/127842288-0c23bacf-6730-4217-91dc-ec75b2052f0e.png)

