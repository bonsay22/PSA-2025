#!/usr/bin/env python3

class LP():
    def __init__(self, name, year, artist, duration):
        self._name = name
        self._year = year
        self._artist = artist
        self._duration = duration

    def to_string(self):
        out = "| {0:^20} | {1:^4} | {2:^20} | {3:^8} |".format(self._name, self._year, self._artist, self._duration)
        return out
    
class Library():
    def __init__(self):
        self._library = list()
        
    def insert_LP(self, lp):
        self._library.append(lp)
        
    def delete_LP(self, lp):
        self._library.remove(lp)
        
    def delete_LP(self,index):
        self.library.pop(index)
        
    def clean_library(self):
        self._library.clear()
            
    def seed_library(self):
        self.insert_LP(LP("Paradise City", 1987, "Guns & Roses", 100))        
        self.insert_LP(LP("Swimming", 2018, "Mac Miller", 120))
        self.insert_LP(LP("Banditi de Prague", 1995, "Kabat", 90))
        
            
    def to_string(self):
        out =  "|{}|\n".format("-"*68)
        out += "| ID | {:^20} | Year | {:^20} | Duration |\n".format("Title", "Artist")
        out += "|{}|\n".format("-"*68)
        i = 0
        for lp in self._library:
            out += "| {} {} \n".format(i,lp.to_string())
            i += 1
        return out
    
def main():
    library = Library()
    
    while True:
        print("|------------------|")
        print("|       Menu       |")    
        print("|------------------|")     
        print(" 1 - Add new LP.")
        print(" 2 - Remove LP.")
        print(" 3 - Clear Library.")
        print(" 4 - Print Library.")
        print(" 5 - Seed Library.")
        print(" q - Exit program")
        choice = input("Select choice: ")
    
        if choice[0] == "1":
            name = input("Enter title: ")
            year = input("Enter year: ")
            artist = input("Enter artist: ")
            duration = input("Enter duration: ")
            lp = LP(name, int(year), artist, int(duration))
            library.insert_LP(lp)
            continue
        if choice[0] == "2":
            print(library.to_string())
            index = input("Enter index LP to delete: ")
            try:
                index = int(index_str)
                library.delete_LP_index(index)
            except ValueError:
                print("ERROR: WRONG index selected. ")
                
            continue
        if choice[0] == "3":
            library.clean_library()
            continue
        if choice[0] == "4":
            print(library.to_string())
            input("Press any key to continue")
            continue
        if choice[0] == "5":
            library.seed_library()
            continue
        if choice[0] == "6":
            exit()
                        
    
if __name__ == "__main__":
    main()    
                    