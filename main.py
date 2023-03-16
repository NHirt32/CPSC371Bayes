import file_reader
import bayes

# Here we create a list of chars of mushroom characteristics from our known mushroom data
sample_data_list = file_reader.file_read("MushroomData_8000.txt")

# Here we create a list of chars of mushroom characteristics from our unknown mushroom data,
# add in a '?" to represent our unknown class data
unknown_data_list = file_reader.file_read("MushroomData_Unknwon_100.txt")
for index in range(len(unknown_data_list)): # Adding ? to our class component of unknown mushrooms
    unknown_data_list[index].insert(0, '?')


bayes.unknown_mushroom_list_probability(sample_data_list, unknown_data_list)

# Console debug printing
for data in unknown_data_list:
    print(str(data))

# Opening file and writing edibility column to it
output = open("predictionResultBayes.txt", "w")
for prediction in unknown_data_list:
    output.write(str(prediction[0]))
    output.write("\n")
output.close()