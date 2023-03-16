import mushroom
import file_reader
import bayes

# Here we create a list of chars of mushroom characteristics from our known mushroom data
sample_data_list = file_reader.file_read("MushroomTrainingData_6400.txt")

# Here we create a list of chars of mushroom characteristics from our unknown mushroom data,
# add in a '?" to represent our unknown class data
unknown_data_list = file_reader.file_read("MushroomTrainingData_1600.txt")

initial_edibility =[]
for value in unknown_data_list:
    initial_edibility.append(value[0])


for index in range(len(unknown_data_list)): # Adding ? to our class component of unknown mushrooms
    unknown_data_list[index][0] = '?'


bayes.unknown_mushroom_list_probability(sample_data_list, unknown_data_list)

correct_prediction = 0
for index, data in enumerate(unknown_data_list):
    if data[0] == initial_edibility[index]:
        correct_prediction += 1


accuracy_percentage = correct_prediction/len(unknown_data_list)
print("Naive Byes has an accuracy of: " + str(accuracy_percentage))

for data in unknown_data_list:
    print(str(data))