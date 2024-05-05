# AN IMPORTANT NOTICE

Due to a major update in Huggingface, the ChatBot option isn't functioning. To understand the entire thing and how it works, here is the tutorial that will help you to get idea about this amazing project.

```bash
https://youtu.be/A23aHxtiApw?si=e3qVegqD30mOro4w
```

The Good thing is another version of this ML project is still online, you can try here:

```bash
https://www.startech.com.bd/tool/finder
```

# laptop-guru
This ML Model will help you to choose the desired laptop based on your given information. 

# Problem Statement

In student life or professional life, almost 95% of people struggle to buy the best laptop according to their demands & purposes. Some of them ended up buying underpowered laptops based on their work & activities. Some of them ended up buying overpowered laptops. It's the kind of thing that, we must confuse to buy the best laptop among the thousands of laptops in the market. To solve this issue, I introduced to you the Laptop Guru ML Recommendation System. Just put your desired specifications & working purposes & it will suggest the best laptop for you. 

# A-Z Process of Building Laptop Guru

## Choosing the Appropriate Model

In this case, **distilroberta-base ** model has been chosen for this ML project. Even though 2000 Laptops sound a lot but in ML world, it's very tiny dataset. To efffectively the tiny dataset, **distilroberta-base ** is the best for this. To understand more check out this link:
```bash
https://huggingface.co/distilroberta-base
```
## Sites that I have scrapped to collect data

I have choosen this site that contain 4k laptops dataset for this ML projects:
```bash
https://www.startech.com.bd/laptop-notebook/laptop
```
###process of scraping & data saving
1. Go to Scraped_data folder
2. Open details_scraper.py
3. run this command:
   ```bash
   python -u details_scraper.py
   '''
  After couples of hours you will get desired data. 

## Model Training
To understand the entire process, there is a file, please run it at your machine:
```bash
python -u text_Data_trainer_with_blurr.ipynb
```

I am using transformer blurr package to train this model. 

## Training accuracy
<img src="https://github.com/darkangrycoder/laptop-guru/blob/main/Annotation%202023-10-17%20133222.png" alt="Stage_0_Training_Image" width="200"/>
<img src="https://github.com/darkangrycoder/laptop-guru/blob/main/Annotation%202023-10-17%20133222.png" alt="Stage_0_Training_Image" width="200"/>

## Understand How to use
```bash
https://youtu.be/A23aHxtiApw
```
## Huggingface Deployment
```
https://huggingface.co/spaces/tdnathmlenthusiast/laptop_guru
```
