# Fonction pour vérifier si une valeur est valide pour une case donnée
def is_valid(grid, row, col, num):
    # Vérifier si le nombre est déjà présent dans la ligne
    for i in range(9):
        if grid[row][i] == num:
            return False
    
    # Vérifier si le nombre est déjà présent dans la colonne
    for i in range(9):
        if grid[i][col] == num:
            return False
    
    # Vérifier si le nombre est déjà présent dans la région 3x3
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    
    # Si le nombre n'est pas déjà présent, il est valide
    return True

# Fonction pour résoudre le Sudoku
def solve_sudoku(grid):
    # Parcourir chaque case
    for row in range(9):
        for col in range(9):
            # Si la case est vide
            if grid[row][col] == 0:
                # Essayer chaque nombre possible
                for num in range(1, 10):
                    # Vérifier si le nombre est valide
                    if is_valid(grid, row, col, num):
                        # Si le nombre est valide, le placer dans la case
                        grid[row][col] = num

                        # Résoudre le reste du Sudoku avec la nouvelle case remplie
                        if solve_sudoku(grid):
                            return True

                        # Si la nouvelle case ne mène pas à une solution, revenir en arrière
                        grid[row][col] = 0

                # Si aucun nombre ne fonctionne, le Sudoku ne peut pas être résolu
                return False

    # Si toutes les cases sont remplies, le Sudoku est résolu
    return True

# Fonction pour afficher le Sudoku
def print_sudoku(grid):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
            if j == 2 or j == 5:
                print("|", end=" ")
        print()
        if i == 2 or i == 5:
            print("-" * 21)




# Exemple de grille de Sudoku à résoudre
grid = [
    [0, 0, 4, 0, 0, 0, 0, 0, 0],
    [0, 7, 5, 1, 0, 8, 0, 4, 0],
    [9, 0, 3, 7, 0, 4, 0, 8, 0],
    [0, 0, 2, 3, 0, 0, 4, 0, 9],
    [3, 4, 0, 6, 0, 5, 0, 1, 7],
    [7, 0, 6, 0, 0, 9, 8, 0, 0],
    [0, 3, 0, 8, 0, 7, 6, 0, 2],
    [0, 2, 0, 9, 0, 3, 1, 7, 0],
    [0, 0, 0, 0, 0, 0, 3, 0, 0]
]

print(solve_sudoku(grid))

print_sudoku(grid)