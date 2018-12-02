#regex  - used for capturing values from input
import re;

def main():
    current_input = _read_input_from_file();
    frequency = _calculate_frequency(current_input);
    print("Frequency:", str(frequency));

def _calculate_frequency(inputValues):
    operator_number_expression = "([-,+]{1})(\d+)"
    operator_number_regex = re.compile(operator_number_expression)

    frequency = 0
    for line in inputValues:
        currentMatch = operator_number_regex.match(line)
        if(currentMatch != None):
            operator = currentMatch.group(1)
            value = currentMatch.group(2)

            if(operator == "+"):
                frequency += int(value)
            elif(operator == "-"):
                frequency -= int(value)
        else:
            print("Match not found")
    return frequency
    

def _read_input_from_file():
    with open('input.txt') as f:
        lines = f.read().splitlines();
    return lines;
    
main();
