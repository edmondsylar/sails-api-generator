# File that handels generation of the models and controllers.
import pathlib
parent = pathlib.Path(__file__).parent.resolve()

def gn_ctr(_file):
    ctr_test = open(parent/'test/controller.js', "w")
    _object = _file.read()
    try: 
        for line in _object:
            ctr_test.write(line)
        # return ('Controller created check your test\'s file.')
        return True
    except Exception as error:
        return ('Error encountered: \n', error)




def gn_mdl(_file):
    ctr_test = open(parent/'test/model.js', "w")
    _object = _file.read()
    try: 
        for line in _object:
            ctr_test.write(line)
        # return ('Controller created check your test\'s file.')
        return True
    except Exception as error:
        return ('Error encountered: \n', error)
