from convert_dcm_jpeg import dcm_to_jpg, dcm_to_png

# test method

# provide input path where .dcm files are present and output path where .png or .jpg files are to be created

# converting test .dcm files to .jpeg

input_path = r"C:\Users\User\Desktop\OSIC_pulmonary_fibrosis_dataset\osic-pulmonary-fibrosis-progression\test\ID00426637202313170790466"

output_path = r"C:\Users\User\Desktop\OSIC_pulmonary_fibrosis_dataset\osic-pulmonary-fibrosis-progression\test\Folder5"

dcm_to_jpg(input_path, output_path)

dcm_to_png(input_path, output_path)


# converting train .dcm files to .jpeg separated for each patient

filepath1 = r'C:\Users\User\Desktop\OSIC_pulmonary_fibrosis_dataset\osic-pulmonary-fibrosis-progression\train'

filepath2 = r'C:\Users\User\Desktop\OSIC_pulmonary_fibrosis_dataset\osic-pulmonary-fibrosis-progression\train_jpeg'


# Create directories for storing jpegs of 176 patients CT scan dicoms

for x in range(176):
    directory = "Patient" + str(x)
    newpath = os.path.join(filepath, directory)
    os.mkdir(newpath)


# converting the dicoms to jpegs and storing in created directories for patients

for filename1 in os.listdir(filepath1):
    for filename2 in os.listdir(filepath2):
        print(filename1, filename2)
        break
