import random
import math
from heapq import nlargest
import numpy as np


# import matplotlib.pyplot as plt

# plt.rcParams['font.size'] = 8


def gen_pts():
    res = []

    for j in range(100):
        pt = (random.uniform(0, 10), random.uniform(0, 10))
        res.append(pt)

    return res


def get_neighbours(pt, step):
    x = pt[0]
    y = pt[1]
    res = []

    res.append((x + step, y))
    res.append((x - step, y))
    res.append((x + step, y + step))
    res.append((x + step, y - step))
    res.append((x - step, y + step))
    res.append((x - step, y - step))
    res.append((x, y + step))
    res.append((x, y - step))
    return res


def use_algo(f_type, algo_name, step, beam_size):
    vals = []
    steps = []

    rand_pts = gen_pts()
    for i in range(len(rand_pts)):
        start_pt = rand_pts[i]

        if (f_type is "f1"):
            val_init = f1(start_pt)
            if (algo_name is "hill"):
                best_pt_val_steps = hill_climbing(f_type, start_pt, val_init, step, 0)
            else:
                best_pt_val_steps = beam_search(f_type, start_pt, val_init, step, 0, beam_size)

        else:
            val_init = f2(start_pt)
            if (algo_name is "hill"):
                best_pt_val_steps = hill_climbing(f_type, start_pt, val_init, step, 0)
            else:
                best_pt_val_steps = beam_search(f_type, start_pt, val_init, step, 0, beam_size)
        # print(best_pt_val_steps)
        vals.append(best_pt_val_steps[0])
        steps.append(best_pt_val_steps[1])

    # print(vals)
    # print(steps)

    return vals, steps


def f1(pt):
    val = math.sin(pt[0] / 2.0) + math.cos(2 * pt[1])
    return val


def f2(pt):
    val = -abs(pt[0] - 2) - abs(0.5 * pt[1] + 1) + 3
    return val


def hill_climbing(f_type, curr_pt, best_val, step, num_steps):
    max_found = False
    while (not max_found):
        is_new_step = False
        curr_best_val = best_val  # store current local max

        # try all neighbours
        for next in get_neighbours(curr_pt, step):
            if (f_type is "f1"):
                val_next = f1(next)
            else:
                val_next = f2(next)

            if (val_next > best_val):  # if new value better than previous, update
                curr_pt = next
                best_val = val_next
                # we found a higher value (might take a step towards it after we check all neigbours)
                is_new_step = True

        if (is_new_step):
            num_steps += 1  # add a step for every time Hill_Climbing is used

        # if current local max was not updated, we are at an optimum
        if (curr_best_val is best_val):
            max_found = True

    return best_val, num_steps


def beam_search(f_type, curr_pt, best_val, step, num_steps, beam_size):
    max_found = True

    # create an initial beam of size k based on the 1st point
    initial_neighbours = []
    for next in get_neighbours(curr_pt, step):
        if (f_type is "f1"):
            val_curr = f1(next)
        else:
            val_curr = f2(next)

        # check if the root point was already the max
        if (val_curr > best_val):
            max_found = False

        neigh_pt_val = (next, val_curr)
        initial_neighbours.append(neigh_pt_val)

    beam = nlargest(beam_size, initial_neighbours, key=lambda tup: tup[1])

    if (max_found):
        return curr_pt, best_val, 0

    # loop and update the beam with the best values until you find the max
    while (not max_found):

        curr_best_val = (beam[0])[1]  # store current highest value
        all_neighbour_pt_val = []

        # try all neighbours
        for beam_pt_val in beam:
            for next in get_neighbours(beam_pt_val[0], step):
                if (f_type is "f1"):
                    val_curr = f1(next)
                else:
                    val_curr = f2(next)

                neigh_pt_val = (next, val_curr)
                all_neighbour_pt_val.append(neigh_pt_val)

        # select k best
        best_neighbours = nlargest(beam_size, all_neighbour_pt_val, key=lambda tup: tup[1])

        # check if the highest parent was the max
        # if current local max was not updated, we are at an optimum

        if (curr_best_val >= (best_neighbours[0])[1]):
            max_found = True

        else:
            num_steps += 1
            beam = best_neighbours

    return curr_best_val, num_steps


# use_algo("f1", "beam", 0.01, 16)
hill_f1 = []
hill_f2 = []

beam_f1 = []
beam_f2 = []

# for step_size in [0.01, 0.05, 0.1, 0.2]:
#     hill_f1 = use_algo("f1", "hill", step_size, 0)
#     hill_f2 = use_algo("f2", "hill", step_size, 0)
#
#     # Convert to arrays
#     hill_f1_vals = np.array(hill_f1[0])
#     hill_f1_steps = np.array(hill_f1[1])
#     hill_f2_vals = np.array(hill_f2[0])
#     hill_f2_steps = np.array(hill_f2[1])
#
#     # Calculate mean
#     hill_f1_vals_mean = np.mean(hill_f1_vals)
#     hill_f1_steps_mean = np.mean(hill_f1_steps)
#     hill_f2_vals_mean = np.mean(hill_f2_vals)
#     hill_f2_steps_mean = np.mean(hill_f2_steps)
#
#     # Calculate standard deviation
#     hill_f1_vals_std = np.std(hill_f1_vals)
#     hill_f1_steps_std = np.std(hill_f1_steps)
#     hill_f2_vals_std = np.std(hill_f2_vals)
#     hill_f2_steps_std = np.std(hill_f2_steps)
#
#     testFile = open('hill_results.txt', 'a')
#
#     testFile.write("Hill Climbing: Max Values and Steps, f1 , Step Size {0}\n".format(str(step_size)))
#     testFile.write("Max Vals Mean = {0}\n".format(str(hill_f1_vals_mean)))
#     testFile.write("Max Vals Std = {0}\n".format(str(hill_f1_vals_std)))
#     testFile.write("Num of Steps Mean = {0}\n".format(str(hill_f1_steps_mean)))
#     testFile.write("Num of Steps Std = {0}\n\n".format(str(hill_f1_steps_std)))
#     for i in range(0, 100):
#         testFile.write(str(hill_f1[0][i]))
#         testFile.write('      ')
#         testFile.write(str(hill_f1[1][i]))
#         testFile.write('\n')
#
#     testFile.write("  \n\n")
#
#     testFile.write("Hill Climbing: Max Values and Steps, f2 , Step Size {0}\n".format(str(step_size)))
#     testFile.write("Max Vals Mean = {0}\n".format(str(hill_f2_vals_mean)))
#     testFile.write("Max Vals Std = {0}\n".format(str(hill_f2_vals_std)))
#     testFile.write("Num of Steps Mean = {0}\n".format(str(hill_f2_steps_mean)))
#     testFile.write("Num of Steps Std = {0}\n\n".format(str(hill_f2_steps_std)))
#     for i in range(0, 100):
#         testFile.write(str(hill_f2[0][i]))
#         testFile.write('      ')
#         testFile.write(str(hill_f2[1][i]))
#         testFile.write('\n')
#
#     testFile.write("-------------------------------------\n\n")
#
#     testFile.close()

for step_size in [0.01, 0.05, 0.1, 0.2]:
    for beam_size in [2, 4, 8, 16]:
        beam_f1 = use_algo("f1", "beam", step_size, beam_size)
        beam_f2 = use_algo("f2", "beam", step_size, beam_size)

        beam_f1_vals = np.array(beam_f1[0])
        beam_f1_steps = np.array(beam_f1[1])
        beam_f2_vals = np.array(beam_f2[0])
        beam_f2_steps = np.array(beam_f2[1])

        beam_f1_vals_mean = np.mean(beam_f1_vals)
        beam_f1_steps_mean = np.mean(beam_f1_steps)
        beam_f2_vals_mean = np.mean(beam_f2_vals)
        beam_f2_steps_mean = np.mean(beam_f2_steps)

        beam_f1_vals_std = np.std(beam_f1_vals)
        beam_f1_steps_std = np.std(beam_f1_steps)
        beam_f2_vals_std = np.std(beam_f2_vals)
        beam_f2_steps_std = np.std(beam_f2_steps)

        testFile = open('beam_results.txt', 'a')

        testFile.write("Local Beam Search:  Max Values and Steps, f1 , Step Size {0}, Beam Size {1}\n".format(str(step_size), str(beam_size)))
        testFile.write("Max Vals Mean = {0}\n".format(str(beam_f1_vals_mean)))
        testFile.write("Max Vals Std = {0}\n".format(str(beam_f1_vals_std)))
        testFile.write("Num of Steps Mean = {0}\n".format(str(beam_f1_steps_mean)))
        testFile.write("Num of Steps Std = {0}\n\n".format(str(beam_f1_steps_std)))
        for i in range(0, 100):
            testFile.write(str(beam_f1[0][i]))
            testFile.write('      ')
            testFile.write(str(beam_f1[1][i]))
            testFile.write('\n')

        testFile.write("  \n\n")

        testFile.write("Local Beam Search: Max Values and Steps, f2 , Step Size {0}, Beam Size {1}\n".format(str(step_size), str(beam_size)))
        testFile.write("Max Vals Mean = {0}\n".format(str(beam_f2_vals_mean)))
        testFile.write("Max Vals Std = {0}\n".format(str(beam_f2_vals_std)))
        testFile.write("Num of Steps Mean = {0}\n".format(str(beam_f2_steps_mean)))
        testFile.write("Num of Steps Std = {0}\n\n".format(str(beam_f2_steps_std)))
        for i in range(0, 100):
            testFile.write(str(beam_f2[0][i]))
            testFile.write('      ')
            testFile.write(str(beam_f2[1][i]))
            testFile.write('\n')

        testFile.write("-------------------------------------\n\n")

    testFile.write("-------------------------------------\n")
    testFile.write("-------------------------------------\n\n\n")

    testFile.close()

    #
    # # Create Arrays for the plot
    # x_axis = []
    # for i in range(100):
    #     x_axis.append(i + 1)
    # x_pos = np.arange(len(x_axis))
    #

    # # Build the plot for f1 values
    # plt.plot(x_axis, hill_f1_vals, 'black')
    # plt.xlabel("Random Pts (numbered)")
    # plt.ylabel("Value for f1")
    # plt.title('Hill Climbing: Max Value for 100 pts, Step Size = {0}'
    #           '\n Mean ={1}\n Std = {2}'.format(str(step_size), str(hill_f1_vals_mean), str(hill_f1_vals_std)))
    # plt.savefig('hill_f1_vals_{0}.png'.format(str(step_size)))
    # plt.show()
    #
    # # Build the plot for f1 # steps
    # plt.plot(x_axis, hill_f1_steps, 'black')
    # plt.xlabel("Random Pts (numbered)")
    # plt.ylabel("# Steps for f1")
    # plt.title('Hill Climbing: # Steps to Max for 100 pts, Step Size = {0}'
    #           '\n Mean ={1}\n Std = {2}'.format(str(step_size), str(hill_f1_steps_mean), str(hill_f1_steps_std)))
    # plt.savefig('hill_f1_numsteps_{0}.png'.format(str(step_size)))
    # plt.show()
    #
    # # Build the plot for f2 values
    # plt.plot(x_axis, hill_f2_vals, 'black')
    # plt.xlabel("Random Pts (numbered)")
    # plt.ylabel("Value for f2")
    # plt.title('Hill Climbing: Max Value for 100 pts, Step Size = {0}'
    #           '\n Mean ={1}\n Std = {2}'.format(str(step_size), str(hill_f2_vals_mean), str(hill_f2_vals_std)))
    # plt.savefig('hill_f2_vals_{0}.png'.format(str(step_size)))
    # plt.show()
    #
    # # Build the plot for f2 # steps
    # plt.plot(x_axis, hill_f2_steps, 'black')
    # plt.xlabel("Random Pts (numbered)")
    # plt.ylabel("# Steps for f2")
    # plt.title('Hill Climbing: # Steps to Max for 100 pts, Step Size = {0}'
    #           '\n Mean ={1}\n Std = {2}'.format(str(step_size), str(hill_f2_steps_mean), str(hill_f2_steps_std)))
    # plt.savefig('hill_f2_numsteps_{0}.png'.format(str(step_size)))
    # plt.show()

# for step_size in [0.01, 0.05, 0.1, 0.2]:
#     for beam_size in [2, 4, 8, 16]:
#         beam_f1 = use_algo("f1", "beam", step_size, beam_size)
#         beam_f2 = use_algo("f2", "beam", step_size, beam_size)
#
#         beam_f1_vals = np.array(beam_f1[1])
#         beam_f1_steps = np.array(beam_f1[2])
#         beam_f2_vals = np.array(beam_f2[1])
#         beam_f2_steps = np.array(beam_f2[2])
#
#         beam_f1_vals_mean = np.mean(beam_f1_vals)
#         beam_f1_steps_mean = np.mean(beam_f1_steps)
#         beam_f2_vals_mean = np.mean(beam_f2_vals)
#         beam_f2_steps_mean = np.mean(beam_f2_steps)
#
#         beam_f1_vals_std = np.std(beam_f1_vals)
#         beam_f1_steps_std = np.std(beam_f1_steps)
#         beam_f2_vals_std = np.std(beam_f2_vals)
#         beam_f2_steps_std = np.std(beam_f2_steps)
#
#         # Build the plot for f1 values
#         plt.plot(x_axis, beam_f1_vals, 'black')
#         plt.xlabel("Random Pts (numbered)")
#         plt.ylabel("Value for f1")
#         plt.title('Beam Search: Max Value for 100 pts, Step Size = {0}, Beam Size = {3}'
#                   '\n Mean ={1}\n Std = {2}'.format(str(step_size), str(beam_f1_vals_mean), str(beam_f1_vals_std), str(beam_size)))
#         plt.savefig('beam_f1_vals_{0}_{1}.png'.format(str(step_size), str(beam_size)))
#         plt.show()
#
#         # Build the plot for f1 # steps
#         plt.plot(x_axis, beam_f1_steps, 'black')
#         plt.xlabel("Random Pts (numbered)")
#         plt.ylabel("# Steps for f1")
#         plt.title('Beam Search: # Steps to Max for 100 pts, Step Size = {0}, Beam Size = {3}'
#                   '\n Mean ={1}\n Std = {2}'.format(str(step_size), str(beam_f1_steps_mean), str(beam_f1_steps_std), str(beam_size)))
#         plt.savefig('beam_f1_numsteps_{0}_{1}.png'.format(str(step_size), str(beam_size)))
#         plt.show()
#
#         # Build the plot for f2 values
#         plt.plot(x_axis, beam_f2_vals, 'black')
#         plt.xlabel("Random Pts (numbered)")
#         plt.ylabel("Value for f2")
#         plt.title('Beam Search: Max Value for 100 pts, Step Size = {0}, Beam Size = {3}'
#                   '\n Mean ={1}\n Std = {2}'.format(str(step_size), str(beam_f2_vals_mean), str(beam_f2_vals_std), str(beam_size)))
#         plt.savefig('beam_f2_vals_{0}_{1}.png'.format(str(step_size), str(beam_size)))
#         plt.show()
#
#         # Build the plot for f2 # steps
#         plt.plot(x_axis, beam_f2_steps, 'black')
#         plt.xlabel("Random Pts (numbered)")
#         plt.ylabel("# Steps for f2")
#         plt.title('Beam Search: # Steps to Max for 100 pts, Step Size = {0}, Beam Size = {3}'
#                   '\n Mean ={1}\n Std = {2}'.format(str(step_size), str(beam_f2_steps_mean), str(beam_f2_steps_std), str(beam_size)))
#         plt.savefig('beam_f2_numsteps_{0}_{1}.png'.format(str(step_size), str(beam_size)))
#         plt.show()
