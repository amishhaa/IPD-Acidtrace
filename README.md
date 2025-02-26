To clone this repository/codebase and run it locally you ahve to follow the following steps:
run the following commands in cmd(you can use command prompt or alternativly the black box which appears at bottom of vscode)
1) git clone https://github.com/amishhaa/IPD-Acidtrace.git


Before coding always run:
git pull
and download all dependencies which is required by the project(currently only flask)

The entire codebase is stored in folder src
-> the blockchain model is intialised as a module and the required functions can be accessed by using it as a class/
importing it as a header
from blockchain import blockchain
-> this above line can be used in any folder/wherever you want to use the blockchain class

Frontend
-> The flask code should go in app.py file and to run the flask code you can use the following commands assuming you are in the main directory
cd src
cd frontend
python app.py /windows or python3 app.py /unix
-> your html and css codes should go in templates and styles respectively
-> storage and retrival of user data and passwords should use the database folder 

Model Training and Documentation 
-> .ipynb files and notebooks will be created for training the model and research in model folder under src
-> documentation has a seperate folder where you can store ppts and research papers
-> models can be later saved as .pickle files and used elsewhere.

Requirements and dependencies
-> there is a requirements.txt whixh currently is unmaintained.
-> currently no work on model training has started so the only dependency is flask which can be installed by
pip install flask 


NOTE
-> if you use any virtual enviornments make sure to not push your .env/ .venv in the codebase 
-> we will maintaing a .gitignore shortly but till then this should be taken care of 


HOW TO PUSH YOUR CHANGES
-> you have to follow the following commands to push your changes to the codebase
git add .
git commit -m"write a meaningfull commit message here, yes its mandatory"
git push 

