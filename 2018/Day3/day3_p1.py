import re;

def main():
    current_input = _read_input_from_file()
    overlapped_claims = _calculate_overlapped_claims(current_input)
    print("Overlapped claims :",str(overlapped_claims))

def _calculate_overlapped_claims(inputValues):
    claims_values_expression = "#(\d*) @ (\d*),(\d*): (\d*)x(\d*)"
    claims_values_regex = re.compile(claims_values_expression)
    encountered_overlaps = set()

    for i in range(len(inputValues)):
        for j in (i,len(inputValues)):
            current_match = claims_values_regex.match(claim)
            claim_id = current_match.group(1)

            #distances
            left_dist = current_match.group(2)
            top_dist = current_match.group(3)

            #dimensions
            width = current_match.group(4)
            height = current_match.group(5)

            print("Id:",claim_id)
            print("LeftDist:", left_dist)
            print("TopDist:",top_dist)
            print("Width:",width)
            print("Height:",height)
        
def _read_input_from_file():
    with open('example_input.txt') as f:
        lines = f.read().splitlines();
    return lines;


main();
