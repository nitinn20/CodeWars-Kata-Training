def cube_checker(volume, side):
    if side>0:
        return volume==side**3
    else:
        return False