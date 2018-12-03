def main():
    current_input = _read_input_from_file()
    check_sum = _calculate_check_sum(current_input)
    print("Check Sum :",str(check_sum))

def _calculate_check_sum(inputValues):
    two_count = 0
    three_count = 0
    
    for box_id in inputValues:
        letter_count_dict = dict()
        for letter in box_id:
            if(letter in letter_count_dict):
                letter_count_dict[letter] += 1
            else:
                letter_count_dict[letter] = 1
                
        if any(letter_count == 2 for __,letter_count in letter_count_dict.items()):
            two_count +=1
        if any(letter_count == 3 for __,letter_count in letter_count_dict.items()):
            three_count +=1
            
    return two_count * three_count
            
def _read_input_from_file():
    with open('input.txt') as f:
        lines = f.read().splitlines();
    return lines;


main();
