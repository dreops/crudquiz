## **CrudQuiz** - An __interactive__ quiz web app.

_In response to the first solo project at QA Consulting._


### **Index**

<span style="text-decoration:underline;">Coming soon!</span>


### **The Brief**

Create a web app deployed on a production-ready server that has full CRUD functionality to meet the MVP (_minimum viable product_) without adding any additional functionality until this MVP has been met. Part of the brief is writing documentation (which you are reading now) as well as the use of a project tracking system (in my case Trello) which also utilises the Kanban method.


## Entity Relationship Diagram





![alt_text](assets/erd.jpg "Entity Relationship Diagram")


To meet the MVP two tables are needed and here a one-to-many relationship is shown between the answer_id row in the Questions table and the user_answers row in the Answers table.


### **Testing**

As per the project brief one can run pytest to run tests on my code.


### **Deployment**

 \
Whist the project is currently in development it has not been deployed on a production server, but will be making use Nginx (possibly my favourite ever web server) and Gunicorn (pronounced ‘Gee Unicorn’).


#### **Technologies Used**



*   Python
*   Flask microframework
*   [Git](https://github.com/dreops/crudquiz) - VCS
*   [Trello](https://trello.com/b/0sRfDybn/crudquiz-kanban) - Project Tracking
*   Google Cloud Platform to host every element of the project from VM’s to SQL
*   Gunicorn (will be used)
*   Static IP and DNS (routing 


### **Credits**

Project by Andreas Andrews

A huge thanks to trainer Ben, Luke, Matt & Piers as well as the incredibly lovely cohort. \
Additional thanks to Rory, Naomi and all the immensely supportive & wonderful staff and trainees I’m grateful to have met whilst training at QA.

<p style="text-align: right">
<em> \
Document version<strong>  0.2.0</strong></em></p>