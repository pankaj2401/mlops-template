import sys
import json 
# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)
 
# Arguments passed
print("\nName of Python script:", sys.argv[0])

# Comment 1
# Print arguments
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")

# Getting existing model parameters
register_model_file = open("code/train/registermodel.json", "r")
model_json_object = json.load(register_model_file)
register_model_file.close()

# Add run id to the tags
model_json_object["model_tags"]["run_id"] = str(sys.argv[1])
register_model_file = open("code/train/registermodel.json", "w")
json.dump(model_json_object, register_model_file)
register_model_file.close()
