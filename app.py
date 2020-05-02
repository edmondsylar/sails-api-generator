import pathlib
# import our generate functions.
from generate import gn_ctr, gn_mdl

# main | parent directory
parent = pathlib.Path(__file__).parent.resolve()


# define controller and model here.
controller = open(parent/'blueprints/controller.txt')
model = open(parent/'blueprints/model.txt')

generate_model = gn_mdl(model)
if generate_model != False:
    generate_controllers = gn_ctr(controller)
    if(generate_controllers != True):
        print(generate_controllers)

    print('sails api created | sails-py-generator.')
else: 
    print(generate_model)
