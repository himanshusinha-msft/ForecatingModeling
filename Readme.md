
## Problem 

We are in the business of  helping external customer and it frequently   happens that due to new feature roll outs , outages, a user(s) is working a integration  etc , question on the  community forum increases and we run into capacity issues on our side .

### Solution 
The intend here was to create a forecasting model for our ticketing data , with an confidence that this help us predict the future tickets . This prediction will help us plan capacity issues . Also it will also show as "lean" period which will help us better plan our resources .  We do have the historical data for the last three years . The way our data was we had daily data for each day. 

We are using the 
* Spark on Azure datarbicks 
* Pandas 
* [Prophet package for forecasting](https://facebook.github.io/prophet/) 
![image](https://user-images.githubusercontent.com/47539458/191912302-c6d029a2-6e45-49bb-ae4e-b35071b26e6f.png)


![image](https://user-images.githubusercontent.com/47539458/191910421-286723e3-4e22-49e2-a6d8-e07004363542.png)

![image](https://user-images.githubusercontent.com/47539458/191910471-4d0c898c-1262-40f1-9763-37b2ad32a34b.png)

![image](https://user-images.githubusercontent.com/47539458/191910502-73bf8ea5-3023-4e22-96a1-d8fe24707f36.png)

![image](https://user-images.githubusercontent.com/47539458/191910561-35e7d475-d9c3-48ed-aae2-6a3a1c673420.png)

![image](https://user-images.githubusercontent.com/47539458/191910593-bf9106cb-9eaa-4ac2-bfab-c9071da35e8f.png)

![image](https://user-images.githubusercontent.com/47539458/191910615-862eb71f-adac-4841-8b3b-573c57a05624.png)


* Case 1 : 
The  below graph does shows the prediction for the whole team .

![image](https://user-images.githubusercontent.com/47539458/191910856-0dc3f200-e4de-4385-8ba9-8b8c3ecd6a93.png)

* Case 2 : 
The  below graph  shows the prediction for the sub-team. The trend is positive 
![image](https://user-images.githubusercontent.com/47539458/191911308-3c552216-7635-46ad-bf15-fab0864d3969.png)

* Case 3 : 
The  below graph  shows the prediction for the sub-team. The trend is negative and as you can see the volume is going down  

![image](https://user-images.githubusercontent.com/47539458/191911359-0149a080-eabb-4abd-b133-02f95f1e39b3.png)


 