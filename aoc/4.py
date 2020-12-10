#!/usr/bin/python3

from . import utils
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
        if attr not in PASSPORT_FIELDS:
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
    
    ###########################################################################
    # Per-passport field validate definitions.                                #
    # MUST define a _validate_{field} fn for each field in PASSPORT_FIELDS    #
    ###########################################################################
    def _validate_int(self, val, min, max):
        return (int(val) >= min and int(val) <= max)
    
    def _validate_regex(self, val, regex):
        p = re.compile(regex)
        return p.match(val) is not None
        
    _validate_cid = (lambda self, x: True)
    _validate_byr = (lambda self, x: self._validate_int(x, 1920, 2002))
    _validate_iyr = (lambda self, x: self._validate_int(x, 2010, 2020))
    _validate_eyr = (lambda self, x: self._validate_int(x, 2020, 2030))
    _validate_hcl = (lambda self, x: self._validate_regex(x, r"^#[0-9a-f]{6}$"))
    _validate_pid = (lambda self, x: self._validate_regex(x, r"^[0-9]{9}$"))
        
    def _validate_hgt(self, val):
        p = re.compile("^(?P<hgt_num>[0-9]+)(?P<unit>cm|in)$")
        m = p.match(val)
        if not m: 
            return False
        if m.group("unit") == "cm":
            return self._validate_int(m.group("hgt_num"), 150, 193)
        else:
            return self._validate_int(m.group("hgt_num"), 59, 76)
        
    def _validate_ecl(self, val):
        accepted = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        return val in accepted

    def _validate_passport(self, passport, validatefields):
        for field in PASSPORT_FIELDS:
            if not passport.has_attr(field):
                if field != "cid": # this is the hack
                    return False
            elif validatefields:
                val = passport.get_attr(field)
                if not getattr(self, "_validate_{}".format(field))(val):
                    return False
        return True
    
    ###########################################################################
    # External API                                                            #
    ###########################################################################
    def read(self):
        sections = utils.get_sections(4)
                
        # Get the entries out of the passport and add to dict. 
        # Passports separated by blank line (\n\n)
        for passport in sections:
            p = Passport()
            for line in passport.split("\n"):
                for entry in line.split(" "):
                    p.add_attr(entry.split(":")[0], entry.split(":")[1])
            self.passports.append(p)
       
    def validate(self, validatefields):                
        validcount = sum(1 for p in self.passports if self._validate_passport(p, validatefields))
        print(validcount)

def main():       
    ps = PassportScanner()
    ps.read()
    print("PART 1:")
    ps.validate(False)
    print("PART 2:")
    ps.validate(True)