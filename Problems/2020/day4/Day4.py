# not complete
import re
def valid_passport(passport):
    print(passport)
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    is_passport = 1
    for field in fields:
        if field not in passport:
            print('is valid\n')
            is_passport = 0
            break
    return is_passport


def valid_passports_with_validation(passport):
    if valid_passport(passport) == 1:
        print('checking valid')
        byr_index = passport.index('byr') + 4
        iyr_index = passport.index('iyr') + 4
        eyr_index = passport.index('eyr') + 4
        hgt_index = passport.index('hgt') + 4
        ecl_index = passport.index('ecl') + 4
        # hcl_index = passport.index('hcl') + 4
        pid_index = passport.index('pid') + 4
        # print('byr', passport[byr_index:byr_index + 5])
        if not 1920 <= int(passport[byr_index:byr_index + 5]) <= 2002:
            return 0
        # print('iyr', passport[iyr_index:iyr_index + 5])
        if not 2010 <= int(passport[iyr_index:iyr_index + 5]) <= 2020:
            return 0
        # print('eyr', passport[eyr_index:eyr_index + 5])
        if not 2020 <= int(passport[eyr_index:eyr_index + 5]) <= 2030:
            return 0
        # if 'in' in passport:
        #     print('hgt', int(passport[hgt_index:passport.index('in')]))
        # else:
        #     print('hgt', int(passport[hgt_index:passport.index('cm')]))
        if not ('in' in passport and 59 <= int(passport[hgt_index:passport.index('in')]) <= 76 or \
                'cm' in passport and 150 <= int(passport[hgt_index:passport.index('cm')]) <= 193):
            return 0
        # print('hcl', passport[hcl_index:hcl_index + 7])
        if not re.findall('hcl:#([0-9a-f]+)', passport):
            return 0
        # print('ecl', passport[ecl_index:ecl_index + 4])
        if not passport[ecl_index:ecl_index + 4] == 'amb' or passport[ecl_index:ecl_index + 4] == 'blu' or \
                passport[ecl_index:ecl_index + 4] == 'brn' or passport[ecl_index:ecl_index + 4] == 'gry' or \
                passport[ecl_index:ecl_index + 4] == 'grn' or passport[ecl_index:ecl_index + 4] == 'hzl' \
                or passport[ecl_index:ecl_index + 4] == 'oth':
            return 0
        # print('pid', passport[pid_index: pid_index + 10])
        if not passport[pid_index: pid_index + 10].isdecimal():
            return 0
    return 1


# Driver code
if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()
        last = lines[-1]
        num_passports = 0
        num_valid_passports = 0
        passport = ''
        for line in lines:
            # read up to blank line
            if line == '\n' or line == lines[-1]:
                num_passports += valid_passport(passport)
                num_valid_passports += valid_passports_with_validation(passport)
                passport = ''
            else:
                passport += line
    print(num_passports)
    print(num_valid_passports)
