def count_vowels(text: str) -> int:
    vowels_list = ['a', 'e', 'u', 'i', 'o']
    vowels_counter = 0
    text = text.lower()
    for char in text:
        if char in vowels_list:
            vowels_counter += 1 
    
    return vowels_counter


print(count_vowels("If you're using a Copilot Business or Copilot Enterprise plan."))