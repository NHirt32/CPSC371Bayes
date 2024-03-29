# CPSC371Bayes

## Contributors
    Name: Andrew Hunter-Owega
    Email: ahunterow@unbc.ca
    Student Number: 230 147 039

    Name: Daniel Strickland
    Email: dstrickla@unbc.ca
    Student Number: 230 146 357

    Name: Nicholas Hirt
    Email: nhirt@unbc.ca
    Student Number: 230 127 295

# Report

## Accuracy of the Application
    For the purpose of measuring prediction accuracy of this program we decided to create custom mushroom data files based off of the provided files (MushroomData_8000.txt and MushroomData_Unknwon_100.txt) to additionally test the accuracy of our model.
    The files in question are "MushroomTrainingData_6400.txt" and "MushroomTestData_1600.txt"; we choose to divide our given data in this way to achieve an 80-20 split.
    When utilizing these files we were able to measure a correct prediction rate of 93%.
    
## Project Structure
        This project is seperated into 3 seperate python files which are described below:
### main.py
        Standard main file for this project. Contains very basic functionality and primarily calls functionality from our other python files.
        Additionally, has an options selector from user whether to use a 8000:100 or 6400:1600 known:unknown mushroom split.
        Note that for model accuracy only 6400:1600 mode is supported as with our 100 unknown mushrooms we do not know their actual edibility values.
### file_reader.py
        This file is responsible for reading data in from our given .txt files and outputting this data as a list.
        This list is stripped of '\n' and split on ','.
### bayes.py
        This file is responsible for our actual formula calculations.
        It will calculate the probability a given mushroom is edible or poisonous and compare these probabilities.
        Based on these comparisions we update our list of mushroom properties.
    
## How To Use
        Open the project in a software that supports python files and run main.py.
        Enter which file mode you'd like to preview (1600 or 100) in the terminal.
        Please note that there is a significant delay for 1600 as it has to compute probabilities for 1600 mushroom attributes.
