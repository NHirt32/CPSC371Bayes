import mushroom
import file_reader

sample_data_list = file_reader.file_read()
mushroom_list = mushroom.mushroom_list_create(sample_data_list)

for mushroom in mushroom_list:
    print(mushroom.classes)