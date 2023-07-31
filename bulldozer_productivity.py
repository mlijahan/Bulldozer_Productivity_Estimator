
""" Calculation of Wheel/Track Bulldozer's Rimpull for a particular activity"""
import numpy as np


haul_speed = float(input("please insert haul distance km:\n"))
reverse_speed = float(input("please insert haul distance km:\n"))
blade_capacity = float(input("please insert haul distance km:\n"))

def haul_time():
    hauldis = []
    hauldis.append(float(input("please insert haul distance km:\n")))
    haulldis = np.array(hauldis)
    haultime = haulldis / haul_speed
    haultime_min = haultime * 60
    return (haultime_min)


@property
def reverse_time():
    reversedis = []
    reversedis.append(float(input("please insert reverse distance km:\n")))
    reverssedis = np.array(reversedis)
    reversetime = reverssedis / reverse_speed
    reversetime_min = reversetime * 60
    return (reversetime_min)


@property
def time_productivity(maneuvering_time=0.05, fix_time=0.05, spread_time=0, cut_time=0):
    time_productivitys = haul_time() + reverse_time() + maneuvering_time + fix_time + spread_time + cut_time
    return (np.round(time_productivitys, 3))


@property
def productivity_max(efi=50):
    productivity_x = (blade_capacity * efi) / time_productivity()
    productivitymax = np.round(productivity_x, 2)
    return (productivitymax)


@property
def operator_factor():
    operator = ['a', 'b', 'c']
    level = [1, 0.75, 0.6]
    operator_leval_dict = dict(zip(operator, level))
    operator_level = input(
        "what is the level of operator?\n(a)'Excellent'\n(b) 'Average'\n(c) 'Poor'\n\n")
    for operator, level in operator_leval_dict.items():
        if operator == operator_level:
            return (level)


@property
def material_factor():
    dozing_material = ['a', 'b', 'c', 'd', 'e']
    factors = [1.2, 0.8, 0.7, 0.8, 0.6]
    fill_factor = dict(zip(dozing_material, factors))
    dozing_material_type = input(
        "what is the type of dozing material?\n(a)'Loose stockpile'\n(b) 'Hard to cut; frozen with tilt cylinder'\n(c) 'Hard to cut; frozenwithout tilt cylinder'\n(d) 'Hard to drift; “dead” (dry, non cohesive material) or very sticky'\n(e) 'Rock, ripped or blasted'\n\n")
    for dozing_material, factors in fill_factor.items():
        if dozing_material == dozing_material_type:
            return (factors)


@property
def dozing_factor():
    dozing = ['a', 'b']
    dozing_factors = [1.2, 1.25]
    dozing_dict = dict(zip(dozing, dozing_factors))
    dozing_type = input("what is the type of dozing?\n(a) 'SLOT DOZING'\n(b) 'SIDE BY SIDE DOZING'\n\n")
    for dozing, dozing_factors in dozing_dict.items():
        if dozing == dozing_type:
            return (dozing_factors)


@property
def visibility_factor():
    visibility = ['a', 'b']
    visibility_factorss = [0.8, 1]
    visibility_factors = dict(zip(visibility, visibility_factorss))
    visibility_sit = input(
        "what is the clearance of visibility?\n(a) 'Dust, rain, snow, fog or darkness'\n(b) 'Excellent'\n\n")
    for visibility, visibility_factorss in visibility_factors.items():
        if visibility == visibility_sit:
            return (visibility_factorss)


@property
def grade_factor():
    grade = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    grade_factorss = [1.6, 1.4, 1.2, 1, 0.8, 0.55, 0.3]
    grade_factors = dict(zip(grade, grade_factorss))
    grade_sit = input(
        "what is the grade of dozing site?\n(a) -30\n(b) -20\n(c) -10\n(d) 0\n(e) 10\n(f) 20\n(g) 30\n\n")
    for grade, grade_factorss in grade_factors.items():
        if grade == grade_sit:
            return (grade_factorss)


@property
def real_productivity():
    reals_productivitys = productivity_max() * grade_factor() * visibility_factor() * dozing_factor() * \
                               material_factor() * operator_factor()
    reals_productivity = [item for sublist in reals_productivitys for item in sublist]
    print(np.round(reals_productivity, 2))
    return (np.round(reals_productivity, 2))








