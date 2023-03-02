def file_read():
    sample_data_file = open("MushroomData_8000.txt", "r")
    sample_data_list = sample_data_file.readlines()

    for index, data in enumerate(sample_data_list):
        data = data.strip("\n")
        sample_data_list[index] = data.split(',')

    return sample_data_list