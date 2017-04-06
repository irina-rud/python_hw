def read_pi():
    with open('pi.txt') as f:
        text = f.read()[2:]
    seq = ''.join(text.split('\n'))
    return seq


def find_subseqs(sub, seq):
    results = []
    begin = seq.find(sub)
    while begin != -1:
        results.append(begin)
        begin = seq.find(sub, begin + len(sub))

    return results


def print_results(results, max_indexes=5):
    print "Found", len(results), "results."
    print "Positions:",
    for res in results[:max_indexes]:
        print res,
    if len(results) > max_indexes:
        print "..."
    else:
        print


def main():
    pi_seq = read_pi()
    sub = raw_input("Enter sequence to search for.\n> ")
    res = find_subseqs(sub, pi_seq)
    print_results(res)


main()