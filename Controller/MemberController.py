

import datetime
import random


class MemberController:
    def generate_member_id(self):
        print("generate_member_id")
        year = datetime.datetime.now().year.__str__()[2:]
        intyear = int(year[-1])

        random_numbers = list()
        random_numbers.append(intyear)

        for i in range(0, 7):
            random_numbers.append(random.randint(0, 9))
        
        checksum = sum(random_numbers) % 10
        random_numbers.append(checksum)

        member_id = year[0] + ''.join(map(str, random_numbers))
    
        print(f'Generated member ID: {member_id}')
        input('Press enter to continue...')
        return member_id
