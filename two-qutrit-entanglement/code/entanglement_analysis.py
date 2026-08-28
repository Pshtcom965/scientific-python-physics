import numpy as np
import matplotlib.pyplot as plt


def generate_random_coefficient_matrix():
    """
    Generate a normalized random complex 3x3 coefficient matrix C.
    """

    C = np.random.randn(3, 3) + 1j * np.random.randn(3, 3)

    # Normalize the two-qutrit state
    C = C / np.linalg.norm(C)

    return C


def calculate_reduced_density_matrix(C):
    """
    Calculate the reduced density matrix:
        rho_A = C C^\u2020
    """

    return C @ C.conj().T


def calculate_entanglement_measures(rho_A):
    """
    Calculate the eigenvalues, I-concurrence C_I,
    and determinant-based invariant G.
    """

    eigenvalues = np.linalg.eigvalsh(rho_A)

    # Remove tiny numerical negative values
    eigenvalues = np.clip(eigenvalues, 0, None)

    # Normalize eigenvalues to avoid numerical round-off errors
    eigenvalues = eigenvalues / np.sum(eigenvalues)

    # I-concurrence
    purity = np.sum(eigenvalues**2)
    C_I = np.sqrt(2 * (1 - purity))

    # Determinant-based geometric invariant
    G = 3 * np.sqrt(3) * np.sqrt(
        np.prod(eigenvalues)
    )

    return eigenvalues, C_I, G


def check_physical_constraint(C_I, G, tolerance=1e-10):
    """
    Check the analytic constraint from Eq. (16):

    C_I^6 - C_I^4
    - 72 C_I^2 G^2
    + 432 G^4
    + 64 G^2 <= 0
    """

    value = (
        C_I**6
        - C_I**4
        - 72 * C_I**2 * G**2
        + 432 * G**4
        + 64 * G**2
    )

    return value <= tolerance


def generate_data(number_of_states=5000):
    """
    Generate random two-qutrit states and calculate
    C_I and G for each state.
    """

    concurrence_values = []
    geometric_values = []

    for _ in range(number_of_states):

        C = generate_random_coefficient_matrix()

        rho_A = calculate_reduced_density_matrix(C)

        eigenvalues, C_I, G = calculate_entanglement_measures(rho_A)

        if check_physical_constraint(C_I, G):
            concurrence_values.append(C_I)
            geometric_values.append(G)

    return np.array(concurrence_values), np.array(geometric_values)


def main():

    C_I, G = generate_data(number_of_states=5000)

    print(f"Number of valid states: {len(C_I)}")
    print(f"Maximum C_I: {np.max(C_I):.6f}")
    print(f"Maximum G: {np.max(G):.6f}")

    plt.figure(figsize=(8, 6))

    plt.scatter(
        C_I,
        G,
        s=8,
        alpha=0.5,
        label="Random two-qutrit states"
    )

    plt.xlabel(r"$C_I$")
    plt.ylabel(r"$G$")
    plt.title("Two-Qutrit Entanglement: $C_I$ vs $G$")
    plt.legend()
    plt.tight_layout()

    plt.show()


if __name__ == "__main__":
    main()
