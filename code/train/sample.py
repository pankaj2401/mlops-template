import sys
import json 
# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)
 
# Arguments passed
print("\nName of Python script:", sys.argv[0])
 
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")
    
myjson = {
  "model_file_name": "model.pkl",
  "tags":{
     "run_id":str(sys.argv[1])
  }
}


with open('registermodel.json', 'w') as fp:
    json.dump(dict, fp, sort_keys=True, indent=4)
