# CrawlMe
Extracting products url from www.snapdeal.com

## Getting Started

You can start by cloning and installing requirements.txt on your local env.
<br><br>

#### Prerequisites

You must be on linux or windows platform.
```
$ git clone https://github.com/krisskad/CrawlMe.git
$ pip install -r requirements.txt
```


#### Usage
You can simply use this django project on your local system as below
```
$ cd CrawlMe
$ python manage.py runserver
```
<br><br>

#### API Documentation
This API Works on two methods as below
1) GET : To get all available categories
2) POST : To get all the products of given category

* ####POSTMAN
```
GET REQUEST [http://127.0.0.1:8000/]
RESPONSE 
{
    "author": "krisskad",
    "email": "krishna.g.kadam98500@gmail.com",
    "example_request": {
        "category": "category_names"
    },
    "available_categories": [
        "mobile phones",
        "tablets",
        "mobile cases & covers",
        "sefie sticks & stands",
    ]
}
```

```
POST REQUEST [http://127.0.0.1:8000/] --> {"category":"tablets"}
RESPONSE 
{
    "Dell Streak Black ( Wifi Only , Voice calling )": "https://www.snapdeal.com/product/dell-streak-black-4g-wifi/640558071105#bcrumbLabelId:133",
    "Q Mi 10i 5G Aurora Metallic ( 4G + Wifi , Voice calling )": "https://www.snapdeal.com/product/q-mi-10i-5g-aurora/626096657340#bcrumbLabelId:133",
    "S Samsung M42 5G Grey ( 4G + Wifi , Voice calling )": "https://www.snapdeal.com/product/s-samsung-m42-5g-grey/667472305893#bcrumbLabelId:133",
    "Q Samsung 128GB Red ( Wifi Only , Voice calling )": "https://www.snapdeal.com/product/q-samsung-128gb-red-wifi/668909380332#bcrumbLabelId:133",
    "Vizio Vz-706 Speed 7 In Android Calling Tablet Pc - Black": "https://www.snapdeal.com/product/vizio-vz706-speed-7-in/648645063952#bcrumbLabelId:133",
    "VIZIO INDIA VIZIO-ZOOM TAB Silver ( 3G + Wifi , Voice calling )": "https://www.snapdeal.com/product/vizio-india-viziozoom-tab-silver/626619526254#bcrumbLabelId:133",
    "Vizio VZ 706 Keyboard Tab Black ( 3G + Wifi , Voice calling )": "https://www.snapdeal.com/product/vizio-vz-706-keyboard-tab/686545230881#bcrumbLabelId:133",
    "Vizio VZ 007 Maxx(2021) Black ( 3G + Wifi , Voice calling )": "https://www.snapdeal.com/product/vizio-vz-007-maxx2021-black/660019110229#bcrumbLabelId:133",
    "Vizio VZ  i7 Slide Max Black ( 3G + Wifi , Voice calling )": "https://www.snapdeal.com/product/vizio-vz-i7-slide-max/668073335994#bcrumbLabelId:133",
    "Vizio VZ Super Tech 118 Black ( 3G + Wifi , Voice calling )": "https://www.snapdeal.com/product/vizio-vz-super-tech-118/665254738138#bcrumbLabelId:133"
}
```


<br><br>

#### SHORT NOTE
<p align="center">
It will take time to respond back depends on the total number of products
</p>