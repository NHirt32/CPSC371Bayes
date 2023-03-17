import sys
import file_reader
import bayes

def user_input():
    file_mode = input("What version of this program would you like to use? \nEnter 100 for an 8000:100 comparision. \nEnter 1600 for a 6400:1600 comparision along with a print of the accuracy\n")
    file_mode = int(file_mode)
    # Here we create a list of chars of mushroom characteristics from our known mushroom data
    if file_mode == 1600:
        sample_data_list = file_reader.file_read("MushroomTrainingData_6400.txt")
        unknown_data_list = file_reader.file_read("MushroomTestData_1600.txt")
        return (sample_data_list, unknown_data_list, file_mode)
    elif file_mode == 100:
        sample_data_list = file_reader.file_read("MushroomData_8000.txt")
        unknown_data_list = file_reader.file_read("MushroomData_Unknwon_100.txt")
        return (sample_data_list, unknown_data_list, file_mode)
    else:
        print("Invalid input")
        sys.exit(1)

file_tuple = user_input()

file_mode = file_tuple[2]

# Our list of known mushroom data
sample_data_list = file_tuple[0]

# Our list of unknown mushroom data
unknown_data_list = file_tuple[1]

if file_mode == 1600:
    initial_edibility =[] # Checking initial edibility data for file mode 1600
    for value in unknown_data_list:
        initial_edibility.append(value.pop(0))

for index in range(len(unknown_data_list)): # Adding ? to our class component of unknown mushrooms
    unknown_data_list[index].insert(0, '?')

results_list = []

bayes.unknown_mushroom_list_probability(sample_data_list, unknown_data_list, results_list)

if file_mode == 1600: # Conditionally checking formula accuracy if given a data set where we already know the answer
    correct_prediction = 0
    for index, data in enumerate(unknown_data_list):
        if data[0] == initial_edibility[index]:
            correct_prediction += 1
    accuracy_percentage = correct_prediction/len(unknown_data_list)
    print("Naive Byes has an accuracy of: " + str(accuracy_percentage))

else:
    # Write Output
    output_file = open("predictionResultNBC.txt", 'w')

    for prediction in results_list:
        output_file.write(prediction + "\n")

    output_file.close()
