with open("input.txt") as f:
    data = list(map(int, f.read().split()))


def get_metadata(data, idx):
    metadatas = data[idx + 1]

    if data[idx] == 0:
        if metadatas == 0:
            return idx + 2, 0, 0
        else:
            return idx + metadatas + 2, sum(data[idx + 2:idx + 2 + metadatas]), sum(data[idx + 2:idx + 2 + metadatas])
    else:
        sums = 0
        current_value = 0
        values = []
        idx = idx + 2
        for x in range(data[idx - 2]):
            idx, partial_sum, value = get_metadata(data, idx)
            values.append(value)
            sums += partial_sum
        if metadatas != 0:
            for metadata in data[idx:idx + metadatas]:
                sums += metadata
                try:
                    current_value += values[metadata - 1]
                except:
                    pass

            idx += metadatas

        return idx, sums, current_value


checksums = get_metadata(data, 0)
print(checksums[1])
print(checksums[2])
