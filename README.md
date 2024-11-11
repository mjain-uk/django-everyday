# django-everyday
Practice and add every day tasks while learning django and django rest framework


## CRUD using django rest framework
- Have CRUD with bare minimum setup to demonstrate the process of serialization. 
- App name is basiccrud
- Demonstrate testing 


## Celery - First task and message broker - Rabbit MQ
Useful links: 
1. https://docs.celeryq.dev/en/latest/getting-started/first-steps-with-celery.html#first-steps

Pre-requisite
- Install a message broker such RabbitMQ

Create Celery Task
- Demonstrate setup celery instance
- Create a task
- To test the task, open shell and import the task such as 
`from basiccrud.tasks import add`
and then
`add.delay(4,5)`
and you should see `<AsyncResult: some-task-id>`

