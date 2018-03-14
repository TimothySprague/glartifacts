def tabulate(rows, sortby=None):
    col_sizes = autosize(rows)
    print_row(rows.pop(0), col_sizes)
    if 'key' in sortby:
        sortby = [sortby]
    for term in sortby:
        rows.sort(key=term['key'], reverse=term.get('reverse', False))

    print_spacer(col_sizes)
    for r in rows:
        print_row(r, col_sizes)

def print_row(row, col_sizes):
    for i, col in enumerate(row):
        print(str(col).ljust(col_sizes[i]+2), end="")
    print("")

def print_spacer(col_sizes):
    spacer = []
    for c in col_sizes:
        spacer.append("-"*c)
    print_row(spacer, col_sizes)

def autosize(rows):
    sizes = []
    for r in rows:
        col_count = len(r) - len(sizes)
        if col_count>0:
            sizes.extend([0]*col_count)

        for i, col in enumerate(r):
            col = str(col)
            if len(col) > sizes[i]:
                sizes[i] = len(col)

    return sizes

storage_units = ['B', 'KiB', 'MiB']
size_format = '{:.2f} {}'
def humanize_size(size):
    for unit in storage_units:
        if size < 1024:
            return size_format.format(size, unit)

        size = size / 1024

    return size_format.format(size, "GiB")
