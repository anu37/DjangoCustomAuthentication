 
# Custom Authentication in Django

  

A sample app with an API to shorten the URL you pass through the POST call. This project mainly shows how custom authentication in django works and how we can overide the default authentication in django. 

The project structure is as follows.

###  Prerequisites

 - Python 3.7
 - Git
 - pipenv


Steps to get the app running in local dev environment. 

 1. Clone the repo using git - **`git clone https://github.com/anu37/DjangoCustomAuthentication.git`**
 2. Execute **`cd ./sample_rest_api`**
 3. Execute **`pipenv shell`**
 4. Execute **`pipenv install`**
 5. Migrate the models into SqlLite DB by using **`python manage.py runserver --settings=sample_rest_api.settings.local`**
 6. Run the server using **`python manage.py runserver --settings=sample_rest_api.settings.local`**

To access the admin panel and the swagger UI you can create a super user using the command 

    python manage.py createsuperuser

There is one manual step to complete the set up 

 - After creating the super user, login to the admin panel and create a record in the Appication model. Note down the **`client id`** and **`client secret.`** 
 

There are 3 APIs exposed in this project

 1. **POST** http://localhost:8000/secure/auth/ - Which gives us the access token required to consume the rest of the API s that ypu create in a project. 
 The request payload is of type `application/json`
>      
>        {
>           "client_id": "string",
>           "client_secret": "string"
>         }

The response from this API is 

>     {
>         "access_token": "wxbFBoOMYQ9sQsLrqoen4Oo8he7NdrbNzFNQAQwV",
>         "refresh_token": "eXRvBp8LKwFG3nbEP3ag0JJPa7nggG4LbSATB0f0",
>         "expiry_date": "2020-05-24T15:34:26.504266Z",
>         "refresh_token_expiry": "2020-05-31T13:34:26.504254Z",
>         "expired": false,
>         "created_on": "2020-05-24T13:34:26.504658Z",
>         "application_id": 1
>     }

2. **POST** http://localhost:8000/secure/refreshtoken/ - To create a new access token if needed or if the tokens are compromised.
The request payload is of type `application/json`
>      
>        {
>           "refresh_token": "string"
>         }

The response from this API is 

>     {
>         "access_token": "Xu52iz2OMF2ozKNGHTGu33j2n1BLdtpzEtqvSQpq",
>         "refresh_token": "OsEPdmBOcROk0ADt3xpJgQTCCB2aNxPCZu2QOLkN",
>         "expiry_date": "2020-05-24T19:58:22.694822Z",
>         "refresh_token_expiry": "2020-05-31T17:58:22.694955Z",
>         "expired": true,
>         "created_on": "2020-05-24T13:34:26.504658Z",
>         "application_id": 1
>     }

 2.  **POST** http://localhost:8000/api/urlshort/ - This is the API which is authnticated using the custom authentication, where we pass the access token that you have got from the previous API in the header in the form of bearer token. 
 

> **header**: `Bearer wxbFBoOMYQ9sQsLrqoen4Oo8he7NdrbNzFNQAQwV`

The request payload is of type `application/json`

>      
>        {
>           "url": "https://www.google.com/"
>         }
The response from this API is 
> 
>     {
>         "result_url": "https://goolnk.com/qbG275"
>     }

The above API is a secure API which is authenticated using the custom authentication. 
The app `customauth`  defines the whole flow of the custom authentication. 

 1. We define the models which stored the application name, client id and client secret.
 2. Also the model for storing the sccess token, refresh token and the expiry of the tokens.
 3. The views define the logic of handling the tokens in the application.
 4. Exceptions.py is how we override the default exceptions in django.
 5. Generators.py shows how we genearte tokens and the secrets.
 6. Auth.py is the heart of the authetication flow, where we define how the token is taken from the API exposed and how we will be checking it in the DB.
 7. We finaly define the authentication class in the `DEFAULT_AUTHENTICATION_CLASSES` in the `REST_FRAMEWORK` dictionary in settings file.
 

### Links

*  **Admin Dashboard** - http://localhost:8000/admin/

*  **Swagger UI** - http://localhost:8000/swagger/

## Things to do

 - [ ] static file handling
 - [ ] nginx
 - [ ] Dockerfile
 - [ ] Kubernetes
 - [ ] Linting 
 - [ ] Testing
 - [ ] gitlab cli
