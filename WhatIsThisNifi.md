# What is this Nifi

✔Moving data from point to point.
✔Doing various conversions.
✔It is used to automate jobs that need to run regularly.
✔It can also be used as nifi ETL tool.

# What is this ETL TOOL

✔Receiving data from a source system(extract).
✔After certain processes(transform).
✔The target is to transferred to a system(load).

![image](https://user-images.githubusercontent.com/58874305/125286552-c8827580-e2d0-11eb-8217-582e8c9ca6b8.png)

# INSIDE NIFI

![image](https://user-images.githubusercontent.com/58874305/125287538-e69ca580-e2d1-11eb-90d3-318d3545d9f9.png)

# PROCESSOR GROUP
✔multiple processors together.Used to manage data flow well.

# İNPUT-OUTPUT PORT
✔It allows importing and exporting data contained in other remote Process Group.

# HUNNEL
✔It is used to combine data from several Connections into one Connection.

# PROCESSORS

✔Processors form the basis of creating the data flow. operations such as receiving, transforming, querying and sending data can be done.

![image](https://user-images.githubusercontent.com/58874305/125288802-65461280-e2d3-11eb-80f5-5e0544c0d9fa.png)

# SETTING THE EXECUTE PROCESSOR

![image](https://user-images.githubusercontent.com/58874305/125335531-83c30280-e301-11eb-9756-a8e891008da3.png)


# SAMPLE DATA FLOW

![image](https://user-images.githubusercontent.com/58874305/125289196-d1287b00-e2d3-11eb-9a3c-8350af2708e9.png)

🔶PURPOSE OF THE FLOW: It is to parse the data in the SQL database and GenerateFlowFile with regex, create a data flow and save it to another location in json format.

![image](https://user-images.githubusercontent.com/58874305/125291912-c3c0c000-e2d6-11eb-82b0-b10f0345e658.png)

![image](https://user-images.githubusercontent.com/58874305/125293748-8fe69a00-e2d8-11eb-9a7d-56f6a5b58d06.png)





