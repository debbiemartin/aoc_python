from sympy.ntheory.residue_ntheory import discrete_log

def get_key(loop_sz, sub_num=7):
    val = 1
    for _ in range(loop_sz):
        val *= sub_num
        val = val % 20201227
    
    return val

def get_loop_sz(pub_key):
    return discrete_log(20201227, pub_key, 7)

def main():
    door_pub_key = 3418282
    card_pub_key = 8719412
    card_loop = get_loop_sz(card_pub_key)
    door_loop = get_loop_sz(door_pub_key)
    
    print(card_loop)
    print(door_loop)
    
    print("PART 1:")
    
    print(get_key(card_loop, sub_num=door_pub_key))
    print(get_key(door_loop, sub_num=card_pub_key))