[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=9556968&assignment_repo_type=AssignmentRepo)
# Final Project

![Badge](https://github.com/software-students-fall2022/final-project-team3-final/actions/workflows/web-app.yml/badge.svg)

## Welcome to our Final Project!

In a nutshell, we're matching a list of ingredients to the best recipe! We're using this [dataset](https://www.kaggle.com/datasets/pes12017000148/food-ingredients-and-recipe-dataset-with-images?select=Food+Ingredients+and+Recipe+Dataset+with+Image+Name+Mapping.csv).

Figma designs link [here](https://www.figma.com/file/9vgLSVy1IFhfK5x9lc7Z5r/SWE-Project-5?node-id=0%3A1&t=uthrQBeSZ5pnSrXY-1)

DockerHub Container Image [here](https://hub.docker.com/r/andreistoica/swe-final-team3/tags)

## Features for Web App
- Begin by entering in a comma-separated list of ingredients in your kitchen on the main page.
- Based on our matching algorithm, we will check your ingredients against a database of over 13,000 recipes.
- We will return the names and ingredients of all the recipes that require a combination of several of the ingredients you listed earlier. 
- Simply find one you are interested in, and begin cooking!

## Instructions for how to configure and run all parts of your project for any developer on any platform

- Install Docker
- Run the command "docker compose up --build" while you are located in the main directory
- The website will be hosted at localhost:2001 
- There are no specific requirements for a .env file, but you can make one if you would like

## Instructions for how to import any starter data into the database, if necessary for the system to operate correctly at first.
- Unneeded, all data is hosted as a separate subsystem.

## Instructions for Running Pytest
1. Go into the web-app directory
`cd web-app`
2. Install requirements
`pip3 install -r requirements.txt`
3. Go into the tests directory within the web-app directory
`cd tests`
4. Run the tests with Pytest
`pytest test_webApp.py`

## Team Members:
- [Anvi Agarwal](https://github.com/agarwalanvi01)
- [Ishana Goyal](https://github.com/ishana-goyal)
- [Shannon Huang](https://github.com/shannonh800)
- [Ankit Jain](https://github.com/ankit181818)
- [Andrei Stoica](https://github.com/andreicstoica)
- [Grace Zhang](https://github.com/gracezhang89)

