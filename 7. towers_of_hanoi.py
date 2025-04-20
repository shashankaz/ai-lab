def towers_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    # Move n-1 disks from source to auxiliary
    towers_of_hanoi(n - 1, source, auxiliary, target)
    # Move nth disk from source to target
    print(f"Move disk {n} from {source} to {target}")
    # Move n-1 disks from auxiliary to target
    towers_of_hanoi(n - 1, auxiliary, target, source)

# Example: Move 3 disks from A to C using B
n = 3
towers_of_hanoi(n, 'A', 'C', 'B')
