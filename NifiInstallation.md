# This explanation is from videos
# step 1 
⚠ For nifi installation, make sure you have the latest version of java installed on your computer. if not installed, download from here
https://www.oracle.com/tr/java/technologies/javase-jdk11-downloads.html

# step 2
➡ watch this video for windows nifi installation.
https://www.youtube.com/watch?v=nplzhAKmH-s&t=527s

# step 3
🔹 I will import my data into nifi from mssql.I will connect with my ip address. for this you can watch this video if the port is not open.
![1_xnSNfPfsEllTjNwbIVe0IA](https://user-images.githubusercontent.com/58874305/125337470-e3221200-e303-11eb-9823-968161514e87.png)
https://www.youtube.com/watch?v=2kODgaYhlNQ

# step 4
If we opened the port, we can make our sql connection. In this video, the connection string is shown well, but there is a shortcoming before that. The parts I marked with purple need to be filled with your sql information.
https://www.youtube.com/watch?v=fuEosO24fgI&t=6s
![1_wXWBLTEys8J-LQ1NcHPGNw](https://user-images.githubusercontent.com/58874305/125338208-c63a0e80-e304-11eb-935e-48e8d22037ea.png)

# step 5
🔹First, we need to make arrangements so that we can use our data.
![1_bxtD6sSg14J1ylqtgb_pbg](https://user-images.githubusercontent.com/58874305/125338526-2761e200-e305-11eb-87a7-c0f45d6978ee.png)
nifi will ask us for interrogation. Since I know that there are Orders in my data, I write the query as select * from Orders.
![1_JfZ-x-HREf6UWhSCr0ZOCQ](https://user-images.githubusercontent.com/58874305/125338551-3052b380-e305-11eb-8829-61f93d00f262.png)

1) ![1_e-tJrol16AeaQ_4waSevuQ](https://user-images.githubusercontent.com/58874305/125339256-fa61ff00-e305-11eb-84ce-d73a7ebc6271.png)
When we click on it and select the enable box in the lower right corner, our data will now begin to come.
2) ![1_GuwwVxltjWxSR2hNMqmjvQ](https://user-images.githubusercontent.com/58874305/125339289-0483fd80-e306-11eb-8899-c6621567e501.png)


