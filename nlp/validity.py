def is_valid_syllogism(premises, conclusion):
    """
    Check if a syllogism is valid using a more nuanced approach.
    This implementation is still limited but handles more cases correctly.
    
    :param premises: List of premise strings
    :param conclusion: Conclusion string
    :return: Boolean indicating validity
    """
    # Extract terms from premises and conclusion
    premise_terms = set()
    for premise in premises:
        premise_terms.update(premise.lower().split())
    conclusion_terms = set(conclusion.lower().split())
    
    # Check if all terms in the conclusion appear in the premises
    if not conclusion_terms.issubset(premise_terms):
        return False
    
    # Check for specific valid syllogism patterns
    if len(premises) == 2:
        # All A are B, All B are C, therefore All A are C
        if (premises[0].startswith("All") and premises[1].startswith("All") and
            conclusion.startswith("All") or conclusion.startswith("Therefore, all")):
            return True
        
        # No A are B, All C are B, therefore No C are A
        if (premises[0].startswith("No") and premises[1].startswith("All") and
            (conclusion.startswith("No") or conclusion.startswith("Therefore, no"))):
            return True
        
        # All A are B, No C are B, therefore No C are A
        if (premises[0].startswith("All") and premises[1].startswith("No") and
            (conclusion.startswith("No") or conclusion.startswith("Therefore, no"))):
            return True
    
    # If no valid pattern is found, return False
    return False

# Example usage
if __name__ == "__main__":
    premises = [
        "No black dogs are fish that live above ground",
        "Some catfish are fish that live below ground"
    ]
    conclusion = "Therefore, black dogs are not catfish"
    
    is_valid = is_valid_syllogism(premises, conclusion)
    print(f"The syllogism is {'valid' if is_valid else 'invalid or indeterminable'}.")
