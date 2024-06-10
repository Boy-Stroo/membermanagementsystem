

import datetime
import random


class MemberController:
    def generate_member_id(self) -> str: 
        print("generate_member_id")
        year = datetime.datetime.now().year.__str__()[2:]
        intyear = int(year)

        random_numbers = list()
        # Add first to numbers of the year
        random_numbers.append(int(year[0]))
        random_numbers.append(int(year[1]))

        # Add 7 random numbers
        for i in range(0, 7):
            random_numbers.append(random.randint(0, 9))
        
        # Calculate and add checksum
        checksum = sum(random_numbers) % 10
        random_numbers.append(checksum)

        member_id = year[0] + ''.join(map(str, random_numbers))
    
        print(f'Generated member ID: {member_id}')
        input('Press enter to continue...')
        return member_id

if (__name__ == "__main__"):
    member_controller = MemberController()
    member_controller.generate_member_id()