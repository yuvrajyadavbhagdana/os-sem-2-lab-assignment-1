#  Complete Python Code 
# Banker's Algorithm Implementation
# Operating System Lab Assignment

def calculate_need(max_matrix, allocation, n, m):
    need = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(max_matrix[i][j] - allocation[i][j])
        need.append(row)
    return need


def bankers_algorithm(n, m, allocation, max_matrix, available):
    need = calculate_need(max_matrix, allocation, n, m)

    print("\nNeed Matrix:")
    for row in need:
        print(row)

    work = available.copy()
    finish = [False] * n
    safe_sequence = []

    while len(safe_sequence) < n:
        found = False

        for i in range(n):
            if not finish[i]:
                # Check if need <= work
                if all(need[i][j] <= work[j] for j in range(m)):
                    # Allocate resources
                    for j in range(m):
                        work[j] += allocation[i][j]

                    safe_sequence.append(i)
                    finish[i] = True
                    found = True

        if not found:
            break

    if len(safe_sequence) == n:
        print("\nSystem is in SAFE state.")
        print("Safe Sequence:", " -> ".join([f"P{i}" for i in safe_sequence]))
    else:
        print("\nSystem is in UNSAFE state (Deadlock may occur).")


# -------------------------------
# TASK 1: Input System Data
# -------------------------------

n = int(input("Enter number of processes: "))
m = int(input("Enter number of resources: "))

print("\nEnter Allocation Matrix:")
allocation = []
for i in range(n):
    row = list(map(int, input(f"P{i}: ").split()))
    allocation.append(row)

print("\nEnter Maximum Matrix:")
max_matrix = []
for i in range(n):
    row = list(map(int, input(f"P{i}: ").split()))
    max_matrix.append(row)

print("\nEnter Available Resources:")
available = list(map(int, input().split()))

# -------------------------------
# Run Banker's Algorithm
# -------------------------------

bankers_algorithm(n, m, allocation, max_matrix, available)
