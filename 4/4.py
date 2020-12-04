#!/usr/bin/python3

import re

class UnknownFieldError(Exception):
    def __init__(self, field):
        self.field = field
        
    def __str__(self):
        return (f"The field {self.field} is not one of the accepted passport "
                f"fields")

class AbsentFieldError(Exception):
    def __init__(self, field):
        self.field = field
        
    def __str__(self):
        return f"The field {self.field} is not present for this passport"      

class PassportFields(object):
    PASSPORT_FIELDS = [
        "byr", 
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
        "cid",
    ]

class Passport(object):
    def __init__(self):
        self.attributes = dict()
    
    def add_attr(self, attr, val):
        if attr not in PassportFields.PASSPORT_FIELDS:
            raise UnknownFieldError(attr)
        else:
            self.attributes[attr] = val
    
    def has_attr(self, attr):
        return attr in self.attributes
        
    def get_attr(self, attr):
        if not attr in self.attributes:
            raise AbsentFieldError(attr)
        else:
            return self.attributes[attr]
        
        
class PassportScanner(object):
    def __init__(self):
        self.passports = []
    
    def _validate_byr(self, val):
        return (int(val) >= 1920 and int(val) <= 2002)
            
    def _validate_iyr(self, val):
        return (int(val) >= 2010 and int(val) <= 2020)
    
    def _validate_eyr(self, val):
        return (int(val) >= 2020 and int(val) <= 2030)
        
    def _validate_hgt(self, val):
        p = re.compile("^(?P<hgt_num>[0-9]+)(?P<unit>cm|in)$")
        m = p.match(val)
        if not m: 
            return False
        if m.group("unit") == "cm":
            return int(m.group("hgt_num")) >= 150 and int(m.group("hgt_num")) <= 193
        else:
            return int(m.group("hgt_num")) >= 59 and int(m.group("hgt_num")) <= 76
    
    def _validate_hcl(self, val):
        p = re.compile(r"^#[0-9a-f]{6}$")
        return p.match(val) is not None
    
    def _validate_ecl(self, val):
        accepted = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        return val in accepted
    
    def _validate_pid(self, val):
        p = re.compile(r"^[0-9]{9}$")
        return p.match(val) is not None
    
    def _validate_cid(self, val):
        return True

    def _validate_passport(self, passport, validatefields):
        for field in PassportFields.PASSPORT_FIELDS:
            if not passport.has_attr(field):
                if field != "cid": # this is the hack
                    return False
            elif validatefields:
                val = passport.get_attr(field)
                if not getattr(self, "_validate_{}".format(field))(val):
                    return False
        return True
    
    def read(self):
        with open("4/input.txt", 'r') as f:
            lines = f.readlines()
        
        # Split the batch file into lists of password lines. Make sure to add 
        # the last one 
        passport_lines = []
        start = 0
        for current, line in enumerate(lines):
            if line == "\n":
                passport_lines.append(lines[start:current])
                start = current + 1
        passport_lines.append(lines[start:])
        
        # get the entries out of the line and add to dict
        for passport_line in passport_lines:
            p = Passport()
            for line in passport_line:
                for entry in line.strip("\n").split(" "):
                    p.add_attr(entry.split(":")[0], entry.split(":")[1])
            self.passports.append(p)
       
    def validate(self, validatefields):                
        validcount = sum(1 for p in self.passports if self._validate_passport(p, validatefields))
        print(f"valid count is {validcount}")
        
ps = PassportScanner()
ps.read()
print("PART 1:")
ps.validate(False)
print("PART 2:")
ps.validate(True)
        