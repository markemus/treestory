#from tags import tags MUST BE IN ALL MODULES
#tags are global flags that enable or disable blurbs in the narrative tree


class Iter_dict():
    tags = {
    "smoke_reaction"    : 1,
    "gender_formal"     : 1
    }

    outputs = {
    "smoke_reaction"    : ["entices", "repulses"],
    "gender_formal"     : ["sir", "madam"]
    }

    def __init__(self):
        None

    def __getitem__(self, key):
        skey = str(key)

        return self.outputs[key][self.tags[key]]

iter_dict = Iter_dict()
