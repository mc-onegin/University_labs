import os
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def external_multiphase_sort(input_file, output_file, chunk_size):
    temp_files = []
    file_counter = 0

    with open(input_file, 'r') as f:
        while True:
            chunk = []
            for k in range(chunk_size):
                line = f.readline()
                if not line:
                    break
                chunk.append(int(line))
            if not chunk:
                break

            sorted_chunk = merge_sort(chunk)
            temp_file = f"temp_run_{file_counter}.txt"
            temp_files.append(temp_file)
            file_counter += 1

            with open(temp_file, 'w') as tmp_f:
                tmp_f.write('\n'.join(map(str, sorted_chunk)) + '\n')

    files = [open(f, 'r') for f in temp_files]
    current_values = []

    for i, f in enumerate(files):
        line = f.readline()
        if line:
            current_values.append((int(line), i))

    with open(output_file, 'w') as out:
        while current_values:
            min_val, min_idx = current_values[0]
            min_pos = 0
            for i, (value, index) in enumerate(current_values[1:], 1):
                if value < min_val:
                    min_val, min_idx = value, index
                    min_pos = i

            out.write(f"{min_val}\n")
            line = files[min_idx].readline()
            if line:
                current_values[min_pos] = (int(line), min_idx)
            else:
                current_values.pop(min_pos)

    for f in files:
        f.close()

    for tmp_file in temp_files:
        os.remove(tmp_file)


external_multiphase_sort('input_12.txt', 'output_12.txt', chunk_size=3)