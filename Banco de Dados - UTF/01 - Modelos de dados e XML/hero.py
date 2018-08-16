class Hero:
    keys = []
    keys.append('name')
    keys.append('popularity')
    keys.append('alignment')
    keys.append('gender')
    keys.append('height_m')
    keys.append('weight_kg')
    keys.append('hometown')
    keys.append('intelligence')
    keys.append('strength')
    keys.append('speed')
    keys.append('durability')
    keys.append('energy_Projection')
    keys.append('fighting_Skills')

    def __init__(self, id, dictionary):
        self.attributes = {}
        self.attributes['id'] = id
        for key in dictionary:
            self.attributes[key] = dictionary[key]
