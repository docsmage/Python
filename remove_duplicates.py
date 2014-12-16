def remove_duplicates(numbers):
    no_dups = []
    for i in numbers:
        if i not in no_dups:
            no_dups.append(i)
    return no_dups

print remove_duplicates(["a", "a", "b", 1, 2, 2, 3])
print remove_duplicates([6, 6, 6, 6, 6])