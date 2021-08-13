# How do we send data to another nifi with nifi?

In this flow, we will take the windows audit logs and send them to another nifi.We will use minifi for this process.
minifi is the agent that allows them to communicate with each other.

1) First we need to download minifi and minifi toolkit.
2) We need to open a port in the target nifi. first we need to go to the "nifi-1.13.2\conf " directory and do the following operations.
3) Here we open the nifi.properties file.

![image](https://user-images.githubusercontent.com/58874305/129353531-1cd6c3e0-e1d7-4a47-808a-53e5411b5a54.png)

4)We fix and save these parts. 
5)nifi is restarted and run.We will use a remote processor.The preset 1234 port doesn't matter. It will understand port 8080 and convert it to 1234.

![image](https://user-images.githubusercontent.com/58874305/129353939-6ae1a535-2444-48f8-b3cd-dd9463b7a02d.png)

6)After making the adjustments,We have enabled the remote processor, our port is now open. We add an input port for the data to come here .

![image](https://user-images.githubusercontent.com/58874305/129354572-934aba34-8c08-4cfe-86b7-9f00bf4d00cf.png)

7)now we have to edit the nifi which will send the data. 
8)After doing the steps 3-4-5, we add the ConsumeWindowsEventLog processor. (we will use nifi's ConsumeWindowsEventLog processor to get windows logs)
9)Now we specify the port to send by adding a remote processor and we save this template.

![image](https://user-images.githubusercontent.com/58874305/129355131-7dab8feb-6b49-426d-966f-eb6c412dc458.png)












