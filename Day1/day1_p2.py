#regex  - used for capturing values from input
import re

def main():
    current_input = _read_input_from_file();
    frequency = _calculate_frequency(current_input);
    print("Frequency:", str(frequency));

def _calculate_frequency(inputValues):
    operator_number_expression = "([-,+]{1})(\d+)"
    operator_number_regex = re.compile(operator_number_expression)
    encountered_frequencies = set()

    frequency = 0
    encountered_frequencies.add(frequency)
    repeat_found = False
    currentPos = 0;

    while(not repeat_found):
        currentInput = inputValues[currentPos % len(inputValues)]
        currentMatch = operator_number_regex.match(currentInput)
        if(currentMatch != None):
            operator = currentMatch.group(1)
            value = currentMatch.group(2)

            if(operator == "+"):
                frequency += int(value)
            elif(operator == "-"):
                frequency -= int(value)
 
            if(frequency in encountered_frequencies):
                repeat_found = True
            else:
                 encountered_frequencies.add(frequency)
        currentPos += 1
    return frequency

def _read_input_from_file():
    with open('input.txt') as f:
        lines = f.read().splitlines();
    return lines;
    
main();
