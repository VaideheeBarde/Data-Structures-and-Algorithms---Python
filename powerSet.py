#Input is a set
#Output is a power set
#Power set of {0, 1, 2} is {phi, {0}, {1}, {2}, {0, 1}, {1, 2}, {0, 2}, {0, 1, 2}}

def generate_power_set(input_set):
    def directed_power_set(to_be_selected, selected_so_far):
        #Generate all subsets whose intersection with input_set[0], ....
        #input_set[to_be_selected - 1] is exactly selected_so_far
        if to_be_selected == len(input_set):
            power_set.append(selected_so_far)
            return

        directed_power_set(to_be_selected + 1, selected_so_far)
        directed_power_set(to_be_selected + 1, selected_so_far + [input_set[to_be_selected]])

    power_set = []
    directed_power_set(0, [])
    return power_set

print(generate_power_set([0, 1, 2]))