api end point to create a caregory regular and medium,square ans small
https://127.0.0.1:8000/api/category/  --post request
i am using postman
make sure Content-type is application/json
in the body section raw you can just type
{
    "category":"regular",
    "size":"medium"
}

if you give other than reqular or square it return catergory should be regular or square
if the is not in the database it return please provide valid size

listing all pizzas
https://127.0.0.1:8000/api/pizza/    --get request

it list all the pizzas with all the information in json format

https://127.0.0.1:8000/api/pizza/pizza/filter/any-category/any-size/  --get request

it fetches the pizzas based on the category in json format if the category not found it return category not found 401 response


https://127.0.0.1:8000/api/pizza/{id}/    --delete request

it delete the specified id of the pizza

https://127.0.0.1:8000/api/pizza/{id}/     --put request
it update the information of what ever you want and just sumit it


Example:
https://127.0.0.1:8000/api/pizza/4/    --put request

in body
{
    "id": 4,
    "name": "healthy1",
    "category": 2,
    "toppings": [
        2
    ]
}


it update the health with health1
