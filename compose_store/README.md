## Docker Swarm Multi-container Application

Application consisting of three containers, each
consisting of a web application (Flask/Python 3):
- `Customer` returns JSON object with customer details for `customerid` in GET request.
- `Product`  returns JSON object with product details
for `productid` in GET request.
- `Order` receives `customerid` and `productid` via
POST request, obtains customer JSON object from
`Customer` service and product JSON object from `Product` service and returns merged JSON object. `Order` is bound to external port 5000.

### Instructions
1. Build images
```
$ cd compose_store
$ docker-compose build
Building customer
Step 1/7 : FROM python:3.6.1-alpine
3.6.1-alpine: Pulling from library/python
...
...
Step 7/7 : CMD python ./order.py
 ---> Running in d14f4b6ddc05
 ---> 5f6ac2fc3f01
Removing intermediate container d14f4b6ddc05
Successfully built 5f6ac2fc3f01
```

2. Images are in local Repository
```
$ docker images
REPOSITORY              TAG                 IMAGE ID            CREATED             SIZE
composestore_order      latest              5f6ac2fc3f01        16 seconds ago      104 MB
composestore_product    latest              94f6bd727bad        29 seconds ago      101 MB
composestore_customer   latest              ec8985a40b74        39 seconds ago      101 MB
python                  3.6.1-alpine        2aa6f28a08ba        3 days ago          89.4 MB
```

3. Bring up Docker containers
```
$ docker-compose up
Creating network "composestore_default" with the default driver
Creating composestore_product_1
Creating composestore_customer_1
Creating composestore_order_1
Attaching to composestore_customer_1, composestore_product_1, composestore_order_1
customer_1  |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
customer_1  |  * Restarting with stat
product_1   |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
product_1   |  * Restarting with stat
customer_1  |  * Debugger is active!
customer_1  |  * Debugger PIN: 347-992-078
product_1   |  * Debugger is active!
product_1   |  * Debugger PIN: 320-542-063
order_1     |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
order_1     |  * Restarting with stat
order_1     |  * Debugger is active!
order_1     |  * Debugger PIN: 136-681-353
<terminal hangs>
```
This starts the containers in attached mode, the terminal hangs on log follow. Use command line option
`-d` to start containers in the background.

4. Submit POST request to `Order` service via curl
Open new shell.
```
$ curl -d "customerid=1&productid=2" -X POST http://127.0.0.1:5000/place_order
{
  "address": "1234 Good St",
  "customerid": 1,
  "description": "Glass",
  "email": "alice@wonderland.org",
  "name": "Alice",
  "price": 6.0,
  "productid": 2
}
```

5. Shutdown containers
Press <CTRL>+C in first shell (if attached) or
run `docker-compose down` in the folder `compose_store`.

6. Remove all containers and then images
```
$ docker rm $(docker ps -qa)
...
$ docker rmi $(docker images -q)
...
```
