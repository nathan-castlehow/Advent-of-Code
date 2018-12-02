def main():
    current_input = _read_input_from_file()
    common_letters = _calculate_common_letters(current_input)
    print("Common letters :",common_letters)

def _calculate_common_letters(inputValues):
    box_id_1 =  ""
    box_id_2 = ""
    found = False

    #todo convert to while loop and use zip
    for i in range(len(inputValues)):
        box_id_1 = inputValues[i]
        for j in range(i,len(inputValues)):
            count = 0
            box_id_2 = inputValues[j]
            for k in range(len(box_id_1)):
                if(box_id_1[k] != box_id_2[k]):
                    count += 1
            if(count == 1):
                found = True
                break
        if(found):
            break

    final_common_letters = ""
    for i in range(len(box_id_1)):
        if(box_id_1[i] == box_id_2[i]):
            final_common_letters += box_id_1[i]
    return final_common_letters

            
def _read_input_from_file():
    with open('input.txt') as f:
        lines = f.read().splitlines();
    return lines;


main();
