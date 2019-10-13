def matchingStrings(strings, queries):
    counting_list, count = [], 0
    queries_length, strings_length = len(queries), len(strings)
    for i in range(queries_length):
        for j in range(strings_length):
            if queries[i] == strings[j]:
                count += 1
        counting_list.append(count)
        count = 0
    return counting_list

if __name__ == '__main__':
    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    print('\n'.join(map(str, res)))
