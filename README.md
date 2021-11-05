# Assignment 2  - distributed in Github Repo e4040-2021Fall-assign2
The assignment is distributed as several jupyter notebooks and a number of directories and subdirectories in utils.

# Detailed instructions how to submit this assignment/homework:
1. The assignment will be distributed as a github classroom assignment - as a special repository accessed through a link
2. A students copy of the assignment gets created automaticaly with a special name - students have to rename the repo per instructions below
3. The solution(s) to the assignment have to be submitted inside that repository as a set of "solved" Jupyter Notebooks, and several modified python files which reside in directories/subdirectories
4. Three files/screenshots need to be uploaded into the directory "figures" which prove that the assignment has been done in the cloud


## (Re)naming of the student repository (TODO students) 
INSTRUCTIONS for naming the student's solution repository for assignments with one student:
* This step will require changing the repository name
* Students MUST use the following name for the repository with their solutions: e4040-2021Fall-assign??-UNI (the first part "e4040-2021Fall-assign??" will probably be inherited from the assignment, so only UNI needs to be added) 
* Initially, the system will give the repo a name which ends with a  student's Github userid. The student MUST change that name and replace it with the name requested in the point above
* Good Example: e4040-2021Fall-assign??-zz9999;   Bad example: e4040-2021Fall-assign??-e4040-2021Fall-assign??-zz9999.
* This change can be done from the "Settings" tab which is located on the repo page.

INSTRUCTIONS for naming the students' solution repository for assignments with more students, such as the final project. Students need to use a 4-letter groupID): 
* Template: e4040-2021Fall-Project-GroupID-UNI1-UNI2-UNI3. -> Example: e4040-2021Fall-Project-MEME-zz9999-aa9999-aa0000.


# Organization of this directory

TODO students: Run commands to create a directory tree, as described in previous assignments

```
.
├── Assignment2-intro.ipynb
├── README.md
├── figures
│   ├── TensorboardScreenshot.png
│   ├── krh2154_gcp_work_example_screenshot_1.png
│   ├── krh2154_gcp_work_example_screenshot_2.png
│   └── krh2154_gcp_work_example_screenshot_3.png
├── model
│   ├── KaggleModel
│   │   ├── saved_model.pb
│   │   └── variables
│   │       └── variables.index
│   ├── task3_model
│   │   ├── saved_model.pb
│   │   └── variables
│   │       └── variables.index
├── predicted.csv
├── task1-optimization.ipynb
├── task2-regularization.ipynb
├── task3_cnn.ipynb
├── task4-augmentation.ipynb
├── task5-kaggle.ipynb
└── utils
    ├── cifar_utils.py
    ├── image_generator.py
    ├── layer_funcs.py
    ├── neuralnets
    │   ├── cnn
    │   │   ├── LeNet_trainer.py
    │   │   ├── model_LeNet.py
    │   │   ├── my_LeNet_trainer.py
    │   │   └── my_model_LeNet.py
    │   ├── kaggle.py
    │   └── mlp.py
    ├── notebook_images
    │   ├── Task3_2_2_metrics.png
    │   ├── task3_1.jpg
    │   ├── task3_2_1.png
    │   ├── task3_2_2.png
    │   └── task3_2_answer.png
    ├── optimizers.py
    └── reg_funcs.py

103 directories, 18666 files
```