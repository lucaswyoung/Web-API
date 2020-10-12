# Web-API

This project repository is a web based calculator API that leverages Python and Flask to perform standard mathemical calculations such as addition, subtraction, multiplication and division.

# API usage

This API is hosted at the following URL: https://sezzlecalcapp.herokuapp.com/results

This API has to endpoints:
- /operate
- /results

# /Operate

This is used to perform the calculator operations, please see the examples below:

Addition: (must use '%2b' instead of a '+' sign when forming the request

CURL -X GET https://sezzlecalcapp.herokuapp.com/operate?operations4%2b4

Multiplication, division and subtraction:

CURL -X GET https://sezzlecalcapp.herokuapp.com/operate?operations4*4

CURL -X GET https://sezzlecalcapp.herokuapp.com/operate?operations4/4

CURL -X GET https://sezzlecalcapp.herokuapp.com/operate?operations4-4

# /Results

You can either navigate to the following URL or request programatically using curl. This endpoint is designed to output in JSON and only show the last 10 calculations, the results with a date/time stamp recent to oldest.

CURL -X GET https://sezzlecalcapp.herokuapp.com/results

Using a browser, navigate to: https://sezzlecalcapp.herokuapp.com/operate?operations4*4



