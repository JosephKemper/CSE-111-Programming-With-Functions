from sentences import get_prepositional_phrase

# Test Singular Prepositional phrases
for _ in range(4):
    singular_phrase = get_prepositional_phrase(1)
    singular_list = singular_phrase.split()
    
    print(singular_list[0])
    print(singular_list[1])
    print(singular_list[2])

# Test Plural Prepositional phrases
for _ in range(4):
    plural_phrase = get_prepositional_phrase(2)
    print(plural_phrase[0])
    print(plural_phrase[1])
    print(plural_phrase[2])
