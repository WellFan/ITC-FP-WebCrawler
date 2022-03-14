# ITC-FP-WebCrawler

## Submission Date: 
Fall 2019

## Overview
This is the final project of Introduction-to-Computer-Science course (CSIE1000, Fall 2019) from National Taiwan University.

In this project, we develope a basic program to crawl data from the news page of our department.([link](https://www.csie.ntu.edu.tw/news/)) There are two key modules to implement this function, namely lxml and request in python. With the aid of them, we could, conveniently, capture html objects from web page and parse them.

Please refers to [homework spec](./hw_spec.pdf) or check TA's repo ([link](https://github.com/kaikai4n/ItC-python-hw-sample-code)) for project specification.

## Environment Setup
Please run the code on window10.

## Usage
```sh
# input format
python main.py --start-date <Year>-<Month>-<Date> --end-date <Year>-<Month>-<Date>
# example
Python main.py --start-date 2022-02-20 --end-date 2022-03-10
```
The default output file is `output.csv`.

## Program Explanation

There are 3 python files in the repository, `main.py`, `args.py`, and `crawler.py`. I will explain the logic of each program as the order.

### main.py

First, the main program will call get_args() in args.py to retrieve parsed arguments. Second, it will pass date arguments to crawler() in crawler.py and obtain a result list. Finally, it will format the content of result list to genereate the csv file. The psuedoCode of main.py is as follows.

```py
arguments = get_args()
result_list = crawler(arguments.date)
f = open(arguments.outputName)
for date, title, content in result_list:
    f.write(resultFormat(date, title, content))
```

### args.py
 The args.py handled three arguments, inclusive of output filename, start date, and end date, then format these arguments for further instructions. 

### crawler.py
 On receiving the time interval to crawl, the crawler.py captured details of each post, including posting dates, title and content, in specified time interval. And returned the packed information about each post in list. Note that xpath is adopted to capture html objects in the webpage.

 ## Contribution
| Contributor | Department | Student Id | Contribution                          |
| ----------- | ---------- | ---------- | ------------------------------------- |
| 樊惟祐      | 物理二     | B06202023  | managed github commits                |
| 楊淳竣      | 資工一     | B08902137  | developed the crawler program         |
| 王繹喆      | 資工一     | B08902120  | managed the progress of each tasks    |