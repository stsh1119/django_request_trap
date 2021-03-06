# Django_request_trap

## Request Trap: A tool for capture and display HTTP requests

### Purpose:

This simple tool is useful during the development of apps that integrate with external services, such as http clients, webhooks, etc. The Requests Trap app provides these services with an endpoint to which they can send requests and notifications

For example, let's assume we are developing an ecommerce site named “myshop" with PayPal integration. During development, Myshop can use Req App to see PayPal requests details via a specific endpoint.

User can setup in the PayPal service the following callback URL: ``` http://request-trap.com/myshop ```

Then the user could see the IPN(Instant Payment Notification) notifications sent by PayPal here: ``` http://request-trap.com/myshop/requests ```

### How it works:

The app has three routes:

1. / (home page with some instructions)

2. /:request_id (this endpoint is used to capture requests)

3. /:request_id/requests (captured requests will be displayed here)

Any request [POST, PUT, GET, DELETE, ...] made to /:request_id will be saved in the db and displayed under /:request/requests.

In /:request_id/requests we should see the request_id in the header, and a list of the received requests, ordered by creation date DESC.

Each request item should display all the information contained in the request, well formatted:

* request date
* remote ip
* request-method
* scheme
* query-string
* query-params
* cookies
* headers

### Install & run locally:
```shell
$ git clone https://github.com/stsh1119/django_request_trap.git
$ cd django_request_trap
$ pipenv install

$ docker run --rm --name mongo_container -d -p 27017:27017 mongo:latest
$ python manage.py runserver
```