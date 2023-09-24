Introduction
REST APIs are an industry-standard way for web services to send and receive data. They use HTTP request methods to facilitate the request-response cycle and typically transfer data using JSON, and more rarely - HTML, XML and other formats.

In this guide, we will create a REST API in Python with Django, using the Django REST Framework to create a shopping cart application.


Note: The complete code for this application can be found on GitHub.

What is a REST API?
REST (Representational State Transfer) is a standard architecture for building and communicating with web services. It typically mandates resources on the web are represented in a text format (like JSON, HTML, or XML) and can be accessed or modified by a predetermined set of operations. Given that we typically build REST APIs to leverage with HTTP instead of other protocols, these operations correspond to HTTP methods like GET, POST, or PUT.

An API (Application Programming Interface), as the name suggests, is an interface that defines the interaction between different software components. Web APIs define what requests can be made to a component (for example, an endpoint to get a list of shopping cart items), how to make them (for example, a GET request), and their expected responses.

In this guide, we'll combine these two concepts to build a REST(ful) API, an API that conforms to the constraints of the REST architectural style, using the Django REST Framework.

What is the Django REST Framework?
The Django REST Framework (DRF) is a package built on top of Django to create web APIs. One of the most remarkable features of Django is its Object Relational Mapper (ORM) which facilitates interaction with the database in a Pythonic way.

However, we can not send Python objects over a network, and hence need a mechanism to translate Django models in other formats like JSON, XML, and vice-versa. This sometimes challenging process, also called serialization, is made super easy with the Django REST Framework.


Note: It's worth noting the difference between creating a REST API with Django itself, and with Django REST.

You can create classic web applications via Django and expose their functionality to the world through REST APIs. In fact, this is pretty easy to do! Though, the Django REST Framework is more specialized for this task, is built on top of plain Django and makes the process easier.

If you'd like to read on how to create REST APIs with the core Django framework - read out Guide to Creating REST APIs in Python with Django.

Setting up Django and Our Application
Django is meant for Rapid Application Development (RAD) projects. Let's rapidly set up a Django project:

Let's start off by initializing a virtual environment, for the sake of organizing dependencies and their effects on other dependencies, and activating it:

$ mkdir drf_tutorial
$ cd drf_tutorial
$ python3 -m venv env
$ env\scripts\activate # Windows 
$ . env/bin/activate # MAC or Linux 
For more on virtualenv, read our Python Virtual Environment Explained!

Or, if you'd like to read about virtualenv alternatives, read our Guide to Managing Python Environments with direnv and pyenv!

Then, we can install Django and the Django REST Framework, within that environment:

$ pip install django
$ pip install djangorestframework

Finally, we can create a project and app, called api_app:

$ django-admin startproject shopping_cart
$ cd shopping_cart # Project contains app
$ python3 manage.py startapp api_app
Once the app is created, it has to be registered in the settings.py file. Let's introduce it alongside some of the built-in applications such as admin and auth which fascilitate administration functionality and simple authentication support.

Open the file under shopping_cart\settings.py and add the api_app directory that we have created into the INSTALLED_APPS list. Also, let's add the rest_framework in the list to let Django know we will be using Django REST Framework (DRF from now onwards):

...
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api_app',
]
Once registered, we can apply the migration (initialize the database) and create a superuser to keep an eye on the database:

$ python3 manage.py migrate  # Initialize database
$ python3 manage.py createsuperuser # Prompts for username and password
With a superuser in place and app registered, we can start the server to accept requests! This is easily done via the runserver command, from within manage.py:

$ python3 manage.py runserver
The process of generating, setting up and configuring a Django Web Application as well as the basic components of Django web applications (defining models, registering models, the Django admin interface, etc) are covered in more detail in our Core Django REST API Guide.

Creating a REST API in Django Using DRF
The Django app is all set, and we can start developing the domain model, persistence and business logic.

Domain Model
Let's create a simple model, CartItem, to denote an online shopping cart item, or rather, a product. In the api_app/models.py file, we'll define our model:

from django.db import models

class CartItem(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.FloatField()
    product_quantity = models.PositiveIntegerField()
Once defined, we'll register our model with Django, so that we can access it from the admin panel. Go to api_app/admin.py and add the following lines:

from django.contrib import admin
from .models import CartItem

admin.site.register(CartItem)
Once a new model has been defined, we'll need to makemigrations for our model to be reflected in the database. From your command prompt, execute the following:

$ python3 manage.py makemigrations
$ python3 manage.py migrate
The model is ready to be used! Web apps frequently transfer model data from one end to another. Naturally, it's time to implement the most useful feature of DRF, serializers!

Serializers define the representation of our model in JSON format and convert object instances to a more transferable format. This will simplify the parsing of data for our API. Deserializers do the opposite - they convert JSON data into our models as object instances.

We will use a serializer to convert our model object to JSON before we send the response. And when we receive a JSON request, our serializer will convert it to the model object, CartItem in this case.

Let's create a serializers.py file in the api_app folder and write a ModelSerializer for our model:

from rest_framework import serializers
from .models import CartItem

class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(max_length=200)
    product_price = serializers.FloatField()
    product_quantity = serializers.IntegerField(required=False, default=1)

    class Meta:
        model = CartItem
        fields = ('__all__')
In the models.py file, we have set the product_quantity attribute of our model as a required field. This will make sure it is always present while saving an object.

However, when the user has not specified the product_quantity - a sensible default assumption is that they want to purchase a single item. The API should not throw an error in this case and set product_quantity to 1 by default.

The serializer will handle this scenario gracefully, without you having to write any such logic in views.py. You can simply add validation and other constraints that are needed to the attribute of the serializer class.

By default, required for every field is set to True. Hence, the serializer will not proceed unless it gets them.

The APIView Class
Like with pure Django, DRF allows both class-based views and function-based views for the API.

In this guide, we'll favor class-based views.

We will be using the APIView class to represent views, which is a subclass of Django's View class. This way we get bootstrapped post(), get(), patch() and delete() methods that we can use to effortlessly perform CRUD operations on our CartItem model, without having to tamper with the persistence layer at all!



Note: While it's alluring to delegate all of the underlying logic to a framework, it's worth noting that you'll likely work with this layer manually at a later date, and proper understanding of databases is highly encouraged.

The get(), post(), patch() and delete() methods can be used in tandem with the model methods, such as all(), save() and delete() to facilitate CRUD functionality for an app.

Our CartItemViews class, which represents the view will extend APIView:

class CartItemViews(APIView):
...
Creating Entities - The POST Request Handler
A POST request is used to send data to the server enclosed in the request body. It is meant to be used when you'd like to create new entities. Let's head to our views and create a POST request handler for our CartItem model.

Let's head to api_app/views.py, create a new class with a post() method that will receive a POST request body, validate it and create an object of class CartItem in our DB:

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CartItemSerializer
from .models import CartItem

class CartItemViews(APIView):
    def post(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
Here you can observe that first, we created a serializer object from the request.data using the CartItemSerializer we've created previously. The is_valid() function returns a Boolean value that indicates whether the request body can be used to create a CartItem object. And the save() methd will create a new instance of CartItem.

The Response must be initialized with the data to be returned. This data can be an instance of any type of Python object like bool, str, dict etc.

Other optional parameters include the status that sets the HTTP response code, content-type that indicates how the data will be rendered, template_name that can be used if HTMLRenderer is selected and headers if we explicitly want to send certain headers in the HTTP response.

Let's set up and expose an endpoint to use our post() method. We do this by editing the shopping_cart/urls.py and including our app's exposed endpoints:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api_app.urls')),
]
With the endpoint exposed, we'll want to register the actual CartItemViews class as a view for the user. Note that this doesn't include a view in the sense of a GUI - it's the request handler.

We've included the api_app.urls here, and delegated the logic that connects the view to the urls.py script within api_app. In the api_app folder, create a new file called urls.py, and link the cart-items/ locator with the CartItemViews class:

from django.urls import path
from .views import CartItemViews

urlpatterns = [
    path('cart-items/', CartItemViews.as_view())
]
The first argument of path() is the subpath where our views would be accessible, and the second argument is the class name we created in views.py to process our request.

Running the Server
Let's run the app and use our end-point /api/cart-items/:

$ python3 manage.py runserver
This will start the local server at http://127.0.0.1:8000/.

On another terminal, let's send a POST request to our end-point with some data:

$ curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8000/api/cart-items/ -d "{\"product_name\":\"name\",\"product_price\":\"41\",\"product_quantity\":\"1\"}"
The view processes the incoming request and responds with the product's data back, as well as a status:

{
    "status": "success",
    "data": {
        "id": 21,
        "product_name": "name",
        "product_price": 41.0,
        "product_quantity": 1
    }
}
The serializer accepts the JSON data, deserializes it into a concrete object and then serializes it again, to return a response.

You can visit http://127.0.0.1:8000/admin/api_app/cartitem/ and you will find the item we just added.

You should also visit http://127.0.0.1:8000/api/cart-items/ and you will see another remarkable feature of DRF, a browsable API.


Free eBook: Git Essentials
Check out our hands-on, practical guide to learning Git, with best-practices, industry-accepted standards, and included cheat sheet. Stop Googling Git commands and actually learn it!


Download the eBook  
Note that we didn't make any HTML page associated with the view, but DRF auto-generated one for us:

DRF Web browseable API after creating endpoint 'api/cart-items'

Note: If you get an error message titled "Template Not Found", be sure you included rest_framework in the INSTALLED_APPS array of shopping_cart/settings.py.

It says that the GET method is not allowed because we haven't created a GET handler for our CartItemViews yet. But there is an input field that will allow you to send a POST request to the endpoint nevertheless.

Request Data Validation
What happens if someone enters enters invalid data? For instance, a string for the product_quantity attribute, which obviously doesn't match the expected data type?

Let's try making an invalid request to the endpoint api/cart-items:

$ curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8000/api/cart-items/ -d "{\"product_name\":\"name\",\"product_price\":\"41\",\"product_quantity\":\"One\"}"
This would result in a response:

{
    "status": "error",
    "data": {
        "product_quantity": [
            "A valid integer is required."
        ]
    }
}
The error is presented beautifully by using the serializer.errors - and we're prompted to input a valid value for the product_quantity attribute. The model knows what it's expecting, and we've supplied the wrong type.

This is an amazing feature of the DRF - automatic data validation. Especially for bootstrapping or prototyping, this saves you from the oftentimes annoying process of validation for simple inputs. You can, however, also define custom validation rules, via custom validators.

If you'd like to read more about validators - read our Guide to Django Validators (coming soon!)

Retrieving Entities - The GET Request Handler
Now that we have successfully added an item to the cart, let's define the logic to retrieve that entity, alongside any other entities that might be in a cart.

There are two typical ways of retrieving resources:

We can make a GET request to list all the entities linked to a cart.
We can retrieve a particular entity from our cart by passing its id as a URL parameter.
We can get a particular object from the model and serialize its data using the CartItemSerializer. Similarly, we can also get all the objects of our model and serialize their data.

The latter approach requires an additional argument, many, to be passed as well:

serializer = CartItemSerializer(items, many=True)
Let's GET an object, given its id, and all of the other items in that cart if the id hasn't been provided, by modifying the api_app/views.py file:

...
class CartItemViews(APIView):
    ...

    def get(self, request, id=None):
        if id:
            item = CartItem.objects.get(id=id)
            serializer = CartItemSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = CartItem.objects.all()
        serializer = CartItemSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
If the optional id argument is omitted, the request returns all of the cart items instead of a particular one and in both cases - a Response lets the client know how the request fared and the serialized data is injected.

Let's hit our endpoint api/cart-items/ with a GET request:

$ curl -X GET http://127.0.0.1:8000/api/cart-items/
This will fetch the results as:

{
    "status": "success",
    "data": [
        {
            "id": 1,
            "product_name": "name",
            "product_price": 41.0,
            "product_quantity": 1
        }
    ]
}

As you can see, CartItemSerializer(items, many=True) has returned serialized data in JSON format - a list of objects. Alternatively, we can supply the id argument through the URL - such as api/cart-items/1/. Once we register an endpoint with a variable URL like this - DRF will automatically tie the path variables to the arguments in our request.

Let's now modify the app's urls.py and add the path - cart-items/<int:id>, that points to our class CartItemViews too.

At this point, api_app/urls.py would look like this:

from django.urls import path
from .views import CartItemViews

urlpatterns = [
    path('cart-items', CartItemViews.as_view()),
    path('cart-items/<int:id>', CartItemViews.as_view())
]
Now, when we hit the api/cart-items/1 endpoint, the variable 1 is resolved to the id argument of the get() method:

$ curl -X GET http://127.0.0.1:8000/api/cart-items/1
This would result in the following response:

{
    "status": "success",
    "data": {
        "id": 1,
        "product_name": "name",
        "product_price": 41.0,
        "product_quantity": 1
    }
}
Here you can observe that CartItemSerializer(item) has returned the CartItem instance's data as a single JSON object instead of an array, as only one resource is expected to be returned.

Updating Entities - The PATCH Request Handler
We can now add and retrieve items from the cart and thus directly alter and observe the cart's state. Now, we need an endpoint to update the item already in a cart, such as increasing the quantity, because who doesn't want more stuff?!

In order to update objects, we can use POST requests, targeting a certain id. Then, we can retrieve that object, update it and save it under the same id - persisting the change.

However, you typically won't be using POST requests for this - even though you can. To decouple creation and update logic - we use PATCH requests to, well, patch existing resources and change them.

The APIView class provides us with the patch() function - which handles PATCH requests and updates the data.

Going back again to api_app/views.py to add the PATCH request handler as below:

...
class CartItemViews(APIView):
    ...    
    def patch(self, request, id=None):
        item = CartItem.objects.get(id=id)
        serializer = CartItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})
Pay close attention to this line:

serializer = CartItemSerializer(item, data=request.data, partial=True)
Here we are passing three arguments to our serializer.

The instance of the CartItem model that we want to update.
The data received from the request.
partial=True to indicate that this may not contain all the fields of our model CartItem.
Since we need to pass in an actual instance, we'll have to use the get() function to first retrieve a resource and then update it.


Note: When retrieving a resource for updating, it's best to perform validation logic to make sure the resource exists in the first place.

And as we are making an update, we will validate our serializer and then save it. It's time to send a PATCH request at api/cart-items/1 and update out item:

$ curl -X PATCH http://127.0.0.1:8000/api/cart-items/1 -H 'Content-Type: application/json' -d '{"product_quantity":6}'
This results in:

{
    "status": "success",
    "data": {
        "id": 1,
        "product_name": "name",
        "product_price": 41.0,
        "product_quantity": 6
    }
}

The response showed an updated quantity. You can also visit http://127.0.0.1:8000/admin/api_app/cartitem/1/change/ and you will find that it is successfully updated.

Deleting Entities - The DELETE Request Handler
We typically add, add, add and then remember we want to buy some items in multiples, as gifts - until the billing section arrives. The reality check typically makes us remove a few things from the cart that we don't really need, and reasses our logic.

A user needs to be able to remove certain items from a cart - if they add it by accident, or simply change their mind.

To remove an item from the cart, let's implement the delete() function, passing in the id of the object we'd like to delete. Then, calling delete() on the model itself, we can remove it from persistence.

We won't need to use a serializer for this purpose as there's no conversion between data and concrete objects. Instead of doing CartItem.objects.get() we can use the get_object_or_404() function that will automatically return a 404 response when the object with the given id is not present - since we won't be returning any info on the deleted entity itself.

This way - we know whether an entity exists (didn't return 404) or not, without having to serialize it and send it back as a response.

Let's go back to api_app/views.py and add the delete() method:

...
from django.shortcuts import get_object_or_404

class CartItemViews(APIView):
    ...
    def delete(self, request, id=None):
        item = get_object_or_404(CartItem, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})
Don't miss the new import statement! After we get the object, calling its delete() method removes it from the database.

Let's try to remove the item from our cart:

$ curl -X "DELETE" http://127.0.0.1:8000/api/cart-items/1
If the item is present, the function should return the following response:

{
    "status": "success",
    "data": "Item Deleted"
}
When the item is not present, the response would look like this:

{
    "detail": "Not found."
}
You can visit http://127.0.0.1:8000/admin/api_app/cartitem/ and the item is no longer present there. You can also visit http://127.0.0.1:8000/api/cart-items/ to access the web browseable API you just created with all the CRUD operations!

Conclusion
This tutorial showed how we can build a RESTful API in Django using the Django REST Framework. We created a Django project and added an api_app application to it. We then created a CartItem model and CartItemSerializer to handle the serialization and deserialization of our model.

We added a class-based view CartItemView to perform CRUD operations on our model. We added an item to the cart using post() we fetched all the items and a particular item using get(). We also created patch() to update our items and delete() to remove an item from the cart.

Reference : https://stackabuse.com/creating-a-rest-api-with-django-rest-framework/

