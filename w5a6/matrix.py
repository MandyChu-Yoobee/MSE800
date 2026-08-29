class Matrix:
    def __init__(self, matrix_data):
        """Initialize matrix from a 2D list, validate matrix format"""
        self.matrix = matrix_data
        # get rows and columns
        self.rows = len(matrix_data)
        self.cols = len(matrix_data[0])

    def matrix_multiply(self, other_matrix):
        """
        Multiply two matrices: self * other_matrix
        return new Matrix object
        """
        # Check multiplication compatibility
        if self.cols != other_matrix.rows:
            raise ValueError(
                f"Cannot multiply: First matrix cols({self.cols}) must equal second matrix rows({other_matrix.rows})"
            )

        # Create empty result matrix M x P
        result_rows = self.rows
        result_cols = other_matrix.cols
        result = [[0 for _ in range(result_cols)] for _ in range(result_rows)]

        # Standard matrix multiplication loops
        for i in range(self.rows):
            for j in range(other_matrix.cols):
                total = 0
                for k in range(self.cols):
                    total += self.matrix[i][k] * other_matrix.matrix[k][j]
                result[i][j] = total

        return Matrix(result)

    def display(self):
        """Print matrix nicely"""
        for row in self.matrix:
            print(row)


# Demo execution: M1 (3×5), M2 (5×2)
if __name__ == "__main__":
    # M1: 3 rows, 5 columns
    m1_data = [
        [1, 2, 3, 4, 5],
        [2, 3, 4, 5, 6],
        [3, 4, 5, 6, 7]
    ]
    # M2: 5 rows, 2 columns
    m2_data = [
        [1, 2],
        [3, 4],
        [5, 6],
        [7, 8],
        [9, 10]
    ]

    # Create Matrix objects
    M1 = Matrix(m1_data)
    M2 = Matrix(m2_data)

    print("==== Matrix M1 (3×5) ====")
    M1.display()
    print("\n==== Matrix M2 (5×2) ====")
    M2.display()

    # Perform multiplication
    product_matrix = M1.matrix_multiply(M2)
    print("\n==== Multiplication Result M1*M2 (3×2) ====")
    product_matrix.display()