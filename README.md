# Web-API

This project repository is a web based calculator API that leverages Python and Flask to perform standard mathemical calculations such as addition, subtraction, multiplication and division.

# API usage

This API is hosted at the following URL: ~~https://calcapp.herokuapp.com/results~~

This API has two endpoints:
- /operate
- /results

# /operate

This is used to perform the calculator operations and return the results in JSON format following the request. 

Input:
```
CURL -X GET https://calcapp.herokuapp.com/operate?operations9*981
```
Output:
```
{
  "operation": "90*891",
  "result": 80190,
  "updated_date": "Mon, 12 Oct 2020 16:51:20 GMT"
}
```
API usage is explained below:

Addition: (must use '%2b' instead of a '+' sign when forming the request)
```
CURL -X GET https://calcapp.herokuapp.com/operate?operations4%2b4
```
Multiplication, division and subtraction:
```
CURL -X GET https://calcapp.herokuapp.com/operate?operations4*4

CURL -X GET https://calcapp.herokuapp.com/operate?operations4/4

CURL -X GET https://calcapp.herokuapp.com/operate?operations4-4
```
# /results

You can either navigate to the following URL or request programatically using curl. This endpoint is designed to output in JSON and only show the last 10 calculations, the results with a date/time stamp recent to oldest.
```
CURL -X GET https://calcapp.herokuapp.com/results
````
Using a browser, navigate to: ~~https://calcapp.herokuapp.com/results~~

*Note:* Refreshing the results endpoint requires a browser refresh at this time.
