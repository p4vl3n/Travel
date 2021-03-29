import re


given_text = input()

pattern = r"(@|#)(?P<word_one>[A-Za-z]{3,})\1\1(?P<word_two>[A-Za-z]{3,})\1"
matches = [obj.groupdict() for obj in re.finditer(pattern, given_text)]
mirror_pairs = []
if matches:
    print(f"{len(matches)} word pairs found!")
    for match in matches:
        if match['word_one'] == match['word_two'][::-1]:
            mirroring_pair = f"{match['word_one']} <=> {match['word_two']}"
            mirror_pairs.append(mirroring_pair)
    if mirror_pairs:
        print(f"The mirror words are:")
        print(", ".join(mirror_pairs))
    else:
        print(f"No mirror words!")
else:
    print(f"No word pairs found!\nNo mirror words!")