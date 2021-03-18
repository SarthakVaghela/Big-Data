import datetime
from collections import defaultdict

DEBUG = True
rmv_freq_items = True

def a_priori(input_file, number_bask, sup_threshold):
    min_req_occ = number_bask * sup_threshold

    global kp
    ite = defaultdict(lambda: 0)
    with open(input_file, 'r') as fp:
        for basket_index in range(number_bask):
            l = fp.readline()
            temp_it = l.split(' ')[: -1]

            for i in temp_it:
                ite[i] += 1

    if DEBUG:
        print("Now the number of unique items: {}".format(len(ite)))

    if rmv_freq_items:
        to_rm = []
        for i in ite:
            if ite[i] < min_req_occ:
                to_rm.append(i)

        for i in to_rm:
            ite.pop(i)

        if DEBUG:
            print("{} infrequent items have been removed.".format(len(to_rm)))
            print("Unique frequent items: {}".format(len(ite)))


    freq_p = defaultdict(lambda: 0)
    if DEBUG:
        print("To consider frequent, the minimum nuber of occurence: {}".format(min_req_occ))

    with open(input_file, 'r') as fp:
        for basket_index in range(number_bask):
            l = fp.readline()
            temp_it = l.split(' ')[: -1]

            for a in range(len(temp_it) - 1):
                for b in range(a + 1, len(temp_it)):
                    # Making sure both ite are frequent
                    if ite[temp_it[a]] > min_req_occ and ite[temp_it[b]] > min_req_occ:
                        freq_p[(a, b)] += 1

    prev_total_frequent_pairs = len(freq_p)
    p_t_p = []
    for kp in freq_p:
        if freq_p[kp] < min_req_occ:
            p_t_p.append(kp)

    for p in p_t_p:
        if DEBUG:
            print("Popping {}: {} occurrences.".format(p, freq_p[p]))
        freq_p.pop(p)

    if DEBUG:
        print("Before verification: {}".format(prev_total_frequent_pairs))
        print("After verification: {}".format(len(freq_p)))

        print("------ Frequent pairs ------")
        for kp in freq_p:
            print("{}: {}".format(kp, freq_p[kp]))

    return freq_p


def main():
    ch_p = float(input("What percentage of file you want to go through?: "))
    if ch_p > 1 or ch_p < 0:
        print("The input must be between 0.0 and 1.0.")
        return

    sup_threshold = float(input("What is your support threshold?: "))
    if sup_threshold > 1 or sup_threshold < 0:
        print("The input must be between 0.0 and 1.0.")
        return

    st_t = datetime.datetime.now()
    print("Start time: {}".format(st_t))
    print("")

    input_file = 'retail.txt'
    t_n_l = 0
    with open(input_file, 'r') as fp:
        while fp.readline():
            t_n_l += 1

    number_bask = int(t_n_l * ch_p)
    if DEBUG:
        print("Number of baskets: {}".format(number_bask))

    freq_p = a_priori(input_file, number_bask, sup_threshold)

    end_time = datetime.datetime.now()
    diff_time = end_time - st_t
    print("")
    print("Start time: {}".format(st_t))
    print("End time: {}".format(end_time))
    print("Total elapsed time: {}".format(diff_time))


if __name__ == "__main__":
    main()