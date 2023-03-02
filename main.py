import mushroom
import file_reader

sample_data_list = file_reader.file_read()
mushroom_list = []
for element in sample_data_list:
    mushroom_list.append(mushroom.mushroom(element[0], element[1], element[2], element[3], element[4], element[5], element[6], element[7],
                                  element[8], element[9], element[10], element[11], element[12], element[13], element[14],
                                  element[15], element[16], element[17], element[18], element[19], element[20], element[21]))

for mushroom in mushroom_list:
    print(mushroom.classes)