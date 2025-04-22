class FuzzySet:
    def __init__(self, elements):
        self.elements = elements  # Dictionary {element: membership_value}
    
    def union(self, other):
        return FuzzySet({x: max(self.elements.get(x, 0), other.elements.get(x, 0)) for x in set(self.elements) | set(other.elements)})
    
    def intersection(self, other):
        return FuzzySet({x: min(self.elements.get(x, 0), other.elements.get(x, 0)) for x in set(self.elements) & set(other.elements)})
    
    def complement(self):
        return FuzzySet({x: 1 - self.elements[x] for x in self.elements})
    
    def difference(self, other):
        return FuzzySet({x: min(self.elements.get(x, 0), 1 - other.elements.get(x, 0)) for x in self.elements})
    
    def __str__(self):
        return str(self.elements)

# Example Fuzzy Sets
A = FuzzySet({'x1': 0.2, 'x2': 0.7, 'x3': 1.0})
B = FuzzySet({'x1': 0.5, 'x2': 0.4, 'x3': 0.8})

print("Union:", A.union(B))
print("Intersection:", A.intersection(B))
print("Complement of A:", A.complement())
print("Difference A - B:", A.difference(B))

# Fuzzy Relations (Cartesian Product)
def cartesian_product(A, B):
    return {(a, b): min(A.elements[a], B.elements[b]) for a in A.elements for b in B.elements}

R = cartesian_product(A, B)
print("\nFuzzy Relation (A × B):", R)

# Max-Min Composition
def max_min_composition(R1, R2):
    result = {}
    for (a, b) in R1:
        for (c, d) in R2:
            if b == c:
                result[(a, d)] = max(result.get((a, d), 0), min(R1[(a, b)], R2[(c, d)]))
    return result

# Example Fuzzy Relations
R1 = cartesian_product(A, B)
R2 = cartesian_product(B, A)
composition = max_min_composition(R1, R2)
print("\nMax-Min Composition:", composition)