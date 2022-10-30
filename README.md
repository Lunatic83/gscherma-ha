# Aidence Gaspare Scherma home assignment

A task application created using Django, Vue.js and GraphQL.

## Features

- Retrieve a list of tasks
- Creat a task
- Edit a task
- Mark a task as completed
- SignUp
- SignIn

## Installation

This is a pure dockerized application


Run Build Application and tests
```bash
cd gscherma-ha
docker-compose up --build
```

After docker-compose build is complete and app is running

http://localhost:8080


Run Tests separatly
```bash
cd gscherma-ha
docker-compose up --build test 
```


# User Guide

To use this application you need to sign up for a new user and then sign in to use all the tasks features.

The task manager will allow you to:
-   See your task list in the home page
-   Mark the task as completed from the home page
-   See the task detail by clicking on a specific task
-   Edit a task 
