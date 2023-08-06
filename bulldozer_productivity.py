
""" Calculation of Wheel/Track Bulldozer's Productivity for a particular activity"""
import numpy as np

manufacturer = input("Insert the manufacturer name of the bulldozer:\n\n")
model_name = input("Insert the model name of the bulldozer:\n\n")
blade_type = input("Insert blade type name of the bulldozer:\n\n")
activity = input("Insert the title of the activity:\n\n")
haul_distance = float(input("please insert haul distance in km:\n"))
haul_speed = float(input("please insert speed of dozer according to the max speed on a particular gear"
                             "during hauling in Km/hr:\n"))
return_distance = float(input("please insert return distance in km:\n"))
return_speed = float(input("please insert speed of dozer according to the max speed on a particular gear"
                                "during returning in Km/hr:\n"))
blade_capacity = float(input("please insert blade's capacity in m3 :\n"))


def machine_name(manufacturer, model_name, blade_type):
    """ Define the fullname of machine as:
    Mnufacturer's name + Tractor's model name + type of blade of bulldozer (S( Straight blade), U( Universal blade), SU(Semi U),...)"""
    manufacturer_case = manufacturer.upper()
    model_case = model_name.upper()
    blade_type_case = blade_type.upper()
    return f'{manufacturer_case} {model_case} {blade_type_case}'

def haul_time(haul_distance):
    hauldistance = []
    hauldistance.append(haul_distance)
    haulldis = np.array(hauldistance)
    haultime = haulldis / haul_speed
    haultime_min = haultime * 60
    return haultime_min


def reverse_time(return_distance):
    returndistance = []
    returndistance.append(return_distance)
    reverssedis = np.array(returndistance)
    reversetime = reverssedis / return_speed
    reversetime_min = reversetime * 60
    return (reversetime_min)


def time_productivity(maneuvering_time=0.05, fix_time=0.05, spread_time=0, cut_time=0):
    time_productivitys = haul_time(haul_distance) + reverse_time(return_distance) + maneuvering_time + fix_time + spread_time + cut_time
    return (np.round(time_productivitys, 3))


def productivity_max(efi=50):
    productivity_x = (blade_capacity * efi) / time_productivity()
    productivitymax = np.round(productivity_x, 2)
    return np.array(productivitymax)


def operator_factor():
    operator = ['a', 'b', 'c']
    level = [1, 0.75, 0.6]
    operator_leval_dict = dict(zip(operator, level))
    operator_level = input(
        "what is the level of operator?\n(a)'Excellent'\n(b) 'Average'\n(c) 'Poor'\n\n")
    for operator, level in operator_leval_dict.items():
        if operator == operator_level:
            return (level)


def material_factor():
    dozing_material = ['a', 'b', 'c', 'd', 'e']
    factors = [1.2, 0.8, 0.7, 0.8, 0.6]
    fill_factor = dict(zip(dozing_material, factors))
    dozing_material_type = input(
        "what is the type of dozing material?\n(a)'Loose stockpile'\n(b) 'Hard to cut; frozen with tilt cylinder'\n(c) 'Hard to cut; frozenwithout tilt cylinder'\n(d) 'Hard to drift; “dead” (dry, non cohesive material) or very sticky'\n(e) 'Rock, ripped or blasted'\n\n")
    for dozing_material, factors in fill_factor.items():
        if dozing_material == dozing_material_type:
            return (factors)


def dozing_factor():
    dozing = ['a', 'b']
    dozing_factors = [1.2, 1.25]
    dozing_dict = dict(zip(dozing, dozing_factors))
    dozing_type = input("what is the type of dozing?\n(a) 'SLOT DOZING'\n(b) 'SIDE BY SIDE DOZING'\n\n")
    for dozing, dozing_factors in dozing_dict.items():
        if dozing == dozing_type:
            return (dozing_factors)


def visibility_factor():
    visibility = ['a', 'b']
    visibility_factorss = [0.8, 1]
    visibility_factors = dict(zip(visibility, visibility_factorss))
    visibility_sit = input(
        "what is the clearance of visibility?\n(a) 'Dust, rain, snow, fog or darkness'\n(b) 'Excellent'\n\n")
    for visibility, visibility_factorss in visibility_factors.items():
        if visibility == visibility_sit:
            return (visibility_factorss)


def grade_factor():
    grade = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    grade_factorss = [1.6, 1.4, 1.2, 1, 0.8, 0.55, 0.3]
    grade_factors = dict(zip(grade, grade_factorss))
    grade_sit = input(
        "what is the grade of dozing site?\n(a) -30\n(b) -20\n(c) -10\n(d) 0\n(e) 10\n(f) 20\n(g) 30\n\n")
    for grade, grade_factorss in grade_factors.items():
        if grade == grade_sit:
            return (grade_factorss)


def real_productivity():
    """ Productivity is in m3/hr"""
    reals_productivitys = productivity_max() * grade_factor() * visibility_factor() * dozing_factor() * \
                               material_factor() * operator_factor()
    print(f'"Real productivity of {machine_name(manufacturer, model_name, blade_type)}" during doing "{activity}" is "{np.round(reals_productivitys[0],2)}"')
    return(np.round(reals_productivitys,2))



def main():

    return real_productivity()

if __name__ == "__main__":
    main()





